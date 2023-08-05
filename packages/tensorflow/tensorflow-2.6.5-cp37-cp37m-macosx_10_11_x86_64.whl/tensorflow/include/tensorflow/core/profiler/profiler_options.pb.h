// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: tensorflow/core/profiler/profiler_options.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3009000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3009002 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto {
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::AuxillaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTable schema[2]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::FieldMetadata field_metadata[];
  static const ::PROTOBUF_NAMESPACE_ID::internal::SerializationTable serialization_table[];
  static const ::PROTOBUF_NAMESPACE_ID::uint32 offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto;
namespace tensorflow {
class ProfileOptions;
class ProfileOptionsDefaultTypeInternal;
extern ProfileOptionsDefaultTypeInternal _ProfileOptions_default_instance_;
class RemoteProfilerSessionManagerOptions;
class RemoteProfilerSessionManagerOptionsDefaultTypeInternal;
extern RemoteProfilerSessionManagerOptionsDefaultTypeInternal _RemoteProfilerSessionManagerOptions_default_instance_;
}  // namespace tensorflow
PROTOBUF_NAMESPACE_OPEN
template<> ::tensorflow::ProfileOptions* Arena::CreateMaybeMessage<::tensorflow::ProfileOptions>(Arena*);
template<> ::tensorflow::RemoteProfilerSessionManagerOptions* Arena::CreateMaybeMessage<::tensorflow::RemoteProfilerSessionManagerOptions>(Arena*);
PROTOBUF_NAMESPACE_CLOSE
namespace tensorflow {

enum ProfileOptions_DeviceType : int {
  ProfileOptions_DeviceType_UNSPECIFIED = 0,
  ProfileOptions_DeviceType_CPU = 1,
  ProfileOptions_DeviceType_GPU = 2,
  ProfileOptions_DeviceType_TPU = 3,
  ProfileOptions_DeviceType_ProfileOptions_DeviceType_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::PROTOBUF_NAMESPACE_ID::int32>::min(),
  ProfileOptions_DeviceType_ProfileOptions_DeviceType_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::PROTOBUF_NAMESPACE_ID::int32>::max()
};
bool ProfileOptions_DeviceType_IsValid(int value);
constexpr ProfileOptions_DeviceType ProfileOptions_DeviceType_DeviceType_MIN = ProfileOptions_DeviceType_UNSPECIFIED;
constexpr ProfileOptions_DeviceType ProfileOptions_DeviceType_DeviceType_MAX = ProfileOptions_DeviceType_TPU;
constexpr int ProfileOptions_DeviceType_DeviceType_ARRAYSIZE = ProfileOptions_DeviceType_DeviceType_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* ProfileOptions_DeviceType_descriptor();
template<typename T>
inline const std::string& ProfileOptions_DeviceType_Name(T enum_t_value) {
  static_assert(::std::is_same<T, ProfileOptions_DeviceType>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function ProfileOptions_DeviceType_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    ProfileOptions_DeviceType_descriptor(), enum_t_value);
}
inline bool ProfileOptions_DeviceType_Parse(
    const std::string& name, ProfileOptions_DeviceType* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<ProfileOptions_DeviceType>(
    ProfileOptions_DeviceType_descriptor(), name, value);
}
// ===================================================================

class ProfileOptions :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:tensorflow.ProfileOptions) */ {
 public:
  ProfileOptions();
  virtual ~ProfileOptions();

  ProfileOptions(const ProfileOptions& from);
  ProfileOptions(ProfileOptions&& from) noexcept
    : ProfileOptions() {
    *this = ::std::move(from);
  }

