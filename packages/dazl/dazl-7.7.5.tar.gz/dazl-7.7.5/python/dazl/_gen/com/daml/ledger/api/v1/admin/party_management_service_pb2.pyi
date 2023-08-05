# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.internal.containers import RepeatedCompositeFieldContainer, RepeatedScalarFieldContainer
from google.protobuf.message import Message as _Message

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "GetParticipantIdRequest",
    "GetParticipantIdResponse",
    "GetPartiesRequest",
    "GetPartiesResponse",
    "ListKnownPartiesRequest",
    "ListKnownPartiesResponse",
    "AllocatePartyRequest",
    "AllocatePartyResponse",
    "PartyDetails",
]


class GetParticipantIdRequest(_Message):
    def __init__(self): ...
    def HasField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def ClearField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetParticipantIdResponse(_Message):
    participant_id: _builtins.str
    def __init__(self, *, participant_id: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _L["participant_id"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["participant_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPartiesRequest(_Message):
    @property
    def parties(self) -> RepeatedScalarFieldContainer[_builtins.str]: ...
    def __init__(self, *, parties: _typing.Optional[_typing.Iterable[_builtins.str]] = ...): ...
    def HasField(self, field_name: _L["parties"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["parties"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPartiesResponse(_Message):
    @property
    def party_details(self) -> RepeatedCompositeFieldContainer[PartyDetails]: ...
    def __init__(self, *, party_details: _typing.Optional[_typing.Iterable[PartyDetails]] = ...): ...
    def HasField(self, field_name: _L["party_details"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["party_details"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ListKnownPartiesRequest(_Message):
    def __init__(self): ...
    def HasField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def ClearField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ListKnownPartiesResponse(_Message):
    @property
    def party_details(self) -> RepeatedCompositeFieldContainer[PartyDetails]: ...
    def __init__(self, *, party_details: _typing.Optional[_typing.Iterable[PartyDetails]] = ...): ...
    def HasField(self, field_name: _L["party_details"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["party_details"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class AllocatePartyRequest(_Message):
    party_id_hint: _builtins.str
    display_name: _builtins.str
    def __init__(self, *, party_id_hint: _typing.Optional[_builtins.str] = ..., display_name: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _L["party_id_hint", "display_name"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["party_id_hint", "display_name"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class AllocatePartyResponse(_Message):
    @property
    def party_details(self) -> PartyDetails: ...
    def __init__(self, *, party_details: _typing.Optional[PartyDetails] = ...): ...
    def HasField(self, field_name: _L["party_details"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["party_details"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class PartyDetails(_Message):
    party: _builtins.str
    display_name: _builtins.str
    is_local: _builtins.bool
    def __init__(self, *, party: _typing.Optional[_builtins.str] = ..., display_name: _typing.Optional[_builtins.str] = ..., is_local: _typing.Optional[_builtins.bool] = ...): ...
    def HasField(self, field_name: _L["party", "display_name", "is_local"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["party", "display_name", "is_local"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
