import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cairn.v1 import activity_pb2 as _activity_pb2
from cairn.v1 import common_pb2 as _common_pb2
from cairn.v1 import metrics_pb2 as _metrics_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SegmentScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEGMENT_SCOPE_UNSPECIFIED: _ClassVar[SegmentScope]
    SEGMENT_SCOPE_PRIVATE: _ClassVar[SegmentScope]
    SEGMENT_SCOPE_INSTANCE: _ClassVar[SegmentScope]

class ClimbCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLIMB_CATEGORY_UNSPECIFIED: _ClassVar[ClimbCategory]
    CLIMB_CATEGORY_NONE: _ClassVar[ClimbCategory]
    CLIMB_CATEGORY_FOUR: _ClassVar[ClimbCategory]
    CLIMB_CATEGORY_THREE: _ClassVar[ClimbCategory]
    CLIMB_CATEGORY_TWO: _ClassVar[ClimbCategory]
    CLIMB_CATEGORY_ONE: _ClassVar[ClimbCategory]
    CLIMB_CATEGORY_HORS_CATEGORIE: _ClassVar[ClimbCategory]

class SegmentSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEGMENT_SORT_UNSPECIFIED: _ClassVar[SegmentSort]
    SEGMENT_SORT_NAME_ASC: _ClassVar[SegmentSort]
    SEGMENT_SORT_DISTANCE_DESC: _ClassVar[SegmentSort]
    SEGMENT_SORT_ELEVATION_DESC: _ClassVar[SegmentSort]
    SEGMENT_SORT_EFFORT_COUNT_DESC: _ClassVar[SegmentSort]
    SEGMENT_SORT_CREATED_AT_DESC: _ClassVar[SegmentSort]

class SegmentEffortSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEGMENT_EFFORT_SORT_UNSPECIFIED: _ClassVar[SegmentEffortSort]
    SEGMENT_EFFORT_SORT_ELAPSED_ASC: _ClassVar[SegmentEffortSort]
    SEGMENT_EFFORT_SORT_START_TIME_DESC: _ClassVar[SegmentEffortSort]
SEGMENT_SCOPE_UNSPECIFIED: SegmentScope
SEGMENT_SCOPE_PRIVATE: SegmentScope
SEGMENT_SCOPE_INSTANCE: SegmentScope
CLIMB_CATEGORY_UNSPECIFIED: ClimbCategory
CLIMB_CATEGORY_NONE: ClimbCategory
CLIMB_CATEGORY_FOUR: ClimbCategory
CLIMB_CATEGORY_THREE: ClimbCategory
CLIMB_CATEGORY_TWO: ClimbCategory
CLIMB_CATEGORY_ONE: ClimbCategory
CLIMB_CATEGORY_HORS_CATEGORIE: ClimbCategory
SEGMENT_SORT_UNSPECIFIED: SegmentSort
SEGMENT_SORT_NAME_ASC: SegmentSort
SEGMENT_SORT_DISTANCE_DESC: SegmentSort
SEGMENT_SORT_ELEVATION_DESC: SegmentSort
SEGMENT_SORT_EFFORT_COUNT_DESC: SegmentSort
SEGMENT_SORT_CREATED_AT_DESC: SegmentSort
SEGMENT_EFFORT_SORT_UNSPECIFIED: SegmentEffortSort
SEGMENT_EFFORT_SORT_ELAPSED_ASC: SegmentEffortSort
SEGMENT_EFFORT_SORT_START_TIME_DESC: SegmentEffortSort

