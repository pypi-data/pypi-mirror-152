# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/tpu/tpu_embedding_configuration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.protobuf.tpu import optimization_parameters_pb2 as tensorflow_dot_core_dot_protobuf_dot_tpu_dot_optimization__parameters__pb2
from tensorflow.core.protobuf.tpu import tpu_embedding_output_layout_pb2 as tensorflow_dot_core_dot_protobuf_dot_tpu_dot_tpu__embedding__output__layout__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/tpu/tpu_embedding_configuration.proto',
  package='tensorflow.tpu',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>tensorflow/core/protobuf/tpu/tpu_embedding_configuration.proto\x12\x0etensorflow.tpu\x1a:tensorflow/core/protobuf/tpu/optimization_parameters.proto\x1a>tensorflow/core/protobuf/tpu/tpu_embedding_output_layout.proto\"\x91\x06\n\x19TPUEmbeddingConfiguration\x12S\n\x10table_descriptor\x18\x01 \x03(\x0b\x32\x39.tensorflow.tpu.TPUEmbeddingConfiguration.TableDescriptor\x12<\n\x04mode\x18\x02 \x01(\x0e\x32..tensorflow.tpu.TPUEmbeddingConfiguration.Mode\x12\"\n\x1a\x62\x61tch_size_per_tensor_core\x18\x03 \x01(\x05\x12\x11\n\tnum_hosts\x18\x04 \x01(\x05\x12\x18\n\x10num_tensor_cores\x18\x05 \x01(\x05\x12U\n\x11sharding_strategy\x18\x06 \x01(\x0e\x32:.tensorflow.tpu.TPUEmbeddingConfiguration.ShardingStrategy\x12+\n#pipeline_execution_with_tensor_core\x18\x07 \x01(\x08\x12\x1e\n\x16profile_data_directory\x18\t \x01(\t\x12\x43\n\routput_layout\x18\x08 \x01(\x0b\x32(.tensorflow.tpu.TPUEmbeddingOutputLayoutB\x02\x18\x01\x1a\xaa\x01\n\x0fTableDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0fvocabulary_size\x18\x02 \x01(\x03\x12\x11\n\tdimension\x18\x03 \x01(\x05\x12\x14\n\x0cnum_features\x18\x04 \x01(\x05\x12G\n\x17optimization_parameters\x18\x05 \x01(\x0b\x32&.tensorflow.tpu.OptimizationParameters\"L\n\x04Mode\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tINFERENCE\x10\x01\x12\x0c\n\x08TRAINING\x10\x02\x12\x16\n\x12\x42\x41\x43KWARD_PASS_ONLY\x10\x03\",\n\x10ShardingStrategy\x12\x0f\n\x0b\x44IV_DEFAULT\x10\x00\x12\x07\n\x03MOD\x10\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_protobuf_dot_tpu_dot_optimization__parameters__pb2.DESCRIPTOR,tensorflow_dot_core_dot_protobuf_dot_tpu_dot_tpu__embedding__output__layout__pb2.DESCRIPTOR,])



_TPUEMBEDDINGCONFIGURATION_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='tensorflow.tpu.TPUEmbeddingConfiguration.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFERENCE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BACKWARD_PASS_ONLY', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=870,
  serialized_end=946,
)
_sym_db.RegisterEnumDescriptor(_TPUEMBEDDINGCONFIGURATION_MODE)

_TPUEMBEDDINGCONFIGURATION_SHARDINGSTRATEGY = _descriptor.EnumDescriptor(
  name='ShardingStrategy',
  full_name='tensorflow.tpu.TPUEmbeddingConfiguration.ShardingStrategy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIV_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=948,
  serialized_end=992,
)
_sym_db.RegisterEnumDescriptor(_TPUEMBEDDINGCONFIGURATION_SHARDINGSTRATEGY)