  inline ProfileOptions& operator=(const ProfileOptions& from) {
    CopyFrom(from);
    return *this;
  }
  inline ProfileOptions& operator=(ProfileOptions&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const ProfileOptions& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const ProfileOptions* internal_default_instance() {
    return reinterpret_cast<const ProfileOptions*>(
               &_ProfileOptions_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(ProfileOptions& a, ProfileOptions& b) {
    a.Swap(&b);
  }
  inline void Swap(ProfileOptions* other) {
    if (other == this) return;
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline ProfileOptions* New() const final {
    return CreateMaybeMessage<ProfileOptions>(nullptr);
  }

  ProfileOptions* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<ProfileOptions>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const ProfileOptions& from);
  void MergeFrom(const ProfileOptions& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(ProfileOptions* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "tensorflow.ProfileOptions";
  }
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto);
    return ::descriptor_table_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  typedef ProfileOptions_DeviceType DeviceType;
  static constexpr DeviceType UNSPECIFIED =
    ProfileOptions_DeviceType_UNSPECIFIED;
  static constexpr DeviceType CPU =
    ProfileOptions_DeviceType_CPU;
  static constexpr DeviceType GPU =
    ProfileOptions_DeviceType_GPU;
  static constexpr DeviceType TPU =
    ProfileOptions_DeviceType_TPU;
  static inline bool DeviceType_IsValid(int value) {
    return ProfileOptions_DeviceType_IsValid(value);
  }
  static constexpr DeviceType DeviceType_MIN =
    ProfileOptions_DeviceType_DeviceType_MIN;
  static constexpr DeviceType DeviceType_MAX =
    ProfileOptions_DeviceType_DeviceType_MAX;
  static constexpr int DeviceType_ARRAYSIZE =
    ProfileOptions_DeviceType_DeviceType_ARRAYSIZE;
  static inline const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor*
  DeviceType_descriptor() {
    return ProfileOptions_DeviceType_descriptor();
  }
  template<typename T>
  static inline const std::string& DeviceType_Name(T enum_t_value) {
    static_assert(::std::is_same<T, DeviceType>::value ||
      ::std::is_integral<T>::value,
      "Incorrect type passed to function DeviceType_Name.");
    return ProfileOptions_DeviceType_Name(enum_t_value);
  }
  static inline bool DeviceType_Parse(const std::string& name,
      DeviceType* value) {
    return ProfileOptions_DeviceType_Parse(name, value);
  }

  // accessors -------------------------------------------------------

  enum : int {
    kRepositoryPathFieldNumber = 10,
    kHostTracerLevelFieldNumber = 2,
    kDeviceTracerLevelFieldNumber = 3,
    kPythonTracerLevelFieldNumber = 4,
    kIncludeDatasetOpsFieldNumber = 1,
    kEnableHloProtoFieldNumber = 7,
    kVersionFieldNumber = 5,
    kDeviceTypeFieldNumber = 6,
    kStartTimestampNsFieldNumber = 8,
    kDurationMsFieldNumber = 9,
  };
  // string repository_path = 10;
  void clear_repository_path();
  const std::string& repository_path() const;
  void set_repository_path(const std::string& value);
  void set_repository_path(std::string&& value);
  void set_repository_path(const char* value);
  void set_repository_path(const char* value, size_t size);
  std::string* mutable_repository_path();
  std::string* release_repository_path();
  void set_allocated_repository_path(std::string* repository_path);

  // uint32 host_tracer_level = 2;
  void clear_host_tracer_level();
  ::PROTOBUF_NAMESPACE_ID::uint32 host_tracer_level() const;
  void set_host_tracer_level(::PROTOBUF_NAMESPACE_ID::uint32 value);

  // uint32 device_tracer_level = 3;
  void clear_device_tracer_level();
  ::PROTOBUF_NAMESPACE_ID::uint32 device_tracer_level() const;
  void set_device_tracer_level(::PROTOBUF_NAMESPACE_ID::uint32 value);

  // uint32 python_tracer_level = 4;
  void clear_python_tracer_level();
  ::PROTOBUF_NAMESPACE_ID::uint32 python_tracer_level() const;
  void set_python_tracer_level(::PROTOBUF_NAMESPACE_ID::uint32 value);

  // bool include_dataset_ops = 1;
  void clear_include_dataset_ops();
  bool include_dataset_ops() const;
  void set_include_dataset_ops(bool value);

  // bool enable_hlo_proto = 7;
  void clear_enable_hlo_proto();
  bool enable_hlo_proto() const;
  void set_enable_hlo_proto(bool value);

  // uint32 version = 5;
  void clear_version();
  ::PROTOBUF_NAMESPACE_ID::uint32 version() const;
  void set_version(::PROTOBUF_NAMESPACE_ID::uint32 value);

  // .tensorflow.ProfileOptions.DeviceType device_type = 6;
  void clear_device_type();
  ::tensorflow::ProfileOptions_DeviceType device_type() const;
  void set_device_type(::tensorflow::ProfileOptions_DeviceType value);

  // uint64 start_timestamp_ns = 8;
  void clear_start_timestamp_ns();
  ::PROTOBUF_NAMESPACE_ID::uint64 start_timestamp_ns() const;
  void set_start_timestamp_ns(::PROTOBUF_NAMESPACE_ID::uint64 value);

  // uint64 duration_ms = 9;
  void clear_duration_ms();
  ::PROTOBUF_NAMESPACE_ID::uint64 duration_ms() const;
  void set_duration_ms(::PROTOBUF_NAMESPACE_ID::uint64 value);

  // @@protoc_insertion_point(class_scope:tensorflow.ProfileOptions)
 private:
  class _Internal;

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr repository_path_;
  ::PROTOBUF_NAMESPACE_ID::uint32 host_tracer_level_;
  ::PROTOBUF_NAMESPACE_ID::uint32 device_tracer_level_;
  ::PROTOBUF_NAMESPACE_ID::uint32 python_tracer_level_;
  bool include_dataset_ops_;
  bool enable_hlo_proto_;
  ::PROTOBUF_NAMESPACE_ID::uint32 version_;
  int device_type_;
  ::PROTOBUF_NAMESPACE_ID::uint64 start_timestamp_ns_;
  ::PROTOBUF_NAMESPACE_ID::uint64 duration_ms_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto;
};
// -------------------------------------------------------------------

class RemoteProfilerSessionManagerOptions :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:tensorflow.RemoteProfilerSessionManagerOptions) */ {
 public:
  RemoteProfilerSessionManagerOptions();
  virtual ~RemoteProfilerSessionManagerOptions();

  RemoteProfilerSessionManagerOptions(const RemoteProfilerSessionManagerOptions& from);
  RemoteProfilerSessionManagerOptions(RemoteProfilerSessionManagerOptions&& from) noexcept
    : RemoteProfilerSessionManagerOptions() {
    *this = ::std::move(from);
  }

  inline RemoteProfilerSessionManagerOptions& operator=(const RemoteProfilerSessionManagerOptions& from) {
    CopyFrom(from);
    return *this;
  }
  inline RemoteProfilerSessionManagerOptions& operator=(RemoteProfilerSessionManagerOptions&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const RemoteProfilerSessionManagerOptions& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const RemoteProfilerSessionManagerOptions* internal_default_instance() {
    return reinterpret_cast<const RemoteProfilerSessionManagerOptions*>(
               &_RemoteProfilerSessionManagerOptions_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  friend void swap(RemoteProfilerSessionManagerOptions& a, RemoteProfilerSessionManagerOptions& b) {
    a.Swap(&b);
  }
  inline void Swap(RemoteProfilerSessionManagerOptions* other) {
    if (other == this) return;
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline RemoteProfilerSessionManagerOptions* New() const final {
    return CreateMaybeMessage<RemoteProfilerSessionManagerOptions>(nullptr);
  }

  RemoteProfilerSessionManagerOptions* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<RemoteProfilerSessionManagerOptions>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const RemoteProfilerSessionManagerOptions& from);
  void MergeFrom(const RemoteProfilerSessionManagerOptions& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(RemoteProfilerSessionManagerOptions* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "tensorflow.RemoteProfilerSessionManagerOptions";
  }
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto);
    return ::descriptor_table_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kServiceAddressesFieldNumber = 2,
    kProfilerOptionsFieldNumber = 1,
    kSessionCreationTimestampNsFieldNumber = 3,
    kMaxSessionDurationMsFieldNumber = 4,
    kDelayMsFieldNumber = 5,
  };
  // repeated string service_addresses = 2;
  int service_addresses_size() const;
  void clear_service_addresses();
  const std::string& service_addresses(int index) const;
  std::string* mutable_service_addresses(int index);
  void set_service_addresses(int index, const std::string& value);
  void set_service_addresses(int index, std::string&& value);
  void set_service_addresses(int index, const char* value);
  void set_service_addresses(int index, const char* value, size_t size);
  std::string* add_service_addresses();
  void add_service_addresses(const std::string& value);
  void add_service_addresses(std::string&& value);
  void add_service_addresses(const char* value);
  void add_service_addresses(const char* value, size_t size);
  const ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField<std::string>& service_addresses() const;
  ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField<std::string>* mutable_service_addresses();

  // .tensorflow.ProfileOptions profiler_options = 1;
  bool has_profiler_options() const;
  void clear_profiler_options();
  const ::tensorflow::ProfileOptions& profiler_options() const;
  ::tensorflow::ProfileOptions* release_profiler_options();
  ::tensorflow::ProfileOptions* mutable_profiler_options();
  void set_allocated_profiler_options(::tensorflow::ProfileOptions* profiler_options);

  // uint64 session_creation_timestamp_ns = 3;
  void clear_session_creation_timestamp_ns();
  ::PROTOBUF_NAMESPACE_ID::uint64 session_creation_timestamp_ns() const;
  void set_session_creation_timestamp_ns(::PROTOBUF_NAMESPACE_ID::uint64 value);

  // uint64 max_session_duration_ms = 4;
  void clear_max_session_duration_ms();
  ::PROTOBUF_NAMESPACE_ID::uint64 max_session_duration_ms() const;
  void set_max_session_duration_ms(::PROTOBUF_NAMESPACE_ID::uint64 value);

  // uint64 delay_ms = 5;
  void clear_delay_ms();
  ::PROTOBUF_NAMESPACE_ID::uint64 delay_ms() const;
  void set_delay_ms(::PROTOBUF_NAMESPACE_ID::uint64 value);

  // @@protoc_insertion_point(class_scope:tensorflow.RemoteProfilerSessionManagerOptions)
 private:
  class _Internal;

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField<std::string> service_addresses_;
  ::tensorflow::ProfileOptions* profiler_options_;
  ::PROTOBUF_NAMESPACE_ID::uint64 session_creation_timestamp_ns_;
  ::PROTOBUF_NAMESPACE_ID::uint64 max_session_duration_ms_;
  ::PROTOBUF_NAMESPACE_ID::uint64 delay_ms_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// ProfileOptions

// uint32 version = 5;
inline void ProfileOptions::clear_version() {
  version_ = 0u;
}
inline ::PROTOBUF_NAMESPACE_ID::uint32 ProfileOptions::version() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.version)
  return version_;
}
inline void ProfileOptions::set_version(::PROTOBUF_NAMESPACE_ID::uint32 value) {
  
  version_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.version)
}

// .tensorflow.ProfileOptions.DeviceType device_type = 6;
inline void ProfileOptions::clear_device_type() {
  device_type_ = 0;
}
inline ::tensorflow::ProfileOptions_DeviceType ProfileOptions::device_type() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.device_type)
  return static_cast< ::tensorflow::ProfileOptions_DeviceType >(device_type_);
}
inline void ProfileOptions::set_device_type(::tensorflow::ProfileOptions_DeviceType value) {
  
  device_type_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.device_type)
}