class Segment(_message.Message):
    __slots__ = ("id", "source", "external_id", "external_account_id", "owner_user_id", "scope", "name", "description", "activity_type", "polyline", "bounding_box", "distance_m", "elevation_gain_m", "elevation_loss_m", "min_elevation_m", "max_elevation_m", "avg_grade", "max_grade", "climb_category", "match_corridor_m", "match_start_tolerance_m", "match_end_tolerance_m", "bidirectional", "starred", "stats", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_M_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_GAIN_M_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_LOSS_M_FIELD_NUMBER: _ClassVar[int]
    MIN_ELEVATION_M_FIELD_NUMBER: _ClassVar[int]
    MAX_ELEVATION_M_FIELD_NUMBER: _ClassVar[int]
    AVG_GRADE_FIELD_NUMBER: _ClassVar[int]
    MAX_GRADE_FIELD_NUMBER: _ClassVar[int]
    CLIMB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    MATCH_CORRIDOR_M_FIELD_NUMBER: _ClassVar[int]
    MATCH_START_TOLERANCE_M_FIELD_NUMBER: _ClassVar[int]
    MATCH_END_TOLERANCE_M_FIELD_NUMBER: _ClassVar[int]
    BIDIRECTIONAL_FIELD_NUMBER: _ClassVar[int]
    STARRED_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    source: str
    external_id: str
    external_account_id: str
    owner_user_id: str
    scope: SegmentScope
    name: str
    description: str
    activity_type: _activity_pb2.ActivityType
    polyline: _common_pb2.EncodedPolyline
    bounding_box: _common_pb2.BoundingBox
    distance_m: float
    elevation_gain_m: float
    elevation_loss_m: float
    min_elevation_m: float
    max_elevation_m: float
    avg_grade: float
    max_grade: float
    climb_category: ClimbCategory
    match_corridor_m: float
    match_start_tolerance_m: float
    match_end_tolerance_m: float
    bidirectional: bool
    starred: bool
    stats: SegmentStats
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., source: _Optional[str] = ..., external_id: _Optional[str] = ..., external_account_id: _Optional[str] = ..., owner_user_id: _Optional[str] = ..., scope: _Optional[_Union[SegmentScope, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., activity_type: _Optional[_Union[_activity_pb2.ActivityType, str]] = ..., polyline: _Optional[_Union[_common_pb2.EncodedPolyline, _Mapping]] = ..., bounding_box: _Optional[_Union[_common_pb2.BoundingBox, _Mapping]] = ..., distance_m: _Optional[float] = ..., elevation_gain_m: _Optional[float] = ..., elevation_loss_m: _Optional[float] = ..., min_elevation_m: _Optional[float] = ..., max_elevation_m: _Optional[float] = ..., avg_grade: _Optional[float] = ..., max_grade: _Optional[float] = ..., climb_category: _Optional[_Union[ClimbCategory, str]] = ..., match_corridor_m: _Optional[float] = ..., match_start_tolerance_m: _Optional[float] = ..., match_end_tolerance_m: _Optional[float] = ..., bidirectional: _Optional[bool] = ..., starred: _Optional[bool] = ..., stats: _Optional[_Union[SegmentStats, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SegmentStats(_message.Message):
    __slots__ = ("effort_count", "athlete_count", "kom_time", "kom_effort_id", "pr_time", "pr_effort_id")
    EFFORT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ATHLETE_COUNT_FIELD_NUMBER: _ClassVar[int]
    KOM_TIME_FIELD_NUMBER: _ClassVar[int]
    KOM_EFFORT_ID_FIELD_NUMBER: _ClassVar[int]
    PR_TIME_FIELD_NUMBER: _ClassVar[int]
    PR_EFFORT_ID_FIELD_NUMBER: _ClassVar[int]
    effort_count: int
    athlete_count: int
    kom_time: _duration_pb2.Duration
    kom_effort_id: str
    pr_time: _duration_pb2.Duration
    pr_effort_id: str
    def __init__(self, effort_count: _Optional[int] = ..., athlete_count: _Optional[int] = ..., kom_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., kom_effort_id: _Optional[str] = ..., pr_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., pr_effort_id: _Optional[str] = ...) -> None: ...

class SegmentEffort(_message.Message):
    __slots__ = ("id", "segment_id", "activity_id", "activity_source_id", "user_id", "start_time", "elapsed", "moving", "start_offset", "end_offset", "avg_heart_rate_bpm", "max_heart_rate_bpm", "avg_power_w", "avg_cadence", "avg_speed_mps", "personal_rank", "instance_rank", "is_personal_record", "is_instance_record", "provider_effort_external_id", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_FIELD_NUMBER: _ClassVar[int]
    MOVING_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    AVG_HEART_RATE_BPM_FIELD_NUMBER: _ClassVar[int]
    MAX_HEART_RATE_BPM_FIELD_NUMBER: _ClassVar[int]
    AVG_POWER_W_FIELD_NUMBER: _ClassVar[int]
    AVG_CADENCE_FIELD_NUMBER: _ClassVar[int]
    AVG_SPEED_MPS_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_RANK_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_RANK_FIELD_NUMBER: _ClassVar[int]
    IS_PERSONAL_RECORD_FIELD_NUMBER: _ClassVar[int]
    IS_INSTANCE_RECORD_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EFFORT_EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    segment_id: str
    activity_id: str
    activity_source_id: str
    user_id: str
    start_time: _timestamp_pb2.Timestamp
    elapsed: _duration_pb2.Duration
    moving: _duration_pb2.Duration
    start_offset: int
    end_offset: int
    avg_heart_rate_bpm: int
    max_heart_rate_bpm: int
    avg_power_w: int
    avg_cadence: int
    avg_speed_mps: float
    personal_rank: int
    instance_rank: int
    is_personal_record: bool
    is_instance_record: bool
    provider_effort_external_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., segment_id: _Optional[str] = ..., activity_id: _Optional[str] = ..., activity_source_id: _Optional[str] = ..., user_id: _Optional[str] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., elapsed: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., moving: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ..., avg_heart_rate_bpm: _Optional[int] = ..., max_heart_rate_bpm: _Optional[int] = ..., avg_power_w: _Optional[int] = ..., avg_cadence: _Optional[int] = ..., avg_speed_mps: _Optional[float] = ..., personal_rank: _Optional[int] = ..., instance_rank: _Optional[int] = ..., is_personal_record: _Optional[bool] = ..., is_instance_record: _Optional[bool] = ..., provider_effort_external_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListSegmentsRequest(_message.Message):
    __slots__ = ("sources", "scopes", "activity_types", "only_with_efforts", "only_starred", "query", "sort", "page")
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    ONLY_WITH_EFFORTS_FIELD_NUMBER: _ClassVar[int]
    ONLY_STARRED_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedScalarFieldContainer[str]
    scopes: _containers.RepeatedScalarFieldContainer[SegmentScope]
    activity_types: _containers.RepeatedScalarFieldContainer[_activity_pb2.ActivityType]
    only_with_efforts: bool
    only_starred: bool
    query: str
    sort: SegmentSort
    page: _common_pb2.PageRequest
    def __init__(self, sources: _Optional[_Iterable[str]] = ..., scopes: _Optional[_Iterable[_Union[SegmentScope, str]]] = ..., activity_types: _Optional[_Iterable[_Union[_activity_pb2.ActivityType, str]]] = ..., only_with_efforts: _Optional[bool] = ..., only_starred: _Optional[bool] = ..., query: _Optional[str] = ..., sort: _Optional[_Union[SegmentSort, str]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListSegmentsResponse(_message.Message):
    __slots__ = ("segments", "page")
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[Segment]
    page: _common_pb2.PageResponse
    def __init__(self, segments: _Optional[_Iterable[_Union[Segment, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class GetSegmentRequest(_message.Message):
    __slots__ = ("id", "include_top_efforts")
    ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TOP_EFFORTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    include_top_efforts: bool
    def __init__(self, id: _Optional[str] = ..., include_top_efforts: _Optional[bool] = ...) -> None: ...

class GetSegmentResponse(_message.Message):
    __slots__ = ("segment", "top_efforts")
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    TOP_EFFORTS_FIELD_NUMBER: _ClassVar[int]
    segment: Segment
    top_efforts: _containers.RepeatedCompositeFieldContainer[SegmentEffort]
    def __init__(self, segment: _Optional[_Union[Segment, _Mapping]] = ..., top_efforts: _Optional[_Iterable[_Union[SegmentEffort, _Mapping]]] = ...) -> None: ...

class CreateSegmentRequest(_message.Message):
    __slots__ = ("name", "description", "activity_type", "polyline", "scope", "match_corridor_m", "match_start_tolerance_m", "match_end_tolerance_m", "bidirectional", "backfill_efforts")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_CORRIDOR_M_FIELD_NUMBER: _ClassVar[int]
    MATCH_START_TOLERANCE_M_FIELD_NUMBER: _ClassVar[int]
    MATCH_END_TOLERANCE_M_FIELD_NUMBER: _ClassVar[int]
    BIDIRECTIONAL_FIELD_NUMBER: _ClassVar[int]
    BACKFILL_EFFORTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    activity_type: _activity_pb2.ActivityType
    polyline: _common_pb2.EncodedPolyline
    scope: SegmentScope
    match_corridor_m: float
    match_start_tolerance_m: float
    match_end_tolerance_m: float
    bidirectional: bool
    backfill_efforts: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., activity_type: _Optional[_Union[_activity_pb2.ActivityType, str]] = ..., polyline: _Optional[_Union[_common_pb2.EncodedPolyline, _Mapping]] = ..., scope: _Optional[_Union[SegmentScope, str]] = ..., match_corridor_m: _Optional[float] = ..., match_start_tolerance_m: _Optional[float] = ..., match_end_tolerance_m: _Optional[float] = ..., bidirectional: _Optional[bool] = ..., backfill_efforts: _Optional[bool] = ...) -> None: ...

class CreateSegmentResponse(_message.Message):
    __slots__ = ("segment", "backfill_job_id")
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    BACKFILL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    segment: Segment
    backfill_job_id: str
    def __init__(self, segment: _Optional[_Union[Segment, _Mapping]] = ..., backfill_job_id: _Optional[str] = ...) -> None: ...

class UpdateSegmentRequest(_message.Message):
    __slots__ = ("id", "field_mask", "name", "description", "scope", "match_corridor_m", "match_start_tolerance_m", "match_end_tolerance_m", "bidirectional", "starred", "polyline")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_CORRIDOR_M_FIELD_NUMBER: _ClassVar[int]
    MATCH_START_TOLERANCE_M_FIELD_NUMBER: _ClassVar[int]
    MATCH_END_TOLERANCE_M_FIELD_NUMBER: _ClassVar[int]
    BIDIRECTIONAL_FIELD_NUMBER: _ClassVar[int]
    STARRED_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    id: str
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    name: str
    description: str
    scope: SegmentScope
    match_corridor_m: float
    match_start_tolerance_m: float
    match_end_tolerance_m: float
    bidirectional: bool
    starred: bool
    polyline: _common_pb2.EncodedPolyline
    def __init__(self, id: _Optional[str] = ..., field_mask: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., scope: _Optional[_Union[SegmentScope, str]] = ..., match_corridor_m: _Optional[float] = ..., match_start_tolerance_m: _Optional[float] = ..., match_end_tolerance_m: _Optional[float] = ..., bidirectional: _Optional[bool] = ..., starred: _Optional[bool] = ..., polyline: _Optional[_Union[_common_pb2.EncodedPolyline, _Mapping]] = ...) -> None: ...

class UpdateSegmentResponse(_message.Message):
    __slots__ = ("segment",)
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    segment: Segment
    def __init__(self, segment: _Optional[_Union[Segment, _Mapping]] = ...) -> None: ...

class DeleteSegmentRequest(_message.Message):
    __slots__ = ("id", "keep_efforts")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEEP_EFFORTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    keep_efforts: bool
    def __init__(self, id: _Optional[str] = ..., keep_efforts: _Optional[bool] = ...) -> None: ...

class DeleteSegmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchSegmentsInBoundingBoxRequest(_message.Message):
    __slots__ = ("bbox", "activity_types", "limit", "include_instance_segments")
    BBOX_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INSTANCE_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    bbox: _common_pb2.BoundingBox
    activity_types: _containers.RepeatedScalarFieldContainer[_activity_pb2.ActivityType]
    limit: int
    include_instance_segments: bool
    def __init__(self, bbox: _Optional[_Union[_common_pb2.BoundingBox, _Mapping]] = ..., activity_types: _Optional[_Iterable[_Union[_activity_pb2.ActivityType, str]]] = ..., limit: _Optional[int] = ..., include_instance_segments: _Optional[bool] = ...) -> None: ...

class SearchSegmentsInBoundingBoxResponse(_message.Message):
    __slots__ = ("segments",)
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[Segment]
    def __init__(self, segments: _Optional[_Iterable[_Union[Segment, _Mapping]]] = ...) -> None: ...

class ListSegmentEffortsRequest(_message.Message):
    __slots__ = ("segment_id", "time_range", "user_id", "page", "sort")
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    segment_id: str
    time_range: _common_pb2.TimeRange
    user_id: str
    page: _common_pb2.PageRequest
    sort: SegmentEffortSort
    def __init__(self, segment_id: _Optional[str] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., user_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ..., sort: _Optional[_Union[SegmentEffortSort, str]] = ...) -> None: ...

class ListSegmentEffortsResponse(_message.Message):
    __slots__ = ("efforts", "page")
    EFFORTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    efforts: _containers.RepeatedCompositeFieldContainer[SegmentEffort]
    page: _common_pb2.PageResponse
    def __init__(self, efforts: _Optional[_Iterable[_Union[SegmentEffort, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class ListMySegmentEffortsRequest(_message.Message):
    __slots__ = ("segment_id", "time_range", "page")
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    segment_id: str
    time_range: _common_pb2.TimeRange
    page: _common_pb2.PageRequest
    def __init__(self, segment_id: _Optional[str] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListMySegmentEffortsResponse(_message.Message):
    __slots__ = ("efforts", "page", "personal_record")
    EFFORTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_RECORD_FIELD_NUMBER: _ClassVar[int]
    efforts: _containers.RepeatedCompositeFieldContainer[SegmentEffort]
    page: _common_pb2.PageResponse
    personal_record: SegmentEffort
    def __init__(self, efforts: _Optional[_Iterable[_Union[SegmentEffort, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ..., personal_record: _Optional[_Union[SegmentEffort, _Mapping]] = ...) -> None: ...

class GetSegmentLeaderboardRequest(_message.Message):
    __slots__ = ("segment_id", "time_range", "biological_sex", "page")
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    BIOLOGICAL_SEX_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    segment_id: str
    time_range: _common_pb2.TimeRange
    biological_sex: _metrics_pb2.BiologicalSex
    page: _common_pb2.PageRequest
    def __init__(self, segment_id: _Optional[str] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., biological_sex: _Optional[_Union[_metrics_pb2.BiologicalSex, str]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class LeaderboardEntry(_message.Message):
    __slots__ = ("rank", "user_id", "user_display_name", "user_avatar_url", "elapsed", "start_time", "effort_id", "activity_id")
    RANK_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    EFFORT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    rank: int
    user_id: str
    user_display_name: str
    user_avatar_url: str
    elapsed: _duration_pb2.Duration
    start_time: _timestamp_pb2.Timestamp
    effort_id: str
    activity_id: str
    def __init__(self, rank: _Optional[int] = ..., user_id: _Optional[str] = ..., user_display_name: _Optional[str] = ..., user_avatar_url: _Optional[str] = ..., elapsed: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., effort_id: _Optional[str] = ..., activity_id: _Optional[str] = ...) -> None: ...

class GetSegmentLeaderboardResponse(_message.Message):
    __slots__ = ("entries", "page", "my_rank", "my_entry")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    MY_RANK_FIELD_NUMBER: _ClassVar[int]
    MY_ENTRY_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[LeaderboardEntry]
    page: _common_pb2.PageResponse
    my_rank: int
    my_entry: LeaderboardEntry
    def __init__(self, entries: _Optional[_Iterable[_Union[LeaderboardEntry, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ..., my_rank: _Optional[int] = ..., my_entry: _Optional[_Union[LeaderboardEntry, _Mapping]] = ...) -> None: ...

class RematchActivityRequest(_message.Message):
    __slots__ = ("activity_id", "segment_ids")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    segment_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, activity_id: _Optional[str] = ..., segment_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RematchActivityResponse(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class RematchSegmentRequest(_message.Message):
    __slots__ = ("segment_id", "time_range")
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    segment_id: str
    time_range: _common_pb2.TimeRange
    def __init__(self, segment_id: _Optional[str] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ...) -> None: ...

class RematchSegmentResponse(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...
