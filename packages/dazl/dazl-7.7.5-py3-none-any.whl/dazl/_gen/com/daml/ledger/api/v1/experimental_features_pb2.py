# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/experimental_features.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/experimental_features.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\036ExperimentalFeaturesOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2com/daml/ledger/api/v1/experimental_features.proto\x12\x16\x63om.daml.ledger.api.v1\"\x82\x04\n\x14\x45xperimentalFeatures\x12v\n\x18self_service_error_codes\x18\x01 \x01(\x0b\x32\x39.com.daml.ledger.api.v1.ExperimentalSelfServiceErrorCodesB\x02\x18\x01R\x15selfServiceErrorCodes\x12O\n\x0bstatic_time\x18\x02 \x01(\x0b\x32..com.daml.ledger.api.v1.ExperimentalStaticTimeR\nstaticTime\x12i\n\x15\x63ommand_deduplication\x18\x03 \x01(\x0b\x32\x34.com.daml.ledger.api.v1.CommandDeduplicationFeaturesR\x14\x63ommandDeduplication\x12\x62\n\x12optional_ledger_id\x18\x04 \x01(\x0b\x32\x34.com.daml.ledger.api.v1.ExperimentalOptionalLedgerIdR\x10optionalLedgerId\x12R\n\x0c\x63ontract_ids\x18\x05 \x01(\x0b\x32/.com.daml.ledger.api.v1.ExperimentalContractIdsR\x0b\x63ontractIds\"\'\n!ExperimentalSelfServiceErrorCodes:\x02\x18\x01\"6\n\x16\x45xperimentalStaticTime\x12\x1c\n\tsupported\x18\x01 \x01(\x08R\tsupported\"\xcb\x02\n\x1c\x43ommandDeduplicationFeatures\x12{\n\x1c\x64\x65\x64uplication_period_support\x18\x01 \x01(\x0b\x32\x39.com.daml.ledger.api.v1.CommandDeduplicationPeriodSupportR\x1a\x64\x65\x64uplicationPeriodSupport\x12_\n\x12\x64\x65\x64uplication_type\x18\x02 \x01(\x0e\x32\x30.com.daml.ledger.api.v1.CommandDeduplicationTypeR\x11\x64\x65\x64uplicationType\x12M\n#max_deduplication_duration_enforced\x18\x03 \x01(\x08R maxDeduplicationDurationEnforced\"\x1e\n\x1c\x45xperimentalOptionalLedgerId\"\xbf\x03\n!CommandDeduplicationPeriodSupport\x12n\n\x0eoffset_support\x18\x01 \x01(\x0e\x32G.com.daml.ledger.api.v1.CommandDeduplicationPeriodSupport.OffsetSupportR\roffsetSupport\x12t\n\x10\x64uration_support\x18\x02 \x01(\x0e\x32I.com.daml.ledger.api.v1.CommandDeduplicationPeriodSupport.DurationSupportR\x0f\x64urationSupport\"d\n\rOffsetSupport\x12\x18\n\x14OFFSET_NOT_SUPPORTED\x10\x00\x12\x19\n\x15OFFSET_NATIVE_SUPPORT\x10\x01\x12\x1e\n\x1aOFFSET_CONVERT_TO_DURATION\x10\x02\"N\n\x0f\x44urationSupport\x12\x1b\n\x17\x44URATION_NATIVE_SUPPORT\x10\x00\x12\x1e\n\x1a\x44URATION_CONVERT_TO_OFFSET\x10\x01\"\xa5\x01\n\x17\x45xperimentalContractIds\x12S\n\x02v1\x18\x01 \x01(\x0e\x32\x43.com.daml.ledger.api.v1.ExperimentalContractIds.ContractIdV1SupportR\x02v1\"5\n\x13\x43ontractIdV1Support\x12\x0c\n\x08SUFFIXED\x10\x00\x12\x10\n\x0cNON_SUFFIXED\x10\x01*I\n\x18\x43ommandDeduplicationType\x12\x0e\n\nASYNC_ONLY\x10\x00\x12\x1d\n\x19\x41SYNC_AND_CONCURRENT_SYNC\x10\x01\x42\x98\x01\n\x16\x63om.daml.ledger.api.v1B\x1e\x45xperimentalFeaturesOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
)