// bool include_dataset_ops = 1;
inline void ProfileOptions::clear_include_dataset_ops() {
  include_dataset_ops_ = false;
}
inline bool ProfileOptions::include_dataset_ops() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.include_dataset_ops)
  return include_dataset_ops_;
}
inline void ProfileOptions::set_include_dataset_ops(bool value) {
  
  include_dataset_ops_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.include_dataset_ops)
}

// uint32 host_tracer_level = 2;
inline void ProfileOptions::clear_host_tracer_level() {
  host_tracer_level_ = 0u;
}
inline ::PROTOBUF_NAMESPACE_ID::uint32 ProfileOptions::host_tracer_level() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.host_tracer_level)
  return host_tracer_level_;
}
inline void ProfileOptions::set_host_tracer_level(::PROTOBUF_NAMESPACE_ID::uint32 value) {
  
  host_tracer_level_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.host_tracer_level)
}

// uint32 device_tracer_level = 3;
inline void ProfileOptions::clear_device_tracer_level() {
  device_tracer_level_ = 0u;
}
inline ::PROTOBUF_NAMESPACE_ID::uint32 ProfileOptions::device_tracer_level() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.device_tracer_level)
  return device_tracer_level_;
}
inline void ProfileOptions::set_device_tracer_level(::PROTOBUF_NAMESPACE_ID::uint32 value) {
  
  device_tracer_level_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.device_tracer_level)
}

