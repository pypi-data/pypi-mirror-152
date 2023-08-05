/* Copyright 2019 The TensorFlow Authors. All Rights Reserved.

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

// Null implementation of the PercentileSampler metric for mobile platforms.

#ifndef TENSORFLOW_CORE_LIB_MONITORING_MOBILE_PERCENTILE_SAMPLER_H_
#define TENSORFLOW_CORE_LIB_MONITORING_MOBILE_PERCENTILE_SAMPLER_H_

#if !defined(IS_MOBILE_PLATFORM) || \
    !defined(TENSORFLOW_INCLUDED_FROM_PERCENTILE_SAMPLER_H)
// If this header file were included directly, and something else included its
// non-mobile counterpart, there could be an unchecked ODR violation on the
// classes below.
#error do not include mobile_percentile_sampler.h directly; use percetile_sampler.h instead
#endif  // !defined(IS_MOBILE_PLATFORM) ||
        // !defined(TENSORFLOW_INCLUDED_FROM_PERCENTILE_SAMPLER_H)

#include "tensorflow/core/lib/core/status.h"
#include "tensorflow/core/lib/monitoring/collection_registry.h"
#include "tensorflow/core/lib/monitoring/metric_def.h"
#include "tensorflow/core/lib/monitoring/types.h"
#include "tensorflow/core/platform/macros.h"

namespace tensorflow {
namespace monitoring {

class PercentileSamplerCell {
 public:
  void Add(double sample) {}

  Percentiles value() const { return Percentiles(); }
};

template <int NumLabels>
class PercentileSampler {
 public:
  static PercentileSampler* New(
      const MetricDef<MetricKind::kCumulative, Percentiles, NumLabels>&
          metric_def,
      std::vector<double> percentiles, size_t max_samples,
      UnitOfMeasure unit_of_measure);

  template <typename... Labels>
  PercentileSamplerCell* GetCell(const Labels&... labels) {
    return &default_cell_;
  }

  Status GetStatus() { return Status::OK(); }

 private:
  PercentileSamplerCell default_cell_;

  PercentileSampler() = default;

  TF_DISALLOW_COPY_AND_ASSIGN(PercentileSampler);
};

template <int NumLabels>
PercentileSampler<NumLabels>* PercentileSampler<NumLabels>::New(
    const MetricDef<MetricKind::kCumulative, Percentiles, NumLabels>&
    /* metric_def */,
    std::vector<double> /* percentiles */, size_t /* max_samples */,
    UnitOfMeasure /* unit_of_measure */) {
  return new PercentileSampler<NumLabels>();
}

}  // namespace monitoring
}  // namespace tensorflow

#endif  // TENSORFLOW_CORE_LIB_MONITORING_MOBILE_PERCENTILE_SAMPLER_H_
