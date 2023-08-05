/* Copyright 2020 The TensorFlow Authors. All Rights Reserved.

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

#ifndef TENSORFLOW_COMPILER_MLIR_HLO_INCLUDE_MLIR_HLO_DIALECT_MHLO_TRANSFORMS_PASSDETAIL_H_
#define TENSORFLOW_COMPILER_MLIR_HLO_INCLUDE_MLIR_HLO_DIALECT_MHLO_TRANSFORMS_PASSDETAIL_H_

#include "mlir/Pass/Pass.h"

namespace mlir {
namespace mhlo {

#define GEN_PASS_CLASSES
#include "mlir-hlo/Dialect/mhlo/transforms/mhlo_passes.h.inc"

}  // end namespace mhlo

namespace lmhlo {

#define GEN_PASS_CLASSES
#include "mlir-hlo/Dialect/mhlo/transforms/lmhlo_passes.h.inc"

}  // end namespace lmhlo

}  // end namespace mlir

namespace mlir {
namespace disc_ral {

#define GEN_PASS_CLASSES
#include "mlir-hlo/Dialect/mhlo/transforms/disc_ral_passes.h.inc"

}  // end namespace disc_ral
}  // end namespace mlir

#endif  // TENSORFLOW_COMPILER_MLIR_HLO_INCLUDE_MLIR_HLO_DIALECT_MHLO_TRANSFORMS_PASSDETAIL_H_