// uint32 python_tracer_level = 4;
inline void ProfileOptions::clear_python_tracer_level() {
  python_tracer_level_ = 0u;
}
inline ::PROTOBUF_NAMESPACE_ID::uint32 ProfileOptions::python_tracer_level() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.python_tracer_level)
  return python_tracer_level_;
}
inline void ProfileOptions::set_python_tracer_level(::PROTOBUF_NAMESPACE_ID::uint32 value) {
  
  python_tracer_level_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.python_tracer_level)
}

// bool enable_hlo_proto = 7;
inline void ProfileOptions::clear_enable_hlo_proto() {
  enable_hlo_proto_ = false;
}
inline bool ProfileOptions::enable_hlo_proto() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.enable_hlo_proto)
  return enable_hlo_proto_;
}
inline void ProfileOptions::set_enable_hlo_proto(bool value) {
  
  enable_hlo_proto_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.enable_hlo_proto)
}

// uint64 start_timestamp_ns = 8;
inline void ProfileOptions::clear_start_timestamp_ns() {
  start_timestamp_ns_ = PROTOBUF_ULONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::uint64 ProfileOptions::start_timestamp_ns() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.start_timestamp_ns)
  return start_timestamp_ns_;
}
inline void ProfileOptions::set_start_timestamp_ns(::PROTOBUF_NAMESPACE_ID::uint64 value) {
  
  start_timestamp_ns_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.start_timestamp_ns)
}