_TPUEMBEDDINGCONFIGURATION_TABLEDESCRIPTOR = _descriptor.Descriptor(
  name='TableDescriptor',
  full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TableDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TableDescriptor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocabulary_size', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TableDescriptor.vocabulary_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimension', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TableDescriptor.dimension', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_features', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TableDescriptor.num_features', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimization_parameters', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.TableDescriptor.optimization_parameters', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=868,
)

_TPUEMBEDDINGCONFIGURATION = _descriptor.Descriptor(
  name='TPUEmbeddingConfiguration',
  full_name='tensorflow.tpu.TPUEmbeddingConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_descriptor', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.table_descriptor', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size_per_tensor_core', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.batch_size_per_tensor_core', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_hosts', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.num_hosts', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_tensor_cores', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.num_tensor_cores', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sharding_strategy', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.sharding_strategy', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline_execution_with_tensor_core', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.pipeline_execution_with_tensor_core', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile_data_directory', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.profile_data_directory', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_layout', full_name='tensorflow.tpu.TPUEmbeddingConfiguration.output_layout', index=8,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TPUEMBEDDINGCONFIGURATION_TABLEDESCRIPTOR, ],
  enum_types=[
    _TPUEMBEDDINGCONFIGURATION_MODE,
    _TPUEMBEDDINGCONFIGURATION_SHARDINGSTRATEGY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=992,
)

_TPUEMBEDDINGCONFIGURATION_TABLEDESCRIPTOR.fields_by_name['optimization_parameters'].message_type = tensorflow_dot_core_dot_protobuf_dot_tpu_dot_optimization__parameters__pb2._OPTIMIZATIONPARAMETERS
_TPUEMBEDDINGCONFIGURATION_TABLEDESCRIPTOR.containing_type = _TPUEMBEDDINGCONFIGURATION
_TPUEMBEDDINGCONFIGURATION.fields_by_name['table_descriptor'].message_type = _TPUEMBEDDINGCONFIGURATION_TABLEDESCRIPTOR
_TPUEMBEDDINGCONFIGURATION.fields_by_name['mode'].enum_type = _TPUEMBEDDINGCONFIGURATION_MODE
_TPUEMBEDDINGCONFIGURATION.fields_by_name['sharding_strategy'].enum_type = _TPUEMBEDDINGCONFIGURATION_SHARDINGSTRATEGY
_TPUEMBEDDINGCONFIGURATION.fields_by_name['output_layout'].message_type = tensorflow_dot_core_dot_protobuf_dot_tpu_dot_tpu__embedding__output__layout__pb2._TPUEMBEDDINGOUTPUTLAYOUT
_TPUEMBEDDINGCONFIGURATION_MODE.containing_type = _TPUEMBEDDINGCONFIGURATION
_TPUEMBEDDINGCONFIGURATION_SHARDINGSTRATEGY.containing_type = _TPUEMBEDDINGCONFIGURATION
DESCRIPTOR.message_types_by_name['TPUEmbeddingConfiguration'] = _TPUEMBEDDINGCONFIGURATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TPUEmbeddingConfiguration = _reflection.GeneratedProtocolMessageType('TPUEmbeddingConfiguration', (_message.Message,), {

  'TableDescriptor' : _reflection.GeneratedProtocolMessageType('TableDescriptor', (_message.Message,), {
    'DESCRIPTOR' : _TPUEMBEDDINGCONFIGURATION_TABLEDESCRIPTOR,
    '__module__' : 'tensorflow.core.protobuf.tpu.tpu_embedding_configuration_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.tpu.TPUEmbeddingConfiguration.TableDescriptor)
    })
  ,
  'DESCRIPTOR' : _TPUEMBEDDINGCONFIGURATION,
  '__module__' : 'tensorflow.core.protobuf.tpu.tpu_embedding_configuration_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tpu.TPUEmbeddingConfiguration)
  })
_sym_db.RegisterMessage(TPUEmbeddingConfiguration)
_sym_db.RegisterMessage(TPUEmbeddingConfiguration.TableDescriptor)


_TPUEMBEDDINGCONFIGURATION.fields_by_name['output_layout']._options = None
# @@protoc_insertion_point(module_scope)
