# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/completion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/completion.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\024CompletionOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'com/daml/ledger/api/v1/completion.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto\"\x99\x03\n\nCompletion\x12\x1d\n\ncommand_id\x18\x01 \x01(\tR\tcommandId\x12*\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status\x12%\n\x0etransaction_id\x18\x03 \x01(\tR\rtransactionId\x12%\n\x0e\x61pplication_id\x18\x04 \x01(\tR\rapplicationId\x12\x15\n\x06\x61\x63t_as\x18\x05 \x03(\tR\x05\x61\x63tAs\x12#\n\rsubmission_id\x18\x06 \x01(\tR\x0csubmissionId\x12\x33\n\x14\x64\x65\x64uplication_offset\x18\x08 \x01(\tH\x00R\x13\x64\x65\x64uplicationOffset\x12R\n\x16\x64\x65\x64uplication_duration\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationH\x00R\x15\x64\x65\x64uplicationDurationB\x16\n\x14\x64\x65\x64uplication_periodJ\x04\x08\x07\x10\x08R\x0fsubmission_rankB\x8e\x01\n\x16\x63om.daml.ledger.api.v1B\x14\x43ompletionOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_COMPLETION = _descriptor.Descriptor(
  name='Completion',
  full_name='com.daml.ledger.api.v1.Completion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_id', full_name='com.daml.ledger.api.v1.Completion.command_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commandId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='com.daml.ledger.api.v1.Completion.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='com.daml.ledger.api.v1.Completion.transaction_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='transactionId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='application_id', full_name='com.daml.ledger.api.v1.Completion.application_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='applicationId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='act_as', full_name='com.daml.ledger.api.v1.Completion.act_as', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='actAs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submission_id', full_name='com.daml.ledger.api.v1.Completion.submission_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='submissionId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deduplication_offset', full_name='com.daml.ledger.api.v1.Completion.deduplication_offset', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='deduplicationOffset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deduplication_duration', full_name='com.daml.ledger.api.v1.Completion.deduplication_duration', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='deduplicationDuration', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='deduplication_period', full_name='com.daml.ledger.api.v1.Completion.deduplication_period',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=125,
  serialized_end=534,
)

_COMPLETION.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_COMPLETION.fields_by_name['deduplication_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_COMPLETION.oneofs_by_name['deduplication_period'].fields.append(
  _COMPLETION.fields_by_name['deduplication_offset'])
_COMPLETION.fields_by_name['deduplication_offset'].containing_oneof = _COMPLETION.oneofs_by_name['deduplication_period']
_COMPLETION.oneofs_by_name['deduplication_period'].fields.append(
  _COMPLETION.fields_by_name['deduplication_duration'])
_COMPLETION.fields_by_name['deduplication_duration'].containing_oneof = _COMPLETION.oneofs_by_name['deduplication_period']
DESCRIPTOR.message_types_by_name['Completion'] = _COMPLETION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Completion = _reflection.GeneratedProtocolMessageType('Completion', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETION,
  '__module__' : 'com.daml.ledger.api.v1.completion_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.Completion)
  })
_sym_db.RegisterMessage(Completion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