_COMMANDDEDUPLICATIONTYPE = _descriptor.EnumDescriptor(
  name='CommandDeduplicationType',
  full_name='com.daml.ledger.api.v1.CommandDeduplicationType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ASYNC_ONLY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ASYNC_AND_CONCURRENT_SYNC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1676,
  serialized_end=1749,
)
_sym_db.RegisterEnumDescriptor(_COMMANDDEDUPLICATIONTYPE)

CommandDeduplicationType = enum_type_wrapper.EnumTypeWrapper(_COMMANDDEDUPLICATIONTYPE)
ASYNC_ONLY = 0
ASYNC_AND_CONCURRENT_SYNC = 1


_COMMANDDEDUPLICATIONPERIODSUPPORT_OFFSETSUPPORT = _descriptor.EnumDescriptor(
  name='OffsetSupport',
  full_name='com.daml.ledger.api.v1.CommandDeduplicationPeriodSupport.OffsetSupport',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFFSET_NOT_SUPPORTED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OFFSET_NATIVE_SUPPORT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OFFSET_CONVERT_TO_DURATION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1326,
  serialized_end=1426,
)
_sym_db.RegisterEnumDescriptor(_COMMANDDEDUPLICATIONPERIODSUPPORT_OFFSETSUPPORT)

_COMMANDDEDUPLICATIONPERIODSUPPORT_DURATIONSUPPORT = _descriptor.EnumDescriptor(
  name='DurationSupport',
  full_name='com.daml.ledger.api.v1.CommandDeduplicationPeriodSupport.DurationSupport',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DURATION_NATIVE_SUPPORT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DURATION_CONVERT_TO_OFFSET', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1428,
  serialized_end=1506,
)
_sym_db.RegisterEnumDescriptor(_COMMANDDEDUPLICATIONPERIODSUPPORT_DURATIONSUPPORT)

_EXPERIMENTALCONTRACTIDS_CONTRACTIDV1SUPPORT = _descriptor.EnumDescriptor(
  name='ContractIdV1Support',
  full_name='com.daml.ledger.api.v1.ExperimentalContractIds.ContractIdV1Support',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUFFIXED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NON_SUFFIXED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1621,
  serialized_end=1674,
)
_sym_db.RegisterEnumDescriptor(_EXPERIMENTALCONTRACTIDS_CONTRACTIDV1SUPPORT)


_EXPERIMENTALFEATURES = _descriptor.Descriptor(
  name='ExperimentalFeatures',
  full_name='com.daml.ledger.api.v1.ExperimentalFeatures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='self_service_error_codes', full_name='com.daml.ledger.api.v1.ExperimentalFeatures.self_service_error_codes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', json_name='selfServiceErrorCodes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='static_time', full_name='com.daml.ledger.api.v1.ExperimentalFeatures.static_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='staticTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command_deduplication', full_name='com.daml.ledger.api.v1.ExperimentalFeatures.command_deduplication', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commandDeduplication', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='optional_ledger_id', full_name='com.daml.ledger.api.v1.ExperimentalFeatures.optional_ledger_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='optionalLedgerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_ids', full_name='com.daml.ledger.api.v1.ExperimentalFeatures.contract_ids', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contractIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=79,
  serialized_end=593,
)


_EXPERIMENTALSELFSERVICEERRORCODES = _descriptor.Descriptor(
  name='ExperimentalSelfServiceErrorCodes',
  full_name='com.daml.ledger.api.v1.ExperimentalSelfServiceErrorCodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\030\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=595,
  serialized_end=634,
)


_EXPERIMENTALSTATICTIME = _descriptor.Descriptor(
  name='ExperimentalStaticTime',
  full_name='com.daml.ledger.api.v1.ExperimentalStaticTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='supported', full_name='com.daml.ledger.api.v1.ExperimentalStaticTime.supported', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='supported', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=636,
  serialized_end=690,
)


