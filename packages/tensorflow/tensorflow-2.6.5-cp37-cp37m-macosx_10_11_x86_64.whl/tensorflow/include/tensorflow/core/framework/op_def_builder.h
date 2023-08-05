/* Copyright 2015 The TensorFlow Authors. All Rights Reserved.

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

// Class and associated machinery for specifying an Op's OpDef and shape
// inference function for Op registration.

#ifndef TENSORFLOW_CORE_FRAMEWORK_OP_DEF_BUILDER_H_
#define TENSORFLOW_CORE_FRAMEWORK_OP_DEF_BUILDER_H_

#include <string>
#include <vector>

#include "tensorflow/core/framework/op_def.pb.h"
#include "tensorflow/core/lib/core/status.h"
#include "tensorflow/core/lib/core/stringpiece.h"
#include "tensorflow/core/platform/macros.h"

namespace tensorflow {

typedef std::function<Status(OpDef* c)> OpTypeConstructor;

class FunctionDefHelper;

namespace shape_inference {
class InferenceContext;
}
typedef std::function<Status(shape_inference::InferenceContext* c)>
    OpShapeInferenceFn;

struct OpRegistrationData {
 public:
  OpRegistrationData() {}
  OpRegistrationData(const OpDef& def) : op_def(def) {}
  OpRegistrationData(const OpDef& def, const OpShapeInferenceFn& fn,
                     bool is_function = false)
      : op_def(def), shape_inference_fn(fn), is_function_op(is_function) {}

  OpDef op_def;
  OpShapeInferenceFn shape_inference_fn;

  // Type constructor. This callable initializes the type of this op.
  // It is provided as a programmatic mechanism for defining an op's
  // type, as part of its registration. It is to be eventually replaced by a
  // textual language.
  //
  // Important: historically, op registrations only contained partial
  // input/output type information in non-standardized attribute declarations
  // (e.g. typically, input types were held in a `dtype` attribute). The type
  // constructor currently duplicates such attribute information, with the aim
  // of entirely subsuming it, and eventually deprecating all type-related
  // attributes.
  //
  // Since ops are typically parametrized, the type created by this constructor
  // is also parametric.
  //
  // Example: for an op `Foo(x: T) -> Bar[T]`:
  //
  //  * typically, its op registration included a single attribute `T: type`;
  //    then the respective input was defined as `x: T`; the output type `Bar`
  //    was implied by the op name.
  //  * the type constructor creates a FullType object containing `Bar[T]`; this
  //    still relies on the `T` attribute which it references.
  //  * in the future, the type constructor will create a FullType containing
  //    `Callable[(x: T), Bar[T]]`, and the attribute `T` will be deprecated.
  OpTypeConstructor type_ctor;

  bool is_function_op = false;
};

// Builder class passed to the REGISTER_OP() macro.
class OpDefBuilder {
 public:
  // Constructs an OpDef with just the name field set.
  explicit OpDefBuilder(std::string op_name);

  // Adds an attr to this OpDefBuilder (and returns *this). The spec has
  // format "<name>:<type>" or "<name>:<type>=<default>"
  // where <name> matches regexp [a-zA-Z][a-zA-Z0-9_]*
  // (by convention only using capital letters for attrs that can be inferred)
  // <type> can be:
  //   "string", "int", "float", "bool", "type", "shape", or "tensor"
  //   "numbertype", "realnumbertype", "quantizedtype"
  //       (meaning "type" with a restriction on valid values)
  //   "{int32,int64}" or {realnumbertype,quantizedtype,string}"
  //       (meaning "type" with a restriction containing unions of value types)
  //   "{\"foo\", \"bar\n baz\"}", or "{'foo', 'bar\n baz'}"
  //       (meaning "string" with a restriction on valid values)
  //   "list(string)", ..., "list(tensor)", "list(numbertype)", ...
  //       (meaning lists of the above types)
  //   "int >= 2" (meaning "int" with a restriction on valid values)
  //   "list(string) >= 2", "list(int) >= 2"
  //       (meaning "list(string)" / "list(int)" with length at least 2)
  // <default>, if included, should use the Proto text format
  // of <type>.  For lists use [a, b, c] format.
  //
  // Note that any attr specifying the length of an input or output will
  // get a default minimum of 1 unless the >= # syntax is used.
  //
  // TODO(josh11b): Perhaps support restrictions and defaults as optional
  // extra arguments to Attr() instead of encoding them in the spec string.
  // TODO(josh11b): Would like to have better dtype handling for tensor attrs:
  // * Ability to say the type of an input/output matches the type of
  //   the tensor.
  // * Ability to restrict the type of the tensor like the existing
  //   restrictions for type attrs.
  // Perhaps by linking the type of the tensor to a type attr?
  OpDefBuilder& Attr(std::string spec);

  // Adds an input or output to this OpDefBuilder (and returns *this).
  // The spec has form "<name>:<type-expr>" or "<name>:Ref(<type-expr>)"
  // where <name> matches regexp [a-z][a-z0-9_]* and <type-expr> can be:
  // * For a single tensor: <type>
  // * For a sequence of tensors with the same type: <number>*<type>
  // * For a sequence of tensors with different types: <type-list>
  // Where:
  //   <type> is either one of "float", "int32", "string", ...
  //                 or the name of an attr (see above) with type "type".
  //   <number> is the name of an attr with type "int".
  //   <type-list> is the name of an attr with type "list(type)".
  // TODO(josh11b): Indicate Ref() via an optional argument instead of
  // in the spec?
  // TODO(josh11b): SparseInput() and SparseOutput() matching the Python
  // handling?
  OpDefBuilder& Input(std::string spec);
  OpDefBuilder& Output(std::string spec);

  // Turns on the indicated boolean flag in this OpDefBuilder (and
  // returns *this).
  OpDefBuilder& SetIsCommutative();
  OpDefBuilder& SetIsAggregate();
  OpDefBuilder& SetIsStateful();
  OpDefBuilder& SetAllowsUninitializedInput();
  OpDefBuilder& SetIsDistributedCommunication();

  // Deprecate the op at a certain GraphDef version.
  OpDefBuilder& Deprecated(int version, std::string explanation);

  // Adds docs to this OpDefBuilder (and returns *this).
  // Docs have the format:
  //   <1-line summary>
  //   <rest of the description>
  //   <name>: <description of name>
  //   <name>: <description of name>
  //     <if long, indent the description on subsequent lines>
  // Where <name> is the name of an attr, input, or output.  Please
  // wrap docs at 72 columns so that it may be indented in the
  // generated output.  For tensor inputs or outputs (not attrs), you
  // may start the description with an "=" (like name:= <description>)
  // to suppress the automatically-generated type documentation in
  // generated output.
#ifndef TF_LEAN_BINARY
  OpDefBuilder& Doc(std::string text);
#else
  OpDefBuilder& Doc(string text) { return *this; }
#endif

  // Sets the function to be used as type constructor. Type constructors are
  // called just before a graph node is finalized, which also happens before
  // shape inference.
  OpDefBuilder& SetTypeConstructor(OpTypeConstructor c);

  // Sets the shape function to be used for shape inference.
  //
  // Note that currently (October 2016), python code still requires a
  // RegisterShape call to invoke this; see call_cpp_shape_fn in
  // python/framework/common_shapes.py
  OpDefBuilder& SetShapeFn(OpShapeInferenceFn fn);

  // Allows the `<type>` in calls to `Attr()` to be "any".
  // This is used by PythonAPIWrapper for pass-through parameters.
  OpDefBuilder& AllowAttrTypeAny();

  // Sets op_reg_data->op_def to the requested OpDef and
  // op_reg_data->shape_inference_fn to the requested shape inference function,
  // or returns an error.
  // Must be called after all of the above methods.
  //
  // Note that OpDefBuilder only reports parsing errors.  You should also
  // call ValidateOpDef() to detect other problems.
  Status Finalize(OpRegistrationData* op_reg_data) const;

 private:
  friend class FunctionDefHelper;

  // Adds control output to this OpDefBuilder (and returns *this).
  // The <name> must be a valid node name (matches regexp
  // [a-zA-Z][a-zA-Z0-9_]*). Named control output can only exist for functions.
  OpDefBuilder& ControlOutput(std::string name);

  OpDef* op_def() { return &op_reg_data_.op_def; }

  OpRegistrationData op_reg_data_;
  std::vector<string> attrs_;
  std::vector<string> inputs_;
  std::vector<string> outputs_;
  std::vector<string> control_outputs_;
  std::string doc_;
  std::vector<string> errors_;
  bool allow_attr_type_any_ = false;
};

}  // namespace tensorflow

#endif  // TENSORFLOW_CORE_FRAMEWORK_OP_DEF_BUILDER_H_
