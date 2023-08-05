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

// This file defines the attributes used in the TensorFlow dialect.

#ifndef TENSORFLOW_COMPILER_MLIR_TENSORFLOW_IR_TF_ATTRIBUTES_H_
#define TENSORFLOW_COMPILER_MLIR_TENSORFLOW_IR_TF_ATTRIBUTES_H_

#include "llvm/ADT/StringRef.h"
#include "mlir/IR/BuiltinAttributes.h"  // from @llvm-project
#include "mlir/IR/BuiltinTypes.h"  // from @llvm-project
#include "mlir/IR/MLIRContext.h"  // from @llvm-project
#include "mlir/IR/OpDefinition.h"  // from @llvm-project

#define GET_ATTRDEF_CLASSES
#include "tensorflow/compiler/mlir/tensorflow/ir/tf_attributes.h.inc"

#endif  // TENSORFLOW_COMPILER_MLIR_TENSORFLOW_IR_TF_ATTRIBUTES_H_
