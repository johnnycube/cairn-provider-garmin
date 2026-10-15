import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_CLASS_UNSPECIFIED: _ClassVar[ErrorClass]
    ERROR_CLASS_NOT_FOUND: _ClassVar[ErrorClass]
    ERROR_CLASS_PERMISSION_DENIED: _ClassVar[ErrorClass]
    ERROR_CLASS_VALIDATION: _ClassVar[ErrorClass]
    ERROR_CLASS_CONFLICT: _ClassVar[ErrorClass]
    ERROR_CLASS_RATE_LIMITED: _ClassVar[ErrorClass]
    ERROR_CLASS_DEPENDENCY_UNAVAILABLE: _ClassVar[ErrorClass]
    ERROR_CLASS_INTERNAL: _ClassVar[ErrorClass]
ERROR_CLASS_UNSPECIFIED: ErrorClass
ERROR_CLASS_NOT_FOUND: ErrorClass
ERROR_CLASS_PERMISSION_DENIED: ErrorClass
ERROR_CLASS_VALIDATION: ErrorClass
ERROR_CLASS_CONFLICT: ErrorClass
ERROR_CLASS_RATE_LIMITED: ErrorClass
ERROR_CLASS_DEPENDENCY_UNAVAILABLE: ErrorClass
ERROR_CLASS_INTERNAL: ErrorClass

class PageRequest(_message.Message):
    __slots__ = ("cursor", "limit")
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    cursor: str
    limit: int
    def __init__(self, cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class PageResponse(_message.Message):
    __slots__ = ("next_cursor", "total")
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    next_cursor: str
    total: int
    def __init__(self, next_cursor: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class TimeRange(_message.Message):
    __slots__ = ("to",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    def __init__(self, to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class ErrorDetail(_message.Message):
    __slots__ = ("code", "i18n_key", "i18n_params", "retry_after_ms", "field_errors")
    class I18nParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class FieldErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CLASS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    I18N_KEY_FIELD_NUMBER: _ClassVar[int]
    I18N_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RETRY_AFTER_MS_FIELD_NUMBER: _ClassVar[int]
    FIELD_ERRORS_FIELD_NUMBER: _ClassVar[int]
    code: str
    i18n_key: str
    i18n_params: _containers.ScalarMap[str, str]
    retry_after_ms: int
    field_errors: _containers.ScalarMap[str, str]
    def __init__(self, code: _Optional[str] = ..., i18n_key: _Optional[str] = ..., i18n_params: _Optional[_Mapping[str, str]] = ..., retry_after_ms: _Optional[int] = ..., field_errors: _Optional[_Mapping[str, str]] = ..., **kwargs) -> None: ...

class ProviderIdConventionMarker(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GeoPoint(_message.Message):
    __slots__ = ("latitude", "longitude", "elevation_m")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_M_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    elevation_m: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., elevation_m: _Optional[float] = ...) -> None: ...

class EncodedPolyline(_message.Message):
    __slots__ = ("encoded", "precision")
    ENCODED_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    encoded: str
    precision: int
    def __init__(self, encoded: _Optional[str] = ..., precision: _Optional[int] = ...) -> None: ...

class BoundingBox(_message.Message):
    __slots__ = ("min_latitude", "min_longitude", "max_latitude", "max_longitude")
    MIN_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    MIN_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    MAX_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    MAX_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    min_latitude: float
    min_longitude: float
    max_latitude: float
    max_longitude: float
    def __init__(self, min_latitude: _Optional[float] = ..., min_longitude: _Optional[float] = ..., max_latitude: _Optional[float] = ..., max_longitude: _Optional[float] = ...) -> None: ...
