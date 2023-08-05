//===- TypeUtilities.h - Helper function for type queries -------*- C++ -*-===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//
//
// This file defines generic type utilities.
//
//===----------------------------------------------------------------------===//

#ifndef MLIR_SUPPORT_TYPEUTILITIES_H
#define MLIR_SUPPORT_TYPEUTILITIES_H

#include "mlir/IR/Operation.h"
#include "llvm/ADT/STLExtras.h"

namespace mlir {

class Attribute;
class TupleType;
class Type;
class Value;

//===----------------------------------------------------------------------===//
// Utility Functions
//===----------------------------------------------------------------------===//

/// Return the element type or return the type itself.
Type getElementTypeOrSelf(Type type);

/// Return the element type or return the type itself.
Type getElementTypeOrSelf(Attribute attr);
Type getElementTypeOrSelf(Value val);

/// Get the types within a nested Tuple. A helper for the class method that
/// handles storage concerns, which is tricky to do in tablegen.
SmallVector<Type, 10> getFlattenedTypes(TupleType t);

/// Return true if the specified type is an opaque type with the specified
/// dialect and typeData.
bool isOpaqueTypeWithName(Type type, StringRef dialect, StringRef typeData);

/// Returns success if the given two shapes are compatible. That is, they have
/// the same size and each pair of the elements are equal or one of them is
/// dynamic.
LogicalResult verifyCompatibleShape(ArrayRef<int64_t> shape1,
                                    ArrayRef<int64_t> shape2);

/// Returns success if the given two types have compatible shape. That is,
/// they are both scalars (not shaped), or they are both shaped types and at
/// least one is unranked or they have compatible dimensions. Dimensions are
/// compatible if at least one is dynamic or both are equal. The element type
/// does not matter.
LogicalResult verifyCompatibleShape(Type type1, Type type2);

/// Returns success if the given two arrays have the same number of elements and
/// each pair wise entries have compatible shape.
LogicalResult verifyCompatibleShapes(TypeRange types1, TypeRange types2);

/// Returns success if all given types have compatible shapes. That is, they are
/// all scalars (not shaped), or they are all shaped types and any ranked shapes
/// have compatible dimensions. The element type does not matter.
LogicalResult verifyCompatibleShapes(TypeRange types);

/// Dimensions are compatible if all non-dynamic dims are equal.
LogicalResult verifyCompatibleDims(ArrayRef<int64_t> dims);
//===----------------------------------------------------------------------===//
// Utility Iterators
//===----------------------------------------------------------------------===//

// An iterator for the element types of an op's operands of shaped types.
class OperandElementTypeIterator final
    : public llvm::mapped_iterator<Operation::operand_iterator,
                                   Type (*)(Value)> {
public:
  /// Initializes the result element type iterator to the specified operand
  /// iterator.
  explicit OperandElementTypeIterator(Operation::operand_iterator it);

private:
  static Type unwrap(Value value);
};

using OperandElementTypeRange = iterator_range<OperandElementTypeIterator>;

// An iterator for the tensor element types of an op's results of shaped types.
class ResultElementTypeIterator final
    : public llvm::mapped_iterator<Operation::result_iterator,
                                   Type (*)(Value)> {
public:
  /// Initializes the result element type iterator to the specified result
  /// iterator.
  explicit ResultElementTypeIterator(Operation::result_iterator it);

private:
  static Type unwrap(Value value);
};

using ResultElementTypeRange = iterator_range<ResultElementTypeIterator>;

} // end namespace mlir

#endif // MLIR_SUPPORT_TYPEUTILITIES_H
