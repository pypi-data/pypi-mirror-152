/* Copyright 2019 The TensorFlow Authors All Rights Reserved.

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
#ifndef TENSORFLOW_CORE_PROFILER_LIB_PROFILER_FACTORY_H_
#define TENSORFLOW_CORE_PROFILER_LIB_PROFILER_FACTORY_H_

#include <memory>
#include <vector>

#include "tensorflow/core/profiler/lib/profiler_interface.h"
#include "tensorflow/core/profiler/profiler_options.pb.h"

namespace tensorflow {
namespace profiler {

// A ProfilerFactory returns an instance of ProfilerInterface if ProfileOptions
// require it. Otherwise, it might return nullptr.
using ProfilerFactory =
    std::unique_ptr<ProfilerInterface> (*)(const ProfileOptions&);

// Registers a profiler factory. Should be invoked at most once per factory.
void RegisterProfilerFactory(ProfilerFactory factory);

// Invokes all registered profiler factories with the given options, and
// returns the instantiated (non-null) profiler interfaces in result.
void CreateProfilers(const ProfileOptions& options,
                     std::vector<std::unique_ptr<ProfilerInterface>>* result);

}  // namespace profiler
}  // namespace tensorflow

#endif  // TENSORFLOW_CORE_PROFILER_LIB_PROFILER_FACTORY_H_