// uint64 duration_ms = 9;
inline void ProfileOptions::clear_duration_ms() {
  duration_ms_ = PROTOBUF_ULONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::uint64 ProfileOptions::duration_ms() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.duration_ms)
  return duration_ms_;
}
inline void ProfileOptions::set_duration_ms(::PROTOBUF_NAMESPACE_ID::uint64 value) {
  
  duration_ms_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.duration_ms)
}

// string repository_path = 10;
inline void ProfileOptions::clear_repository_path() {
  repository_path_.ClearToEmptyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline const std::string& ProfileOptions::repository_path() const {
  // @@protoc_insertion_point(field_get:tensorflow.ProfileOptions.repository_path)
  return repository_path_.GetNoArena();
}
inline void ProfileOptions::set_repository_path(const std::string& value) {
  
  repository_path_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:tensorflow.ProfileOptions.repository_path)
}
inline void ProfileOptions::set_repository_path(std::string&& value) {
  
  repository_path_.SetNoArena(
    &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:tensorflow.ProfileOptions.repository_path)
}
inline void ProfileOptions::set_repository_path(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  
  repository_path_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:tensorflow.ProfileOptions.repository_path)
}
inline void ProfileOptions::set_repository_path(const char* value, size_t size) {
  
  repository_path_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:tensorflow.ProfileOptions.repository_path)
}
inline std::string* ProfileOptions::mutable_repository_path() {
  
  // @@protoc_insertion_point(field_mutable:tensorflow.ProfileOptions.repository_path)
  return repository_path_.MutableNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline std::string* ProfileOptions::release_repository_path() {
  // @@protoc_insertion_point(field_release:tensorflow.ProfileOptions.repository_path)
  
  return repository_path_.ReleaseNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline void ProfileOptions::set_allocated_repository_path(std::string* repository_path) {
  if (repository_path != nullptr) {
    
  } else {
    
  }
  repository_path_.SetAllocatedNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), repository_path);
  // @@protoc_insertion_point(field_set_allocated:tensorflow.ProfileOptions.repository_path)
}

