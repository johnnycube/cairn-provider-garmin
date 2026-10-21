import datetime

from cairn.v1 import activity_pb2 as _activity_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GearKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GEAR_KIND_UNSPECIFIED: _ClassVar[GearKind]
    GEAR_KIND_BIKE: _ClassVar[GearKind]
    GEAR_KIND_SHOE: _ClassVar[GearKind]
    GEAR_KIND_OTHER: _ClassVar[GearKind]
GEAR_KIND_UNSPECIFIED: GearKind
GEAR_KIND_BIKE: GearKind
GEAR_KIND_SHOE: GearKind
GEAR_KIND_OTHER: GearKind

class Gear(_message.Message):
    __slots__ = ("id", "kind", "name", "brand", "model", "notes", "purchase_date", "retired", "retired_at", "total_distance_m", "total_moving_s", "activity_count", "external_refs", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_DATE_FIELD_NUMBER: _ClassVar[int]
    RETIRED_FIELD_NUMBER: _ClassVar[int]
    RETIRED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISTANCE_M_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MOVING_S_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: GearKind
    name: str
    brand: str
    model: str
    notes: str
    purchase_date: str
    retired: bool
    retired_at: _timestamp_pb2.Timestamp
    total_distance_m: float
    total_moving_s: int
    activity_count: int
    external_refs: _containers.RepeatedCompositeFieldContainer[GearExternalRef]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[GearKind, str]] = ..., name: _Optional[str] = ..., brand: _Optional[str] = ..., model: _Optional[str] = ..., notes: _Optional[str] = ..., purchase_date: _Optional[str] = ..., retired: _Optional[bool] = ..., retired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_distance_m: _Optional[float] = ..., total_moving_s: _Optional[int] = ..., activity_count: _Optional[int] = ..., external_refs: _Optional[_Iterable[_Union[GearExternalRef, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GearExternalRef(_message.Message):
    __slots__ = ("provider", "external_account_id", "external_id", "provider_name", "provider_distance_m", "primary", "last_seen_at", "gear_id", "kind", "brand", "model", "description", "retired", "default_for")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_DISTANCE_M_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    GEAR_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RETIRED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FOR_FIELD_NUMBER: _ClassVar[int]
    provider: str
    external_account_id: str
    external_id: str
    provider_name: str
    provider_distance_m: float
    primary: bool
    last_seen_at: _timestamp_pb2.Timestamp
    gear_id: str
    kind: GearKind
    brand: str
    model: str
    description: str
    retired: bool
    default_for: _containers.RepeatedScalarFieldContainer[_activity_pb2.ActivityType]
    def __init__(self, provider: _Optional[str] = ..., external_account_id: _Optional[str] = ..., external_id: _Optional[str] = ..., provider_name: _Optional[str] = ..., provider_distance_m: _Optional[float] = ..., primary: _Optional[bool] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gear_id: _Optional[str] = ..., kind: _Optional[_Union[GearKind, str]] = ..., brand: _Optional[str] = ..., model: _Optional[str] = ..., description: _Optional[str] = ..., retired: _Optional[bool] = ..., default_for: _Optional[_Iterable[_Union[_activity_pb2.ActivityType, str]]] = ...) -> None: ...

class GearDefault(_message.Message):
    __slots__ = ("activity_type", "gear_id")
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GEAR_ID_FIELD_NUMBER: _ClassVar[int]
    activity_type: _activity_pb2.ActivityType
    gear_id: str
    def __init__(self, activity_type: _Optional[_Union[_activity_pb2.ActivityType, str]] = ..., gear_id: _Optional[str] = ...) -> None: ...

class ListGearRequest(_message.Message):
    __slots__ = ("include_retired",)
    INCLUDE_RETIRED_FIELD_NUMBER: _ClassVar[int]
    include_retired: bool
    def __init__(self, include_retired: _Optional[bool] = ...) -> None: ...

class ListGearResponse(_message.Message):
    __slots__ = ("gear",)
    GEAR_FIELD_NUMBER: _ClassVar[int]
    gear: _containers.RepeatedCompositeFieldContainer[Gear]
    def __init__(self, gear: _Optional[_Iterable[_Union[Gear, _Mapping]]] = ...) -> None: ...

class GetGearRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetGearResponse(_message.Message):
    __slots__ = ("gear",)
    GEAR_FIELD_NUMBER: _ClassVar[int]
    gear: Gear
    def __init__(self, gear: _Optional[_Union[Gear, _Mapping]] = ...) -> None: ...

class CreateGearRequest(_message.Message):
    __slots__ = ("kind", "name", "brand", "model", "notes", "purchase_date")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_DATE_FIELD_NUMBER: _ClassVar[int]
    kind: GearKind
    name: str
    brand: str
    model: str
    notes: str
    purchase_date: str
    def __init__(self, kind: _Optional[_Union[GearKind, str]] = ..., name: _Optional[str] = ..., brand: _Optional[str] = ..., model: _Optional[str] = ..., notes: _Optional[str] = ..., purchase_date: _Optional[str] = ...) -> None: ...

class CreateGearResponse(_message.Message):
    __slots__ = ("gear",)
    GEAR_FIELD_NUMBER: _ClassVar[int]
    gear: Gear
    def __init__(self, gear: _Optional[_Union[Gear, _Mapping]] = ...) -> None: ...

class UpdateGearRequest(_message.Message):
    __slots__ = ("id", "field_mask", "name", "brand", "model", "notes", "purchase_date", "kind", "retired")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_DATE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    RETIRED_FIELD_NUMBER: _ClassVar[int]
    id: str
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    name: str
    brand: str
    model: str
    notes: str
    purchase_date: str
    kind: GearKind
    retired: bool
    def __init__(self, id: _Optional[str] = ..., field_mask: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., brand: _Optional[str] = ..., model: _Optional[str] = ..., notes: _Optional[str] = ..., purchase_date: _Optional[str] = ..., kind: _Optional[_Union[GearKind, str]] = ..., retired: _Optional[bool] = ...) -> None: ...

class UpdateGearResponse(_message.Message):
    __slots__ = ("gear",)
    GEAR_FIELD_NUMBER: _ClassVar[int]
    gear: Gear
    def __init__(self, gear: _Optional[_Union[Gear, _Mapping]] = ...) -> None: ...

class DeleteGearRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteGearResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MergeGearRequest(_message.Message):
    __slots__ = ("from_id", "to_id")
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TO_ID_FIELD_NUMBER: _ClassVar[int]
    from_id: str
    to_id: str
    def __init__(self, from_id: _Optional[str] = ..., to_id: _Optional[str] = ...) -> None: ...

class MergeGearResponse(_message.Message):
    __slots__ = ("gear",)
    GEAR_FIELD_NUMBER: _ClassVar[int]
    gear: Gear
    def __init__(self, gear: _Optional[_Union[Gear, _Mapping]] = ...) -> None: ...

class SetGearDefaultRequest(_message.Message):
    __slots__ = ("activity_type", "gear_id")
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GEAR_ID_FIELD_NUMBER: _ClassVar[int]
    activity_type: _activity_pb2.ActivityType
    gear_id: str
    def __init__(self, activity_type: _Optional[_Union[_activity_pb2.ActivityType, str]] = ..., gear_id: _Optional[str] = ...) -> None: ...

class SetGearDefaultResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearGearDefaultRequest(_message.Message):
    __slots__ = ("activity_type",)
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    activity_type: _activity_pb2.ActivityType
    def __init__(self, activity_type: _Optional[_Union[_activity_pb2.ActivityType, str]] = ...) -> None: ...

class ClearGearDefaultResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGearDefaultsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGearDefaultsResponse(_message.Message):
    __slots__ = ("defaults",)
    DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    defaults: _containers.RepeatedCompositeFieldContainer[GearDefault]
    def __init__(self, defaults: _Optional[_Iterable[_Union[GearDefault, _Mapping]]] = ...) -> None: ...

class LinkGearRefRequest(_message.Message):
    __slots__ = ("gear_id", "provider", "external_account_id", "external_id")
    GEAR_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    gear_id: str
    provider: str
    external_account_id: str
    external_id: str
    def __init__(self, gear_id: _Optional[str] = ..., provider: _Optional[str] = ..., external_account_id: _Optional[str] = ..., external_id: _Optional[str] = ...) -> None: ...

class LinkGearRefResponse(_message.Message):
    __slots__ = ("gear",)
    GEAR_FIELD_NUMBER: _ClassVar[int]
    gear: Gear
    def __init__(self, gear: _Optional[_Union[Gear, _Mapping]] = ...) -> None: ...

class ListPendingGearRefsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPendingGearRefsResponse(_message.Message):
    __slots__ = ("refs",)
    REFS_FIELD_NUMBER: _ClassVar[int]
    refs: _containers.RepeatedCompositeFieldContainer[GearExternalRef]
    def __init__(self, refs: _Optional[_Iterable[_Union[GearExternalRef, _Mapping]]] = ...) -> None: ...

class CreateGearFromRefRequest(_message.Message):
    __slots__ = ("provider", "external_account_id", "external_id")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    provider: str
    external_account_id: str
    external_id: str
    def __init__(self, provider: _Optional[str] = ..., external_account_id: _Optional[str] = ..., external_id: _Optional[str] = ...) -> None: ...

class CreateGearFromRefResponse(_message.Message):
    __slots__ = ("gear",)
    GEAR_FIELD_NUMBER: _ClassVar[int]
    gear: Gear
    def __init__(self, gear: _Optional[_Union[Gear, _Mapping]] = ...) -> None: ...