_COMMANDDEDUPLICATIONFEATURES = _descriptor.Descriptor(
  name='CommandDeduplicationFeatures',
  full_name='com.daml.ledger.api.v1.CommandDeduplicationFeatures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deduplication_period_support', full_name='com.daml.ledger.api.v1.CommandDeduplicationFeatures.deduplication_period_support', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='deduplicationPeriodSupport', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deduplication_type', full_name='com.daml.ledger.api.v1.CommandDeduplicationFeatures.deduplication_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='deduplicationType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_deduplication_duration_enforced', full_name='com.daml.ledger.api.v1.CommandDeduplicationFeatures.max_deduplication_duration_enforced', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='maxDeduplicationDurationEnforced', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=693,
  serialized_end=1024,
)


_EXPERIMENTALOPTIONALLEDGERID = _descriptor.Descriptor(
  name='ExperimentalOptionalLedgerId',
  full_name='com.daml.ledger.api.v1.ExperimentalOptionalLedgerId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1026,
  serialized_end=1056,
)


_COMMANDDEDUPLICATIONPERIODSUPPORT = _descriptor.Descriptor(
  name='CommandDeduplicationPeriodSupport',
  full_name='com.daml.ledger.api.v1.CommandDeduplicationPeriodSupport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset_support', full_name='com.daml.ledger.api.v1.CommandDeduplicationPeriodSupport.offset_support', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='offsetSupport', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration_support', full_name='com.daml.ledger.api.v1.CommandDeduplicationPeriodSupport.duration_support', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='durationSupport', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMANDDEDUPLICATIONPERIODSUPPORT_OFFSETSUPPORT,
    _COMMANDDEDUPLICATIONPERIODSUPPORT_DURATIONSUPPORT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1059,
  serialized_end=1506,
)


_EXPERIMENTALCONTRACTIDS = _descriptor.Descriptor(
  name='ExperimentalContractIds',
  full_name='com.daml.ledger.api.v1.ExperimentalContractIds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='v1', full_name='com.daml.ledger.api.v1.ExperimentalContractIds.v1', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='v1', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXPERIMENTALCONTRACTIDS_CONTRACTIDV1SUPPORT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1509,
  serialized_end=1674,
)

_EXPERIMENTALFEATURES.fields_by_name['self_service_error_codes'].message_type = _EXPERIMENTALSELFSERVICEERRORCODES
_EXPERIMENTALFEATURES.fields_by_name['static_time'].message_type = _EXPERIMENTALSTATICTIME
_EXPERIMENTALFEATURES.fields_by_name['command_deduplication'].message_type = _COMMANDDEDUPLICATIONFEATURES
_EXPERIMENTALFEATURES.fields_by_name['optional_ledger_id'].message_type = _EXPERIMENTALOPTIONALLEDGERID
_EXPERIMENTALFEATURES.fields_by_name['contract_ids'].message_type = _EXPERIMENTALCONTRACTIDS
_COMMANDDEDUPLICATIONFEATURES.fields_by_name['deduplication_period_support'].message_type = _COMMANDDEDUPLICATIONPERIODSUPPORT
_COMMANDDEDUPLICATIONFEATURES.fields_by_name['deduplication_type'].enum_type = _COMMANDDEDUPLICATIONTYPE
_COMMANDDEDUPLICATIONPERIODSUPPORT.fields_by_name['offset_support'].enum_type = _COMMANDDEDUPLICATIONPERIODSUPPORT_OFFSETSUPPORT
_COMMANDDEDUPLICATIONPERIODSUPPORT.fields_by_name['duration_support'].enum_type = _COMMANDDEDUPLICATIONPERIODSUPPORT_DURATIONSUPPORT
_COMMANDDEDUPLICATIONPERIODSUPPORT_OFFSETSUPPORT.containing_type = _COMMANDDEDUPLICATIONPERIODSUPPORT
_COMMANDDEDUPLICATIONPERIODSUPPORT_DURATIONSUPPORT.containing_type = _COMMANDDEDUPLICATIONPERIODSUPPORT
_EXPERIMENTALCONTRACTIDS.fields_by_name['v1'].enum_type = _EXPERIMENTALCONTRACTIDS_CONTRACTIDV1SUPPORT
_EXPERIMENTALCONTRACTIDS_CONTRACTIDV1SUPPORT.containing_type = _EXPERIMENTALCONTRACTIDS
DESCRIPTOR.message_types_by_name['ExperimentalFeatures'] = _EXPERIMENTALFEATURES
DESCRIPTOR.message_types_by_name['ExperimentalSelfServiceErrorCodes'] = _EXPERIMENTALSELFSERVICEERRORCODES
DESCRIPTOR.message_types_by_name['ExperimentalStaticTime'] = _EXPERIMENTALSTATICTIME
DESCRIPTOR.message_types_by_name['CommandDeduplicationFeatures'] = _COMMANDDEDUPLICATIONFEATURES
DESCRIPTOR.message_types_by_name['ExperimentalOptionalLedgerId'] = _EXPERIMENTALOPTIONALLEDGERID
DESCRIPTOR.message_types_by_name['CommandDeduplicationPeriodSupport'] = _COMMANDDEDUPLICATIONPERIODSUPPORT
DESCRIPTOR.message_types_by_name['ExperimentalContractIds'] = _EXPERIMENTALCONTRACTIDS
DESCRIPTOR.enum_types_by_name['CommandDeduplicationType'] = _COMMANDDEDUPLICATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExperimentalFeatures = _reflection.GeneratedProtocolMessageType('ExperimentalFeatures', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTALFEATURES,
  '__module__' : 'com.daml.ledger.api.v1.experimental_features_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.ExperimentalFeatures)
  })
