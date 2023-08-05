# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/testing/reset_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/testing/reset_service.proto',
  package='com.daml.ledger.api.v1.testing',
  syntax='proto3',
  serialized_options=b'\n\036com.daml.ledger.api.v1.testingB\026ResetServiceOuterClassZWgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1/testing\252\002\036Com.Daml.Ledger.Api.V1.Testing',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2com/daml/ledger/api/v1/testing/reset_service.proto\x12\x1e\x63om.daml.ledger.api.v1.testing\x1a\x1bgoogle/protobuf/empty.proto\"+\n\x0cResetRequest\x12\x1b\n\tledger_id\x18\x01 \x01(\tR\x08ledgerId2]\n\x0cResetService\x12M\n\x05Reset\x12,.com.daml.ledger.api.v1.testing.ResetRequest\x1a\x16.google.protobuf.EmptyB\xb2\x01\n\x1e\x63om.daml.ledger.api.v1.testingB\x16ResetServiceOuterClassZWgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1/testing\xaa\x02\x1e\x43om.Daml.Ledger.Api.V1.Testingb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_RESETREQUEST = _descriptor.Descriptor(
  name='ResetRequest',
  full_name='com.daml.ledger.api.v1.testing.ResetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.testing.ResetRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ledgerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=115,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['ResetRequest'] = _RESETREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResetRequest = _reflection.GeneratedProtocolMessageType('ResetRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.testing.reset_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.testing.ResetRequest)
  })
_sym_db.RegisterMessage(ResetRequest)


DESCRIPTOR._options = None

_RESETSERVICE = _descriptor.ServiceDescriptor(
  name='ResetService',
  full_name='com.daml.ledger.api.v1.testing.ResetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=160,
  serialized_end=253,
  methods=[
  _descriptor.MethodDescriptor(
    name='Reset',
    full_name='com.daml.ledger.api.v1.testing.ResetService.Reset',
    index=0,
    containing_service=None,
    input_type=_RESETREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESETSERVICE)

DESCRIPTOR.services_by_name['ResetService'] = _RESETSERVICE

# @@protoc_insertion_point(module_scope)