// -------------------------------------------------------------------

// RemoteProfilerSessionManagerOptions

// .tensorflow.ProfileOptions profiler_options = 1;
inline bool RemoteProfilerSessionManagerOptions::has_profiler_options() const {
  return this != internal_default_instance() && profiler_options_ != nullptr;
}
inline void RemoteProfilerSessionManagerOptions::clear_profiler_options() {
  if (GetArenaNoVirtual() == nullptr && profiler_options_ != nullptr) {
    delete profiler_options_;
  }
  profiler_options_ = nullptr;
}
inline const ::tensorflow::ProfileOptions& RemoteProfilerSessionManagerOptions::profiler_options() const {
  const ::tensorflow::ProfileOptions* p = profiler_options_;
  // @@protoc_insertion_point(field_get:tensorflow.RemoteProfilerSessionManagerOptions.profiler_options)
  return p != nullptr ? *p : *reinterpret_cast<const ::tensorflow::ProfileOptions*>(
      &::tensorflow::_ProfileOptions_default_instance_);
}
inline ::tensorflow::ProfileOptions* RemoteProfilerSessionManagerOptions::release_profiler_options() {
  // @@protoc_insertion_point(field_release:tensorflow.RemoteProfilerSessionManagerOptions.profiler_options)
  
  ::tensorflow::ProfileOptions* temp = profiler_options_;
  profiler_options_ = nullptr;
  return temp;
}
inline ::tensorflow::ProfileOptions* RemoteProfilerSessionManagerOptions::mutable_profiler_options() {
  
  if (profiler_options_ == nullptr) {
    auto* p = CreateMaybeMessage<::tensorflow::ProfileOptions>(GetArenaNoVirtual());
    profiler_options_ = p;
  }
  // @@protoc_insertion_point(field_mutable:tensorflow.RemoteProfilerSessionManagerOptions.profiler_options)
  return profiler_options_;
}
inline void RemoteProfilerSessionManagerOptions::set_allocated_profiler_options(::tensorflow::ProfileOptions* profiler_options) {
  ::PROTOBUF_NAMESPACE_ID::Arena* message_arena = GetArenaNoVirtual();
  if (message_arena == nullptr) {
    delete profiler_options_;
  }
  if (profiler_options) {
    ::PROTOBUF_NAMESPACE_ID::Arena* submessage_arena = nullptr;
    if (message_arena != submessage_arena) {
      profiler_options = ::PROTOBUF_NAMESPACE_ID::internal::GetOwnedMessage(
          message_arena, profiler_options, submessage_arena);
    }
    
  } else {
    
  }
  profiler_options_ = profiler_options;
  // @@protoc_insertion_point(field_set_allocated:tensorflow.RemoteProfilerSessionManagerOptions.profiler_options)
}

