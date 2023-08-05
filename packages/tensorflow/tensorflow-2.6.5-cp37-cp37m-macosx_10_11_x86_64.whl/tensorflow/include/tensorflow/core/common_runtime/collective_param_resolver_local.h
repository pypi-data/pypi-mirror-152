/* Copyright 2018 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/
#ifndef TENSORFLOW_CORE_COMMON_RUNTIME_COLLECTIVE_PARAM_RESOLVER_LOCAL_H_
#define TENSORFLOW_CORE_COMMON_RUNTIME_COLLECTIVE_PARAM_RESOLVER_LOCAL_H_

#include <functional>
#include <memory>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

#include "tensorflow/core/framework/collective.h"
#include "tensorflow/core/framework/device_attributes.pb.h"
#include "tensorflow/core/lib/gtl/flatmap.h"
#include "tensorflow/core/platform/thread_annotations.h"

namespace tensorflow {
class CompleteGroupRequest;
class CompleteGroupResponse;
class CompleteInstanceRequest;
class CompleteInstanceResponse;
class ConfigProto;
class DeviceMgr;

// Implements ParamResolverInterface for a single-task context.
// It also implements the functionality necessary to serve as the
// group leader for param resolution in a multi-task context.
class CollectiveParamResolverLocal : public ParamResolverInterface {
 public:
  CollectiveParamResolverLocal(const ConfigProto& config,
                               const DeviceMgr* dev_mgr,
                               DeviceResolverInterface* dev_resolver,
                               NcclCommunicatorInterface* nccl_communicator,
                               const string& task_name);

  ~CollectiveParamResolverLocal() override {}

  void CompleteParamsAsync(const DeviceAttributes& device, CollectiveParams* cp,
                           CancellationManager* cancel_mgr,
                           const StatusCallback& done) override;

  void CompleteGroupAsync(const CompleteGroupRequest* request,
                          CompleteGroupResponse* response,
                          CancellationManager* cancel_mgr,
                          const StatusCallback& done) override;

  void CompleteInstanceAsync(const CompleteInstanceRequest* request,
                             CompleteInstanceResponse* response,
                             CancellationManager* cancel_mgr,
                             const StatusCallback& done) override;

  void StartAbort(const Status& s) override;

 protected:
  // For access to InstanceRec and CompleteDefaultRanking.
  friend class CollectiveParamResolverLocalTest;

  // Used to complete/verify CollGroup.
  struct GroupRec {
    mutable mutex mu;
    CollGroupParams group TF_GUARDED_BY(mu);
    Status status TF_GUARDED_BY(mu);
    std::unordered_map<string, DeviceAttributes> devices TF_GUARDED_BY(mu);
    std::vector<StatusCallback> waiting TF_GUARDED_BY(mu);
  };

  // Finds the GroupRec that corresponds to cp->group_key.
  // Also populates cp->group from that group_rec.
  // Will wait until GroupRec is fully populated or an error arises before
  // calling done.  Callback GroupRec* arg is only valid if status is ok.
  // Ownership of GroupRec stays with this object and does not pass to the
  // callback.
  typedef std::function<void(const Status& s, const GroupRec* gr)>
      GroupRecCallback;
  void CompleteGroupLocal(const DeviceAttributes& device, CollectiveParams* cp,
                          const GroupRecCallback& done,
                          CancellationManager* cancel_mgr)
      TF_LOCKS_EXCLUDED(group_mu_);

  // Finishes the group parameters once all members of the group are there.
  void FinishGroup(GroupRec* gr) TF_EXCLUSIVE_LOCKS_REQUIRED(gr->mu);

  // Used to complete/verify CollInstance.
  struct InstanceRec;

  typedef std::function<void(InstanceRec*)> IRConsumer;
  struct InstanceRec {
    mutex mu;
    // Values to be shared by all instances, constant after initialization.
    CollectiveParams* shared;
    // If an error occurs during initialization this structure stays in the
    // table with a non-OK status. Purging the table and restarting needs to be
    // done at a higher level.
    Status status TF_GUARDED_BY(mu);

    // These fields are used to count the instances that have called
    // in and become known while resolving broadcast source identity and
    // communicator key.
    int source_rank TF_GUARDED_BY(mu);
    string communicator_key TF_GUARDED_BY(mu);
    int known_count TF_GUARDED_BY(mu);
    std::vector<bool> known TF_GUARDED_BY(mu);
    std::vector<IRConsumer> known_waiters TF_GUARDED_BY(mu);

    InstanceRec()
        : shared(new CollectiveParams()), source_rank(-1), known_count(0) {}
    ~InstanceRec() { shared->Unref(); }
  };

  // Find the InstanceRec with the same instance_key as cp.  If it doesn't
  // already exist, create and initialize from gr and cp.
  // created is set to true if a new IRec is created, false otherwise.
  //
  // Precondition: *gr must be a complete GroupRec, i.e. the value set
  // by CompleteGroupLocal. *cp must be populated with all the fields
  // required by InitInstanceSharedParams.  Ownership of InstanceRec stays
  // with this object and does not pass to the callback.
  InstanceRec* GetOrCreateInstanceRec(const GroupRec* gr, CollectiveParams* cp,
                                      bool* created)
      TF_LOCKS_EXCLUDED(instance_mu_, gr->mu, group_mu_);

  // Populate *ir with device membership from gr, then initialize to be specific
  // to cp->instance_key, i.e. order the devices and tasks.
  //
  // Preconditions:
  //  cp is populated with all DeviceLocalities
  void InitInstanceSharedParams(const GroupRec* gr, const CollectiveParams* cp,
                                InstanceRec* ir) TF_LOCKS_EXCLUDED(gr->mu);

  // Establishes the final order of gp->device_names and gp->task_names by
  // considering localities of all devices.
  void CompleteDefaultRanking(const std::vector<DeviceAttributes>& attributes,
                              CollGroupParams* gp);

  // Finish populating *cp.
  // Precondition: *gr has been fully populated by CompleteGroupLocal.
  void CompleteInstanceLocal(const string& device, const GroupRec* gr,
                             CollectiveParams* cp, bool is_source,
                             const StatusCallback& done)
      TF_LOCKS_EXCLUDED(instance_mu_, gr->mu, group_mu_);

  // Finish populating *cp from fully initialized *ir.
  // Precondition: *gr and *ir are fully populated.
  void CompleteInstanceFromInitializedIRec(const string& device,
                                           const GroupRec* gr,
                                           CollectiveParams* cp,
                                           InstanceRec* ir, bool is_source,
                                           const StatusCallback& done)
      TF_LOCKS_EXCLUDED(ir->mu);

  // Complete instance params after waiting for group.
  // Precondition: *cp has complete group data and default_rank.
  void WaitForGroup(InstanceRec* ir, CollectiveParams* cp, bool is_source,
                    const IRConsumer& f) TF_LOCKS_EXCLUDED(ir->mu);

  // If cp.device_names contains only devices local to this process
  // populates *localities, else returns an error.
  Status GetLocalDeviceLocalities(const CollectiveParams& cp,
                                  std::vector<DeviceLocality>* localities);

  // Sets CollTaskParams.is_local and CollectiveParams.default_rank.
  // Precondition: cp->device_names is fully populated and in final order.
  void CompleteTaskIsLocal(const string& task_name, CollectiveParams* cp);

  // Sets cp->instance_default_rank according to location of device in
  // current ordering of cp->instance.device_names.
  void SetDefaultRank(const string& device, CollectiveParams* cp);

  // Sets cp->instance.type based on collective op type, and attempts to assign
  // best implementation.
  void AssignCollectiveType(CollectiveParams* cp);

  void StartAbortLocal(const Status& s)
      TF_LOCKS_EXCLUDED(status_mu_, group_mu_, instance_mu_);

  const bool nccl_;
  const DeviceMgr* dev_mgr_;
  DeviceResolverInterface* dev_resolver_;  // Not owned.
  NcclCommunicatorInterface* nccl_communicator_;  // Not owned.
  string task_name_;
  string gpu_ring_order_;
  mutex group_mu_;
  gtl::FlatMap<int32, std::unique_ptr<GroupRec>> group_table_
      TF_GUARDED_BY(group_mu_);
  mutex instance_mu_;
  gtl::FlatMap<int32, gtl::FlatMap<int32, std::unique_ptr<InstanceRec>>>
      instance_table_ TF_GUARDED_BY(instance_mu_);
  mutex status_mu_;
  Status status_ TF_GUARDED_BY(status_mu_);
};

}  // namespace tensorflow

#endif  // TENSORFLOW_CORE_COMMON_RUNTIME_COLLECTIVE_PARAM_RESOLVER_LOCAL_H_
