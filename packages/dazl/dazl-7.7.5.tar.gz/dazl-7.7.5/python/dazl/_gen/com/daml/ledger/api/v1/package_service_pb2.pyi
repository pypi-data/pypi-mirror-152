# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.descriptor import EnumDescriptor
from google.protobuf.internal.containers import RepeatedScalarFieldContainer
from google.protobuf.message import Message as _Message

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "ListPackagesRequest",
    "ListPackagesResponse",
    "GetPackageRequest",
    "GetPackageResponse",
    "GetPackageStatusRequest",
    "GetPackageStatusResponse",
]

class PackageStatus:
    DESCRIPTOR: _typing.ClassVar[EnumDescriptor] = ...
    UNKNOWN: _typing.ClassVar[_L[0]] = ...
    REGISTERED: _typing.ClassVar[_L[1]] = ...
UNKNOWN = _L[0]
REGISTERED = _L[1]

class HashFunction:
    DESCRIPTOR: _typing.ClassVar[EnumDescriptor] = ...
    SHA256: _typing.ClassVar[_L[0]] = ...
SHA256 = _L[0]


class ListPackagesRequest(_Message):
    ledger_id: _builtins.str
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _L["ledger_id"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["ledger_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ListPackagesResponse(_Message):
    @property
    def package_ids(self) -> RepeatedScalarFieldContainer[_builtins.str]: ...
    def __init__(self, *, package_ids: _typing.Optional[_typing.Iterable[_builtins.str]] = ...): ...
    def HasField(self, field_name: _L["package_ids"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["package_ids"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPackageRequest(_Message):
    ledger_id: _builtins.str
    package_id: _builtins.str
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ..., package_id: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _L["ledger_id", "package_id"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["ledger_id", "package_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPackageResponse(_Message):
    @property
    def hash_function(self) -> _L[0]: ...
    archive_payload: _builtins.bytes
    hash: _builtins.str
    def __init__(self, *, hash_function: _typing.Optional[_L['SHA256', 0]] = ..., archive_payload: _typing.Optional[_builtins.bytes] = ..., hash: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _L["hash_function", "archive_payload", "hash"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["hash_function", "archive_payload", "hash"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPackageStatusRequest(_Message):
    ledger_id: _builtins.str
    package_id: _builtins.str
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ..., package_id: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _L["ledger_id", "package_id"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["ledger_id", "package_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPackageStatusResponse(_Message):
    @property
    def package_status(self) -> _L[0, 1]: ...
    def __init__(self, *, package_status: _typing.Optional[_L['UNKNOWN', 0, 'REGISTERED', 1]] = ...): ...
    def HasField(self, field_name: _L["package_status"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["package_status"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