_sym_db.RegisterMessage(ExperimentalFeatures)

ExperimentalSelfServiceErrorCodes = _reflection.GeneratedProtocolMessageType('ExperimentalSelfServiceErrorCodes', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTALSELFSERVICEERRORCODES,
  '__module__' : 'com.daml.ledger.api.v1.experimental_features_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.ExperimentalSelfServiceErrorCodes)
  })
_sym_db.RegisterMessage(ExperimentalSelfServiceErrorCodes)

ExperimentalStaticTime = _reflection.GeneratedProtocolMessageType('ExperimentalStaticTime', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTALSTATICTIME,
  '__module__' : 'com.daml.ledger.api.v1.experimental_features_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.ExperimentalStaticTime)
  })
_sym_db.RegisterMessage(ExperimentalStaticTime)

CommandDeduplicationFeatures = _reflection.GeneratedProtocolMessageType('CommandDeduplicationFeatures', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDDEDUPLICATIONFEATURES,
  '__module__' : 'com.daml.ledger.api.v1.experimental_features_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.CommandDeduplicationFeatures)
  })
_sym_db.RegisterMessage(CommandDeduplicationFeatures)

ExperimentalOptionalLedgerId = _reflection.GeneratedProtocolMessageType('ExperimentalOptionalLedgerId', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTALOPTIONALLEDGERID,
  '__module__' : 'com.daml.ledger.api.v1.experimental_features_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.ExperimentalOptionalLedgerId)
  })
_sym_db.RegisterMessage(ExperimentalOptionalLedgerId)

CommandDeduplicationPeriodSupport = _reflection.GeneratedProtocolMessageType('CommandDeduplicationPeriodSupport', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDDEDUPLICATIONPERIODSUPPORT,
  '__module__' : 'com.daml.ledger.api.v1.experimental_features_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.CommandDeduplicationPeriodSupport)
  })
_sym_db.RegisterMessage(CommandDeduplicationPeriodSupport)

ExperimentalContractIds = _reflection.GeneratedProtocolMessageType('ExperimentalContractIds', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTALCONTRACTIDS,
  '__module__' : 'com.daml.ledger.api.v1.experimental_features_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.ExperimentalContractIds)
  })
_sym_db.RegisterMessage(ExperimentalContractIds)


DESCRIPTOR._options = None
_EXPERIMENTALFEATURES.fields_by_name['self_service_error_codes']._options = None
_EXPERIMENTALSELFSERVICEERRORCODES._options = None
# @@protoc_insertion_point(module_scope)