// repeated string service_addresses = 2;
inline int RemoteProfilerSessionManagerOptions::service_addresses_size() const {
  return service_addresses_.size();
}
inline void RemoteProfilerSessionManagerOptions::clear_service_addresses() {
  service_addresses_.Clear();
}
inline const std::string& RemoteProfilerSessionManagerOptions::service_addresses(int index) const {
  // @@protoc_insertion_point(field_get:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
  return service_addresses_.Get(index);
}
inline std::string* RemoteProfilerSessionManagerOptions::mutable_service_addresses(int index) {
  // @@protoc_insertion_point(field_mutable:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
  return service_addresses_.Mutable(index);
}
inline void RemoteProfilerSessionManagerOptions::set_service_addresses(int index, const std::string& value) {
  // @@protoc_insertion_point(field_set:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
  service_addresses_.Mutable(index)->assign(value);
}
inline void RemoteProfilerSessionManagerOptions::set_service_addresses(int index, std::string&& value) {
  // @@protoc_insertion_point(field_set:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
  service_addresses_.Mutable(index)->assign(std::move(value));
}
inline void RemoteProfilerSessionManagerOptions::set_service_addresses(int index, const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  service_addresses_.Mutable(index)->assign(value);
  // @@protoc_insertion_point(field_set_char:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
}
inline void RemoteProfilerSessionManagerOptions::set_service_addresses(int index, const char* value, size_t size) {
  service_addresses_.Mutable(index)->assign(
    reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_set_pointer:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
}
inline std::string* RemoteProfilerSessionManagerOptions::add_service_addresses() {
  // @@protoc_insertion_point(field_add_mutable:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
  return service_addresses_.Add();
}
inline void RemoteProfilerSessionManagerOptions::add_service_addresses(const std::string& value) {
  service_addresses_.Add()->assign(value);
  // @@protoc_insertion_point(field_add:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
}
inline void RemoteProfilerSessionManagerOptions::add_service_addresses(std::string&& value) {
  service_addresses_.Add(std::move(value));
  // @@protoc_insertion_point(field_add:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
}
inline void RemoteProfilerSessionManagerOptions::add_service_addresses(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  service_addresses_.Add()->assign(value);
  // @@protoc_insertion_point(field_add_char:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
}
inline void RemoteProfilerSessionManagerOptions::add_service_addresses(const char* value, size_t size) {
  service_addresses_.Add()->assign(reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_add_pointer:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
}
inline const ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField<std::string>&
RemoteProfilerSessionManagerOptions::service_addresses() const {
  // @@protoc_insertion_point(field_list:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
  return service_addresses_;
}
inline ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField<std::string>*
RemoteProfilerSessionManagerOptions::mutable_service_addresses() {
  // @@protoc_insertion_point(field_mutable_list:tensorflow.RemoteProfilerSessionManagerOptions.service_addresses)
  return &service_addresses_;
}

// uint64 session_creation_timestamp_ns = 3;
inline void RemoteProfilerSessionManagerOptions::clear_session_creation_timestamp_ns() {
  session_creation_timestamp_ns_ = PROTOBUF_ULONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::uint64 RemoteProfilerSessionManagerOptions::session_creation_timestamp_ns() const {
  // @@protoc_insertion_point(field_get:tensorflow.RemoteProfilerSessionManagerOptions.session_creation_timestamp_ns)
  return session_creation_timestamp_ns_;
}
inline void RemoteProfilerSessionManagerOptions::set_session_creation_timestamp_ns(::PROTOBUF_NAMESPACE_ID::uint64 value) {
  
  session_creation_timestamp_ns_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.RemoteProfilerSessionManagerOptions.session_creation_timestamp_ns)
}

// uint64 max_session_duration_ms = 4;
inline void RemoteProfilerSessionManagerOptions::clear_max_session_duration_ms() {
  max_session_duration_ms_ = PROTOBUF_ULONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::uint64 RemoteProfilerSessionManagerOptions::max_session_duration_ms() const {
  // @@protoc_insertion_point(field_get:tensorflow.RemoteProfilerSessionManagerOptions.max_session_duration_ms)
  return max_session_duration_ms_;
}
inline void RemoteProfilerSessionManagerOptions::set_max_session_duration_ms(::PROTOBUF_NAMESPACE_ID::uint64 value) {
  
  max_session_duration_ms_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.RemoteProfilerSessionManagerOptions.max_session_duration_ms)
}

// uint64 delay_ms = 5;
inline void RemoteProfilerSessionManagerOptions::clear_delay_ms() {
  delay_ms_ = PROTOBUF_ULONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::uint64 RemoteProfilerSessionManagerOptions::delay_ms() const {
  // @@protoc_insertion_point(field_get:tensorflow.RemoteProfilerSessionManagerOptions.delay_ms)
  return delay_ms_;
}
inline void RemoteProfilerSessionManagerOptions::set_delay_ms(::PROTOBUF_NAMESPACE_ID::uint64 value) {
  
  delay_ms_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.RemoteProfilerSessionManagerOptions.delay_ms)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace tensorflow

PROTOBUF_NAMESPACE_OPEN

template <> struct is_proto_enum< ::tensorflow::ProfileOptions_DeviceType> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::tensorflow::ProfileOptions_DeviceType>() {
  return ::tensorflow::ProfileOptions_DeviceType_descriptor();
}

PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fprofiler_2fprofiler_5foptions_2eproto
