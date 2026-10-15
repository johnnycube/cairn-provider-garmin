import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cairn.v1 import activity_pb2 as _activity_pb2
from cairn.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_SORT_UNSPECIFIED: _ClassVar[MetricSort]
    METRIC_SORT_TS_DESC: _ClassVar[MetricSort]
    METRIC_SORT_TS_ASC: _ClassVar[MetricSort]

class MetricBucket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_BUCKET_UNSPECIFIED: _ClassVar[MetricBucket]
    METRIC_BUCKET_HOUR: _ClassVar[MetricBucket]
    METRIC_BUCKET_DAY: _ClassVar[MetricBucket]
    METRIC_BUCKET_WEEK: _ClassVar[MetricBucket]
    METRIC_BUCKET_MONTH: _ClassVar[MetricBucket]

class MetricAggregation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_AGGREGATION_UNSPECIFIED: _ClassVar[MetricAggregation]
    METRIC_AGGREGATION_AVG: _ClassVar[MetricAggregation]
    METRIC_AGGREGATION_MIN: _ClassVar[MetricAggregation]
    METRIC_AGGREGATION_MAX: _ClassVar[MetricAggregation]
    METRIC_AGGREGATION_SUM: _ClassVar[MetricAggregation]
    METRIC_AGGREGATION_LAST: _ClassVar[MetricAggregation]
    METRIC_AGGREGATION_FIRST: _ClassVar[MetricAggregation]
    METRIC_AGGREGATION_COUNT: _ClassVar[MetricAggregation]

class BiologicalSex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BIOLOGICAL_SEX_UNSPECIFIED: _ClassVar[BiologicalSex]
    BIOLOGICAL_SEX_FEMALE: _ClassVar[BiologicalSex]
    BIOLOGICAL_SEX_MALE: _ClassVar[BiologicalSex]
    BIOLOGICAL_SEX_OTHER: _ClassVar[BiologicalSex]

class TSSPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TSS_PREFERENCE_UNSPECIFIED: _ClassVar[TSSPreference]
    TSS_PREFERENCE_AUTO: _ClassVar[TSSPreference]
    TSS_PREFERENCE_POWER: _ClassVar[TSSPreference]
    TSS_PREFERENCE_PACE: _ClassVar[TSSPreference]
    TSS_PREFERENCE_HEART_RATE: _ClassVar[TSSPreference]

class SettingsSection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SETTINGS_SECTION_UNSPECIFIED: _ClassVar[SettingsSection]
    SETTINGS_SECTION_PROFILE: _ClassVar[SettingsSection]
    SETTINGS_SECTION_THRESHOLDS: _ClassVar[SettingsSection]
    SETTINGS_SECTION_MERGE_POLICIES: _ClassVar[SettingsSection]
    SETTINGS_SECTION_AUTO_REIMPORT: _ClassVar[SettingsSection]
    SETTINGS_SECTION_POLLING: _ClassVar[SettingsSection]
    SETTINGS_SECTION_PRIVACY: _ClassVar[SettingsSection]
    SETTINGS_SECTION_TSS_PREFERENCES: _ClassVar[SettingsSection]
    SETTINGS_SECTION_BEST_EFFORTS: _ClassVar[SettingsSection]
METRIC_SORT_UNSPECIFIED: MetricSort
METRIC_SORT_TS_DESC: MetricSort
METRIC_SORT_TS_ASC: MetricSort
METRIC_BUCKET_UNSPECIFIED: MetricBucket
METRIC_BUCKET_HOUR: MetricBucket
METRIC_BUCKET_DAY: MetricBucket
METRIC_BUCKET_WEEK: MetricBucket
METRIC_BUCKET_MONTH: MetricBucket
METRIC_AGGREGATION_UNSPECIFIED: MetricAggregation
METRIC_AGGREGATION_AVG: MetricAggregation
METRIC_AGGREGATION_MIN: MetricAggregation
METRIC_AGGREGATION_MAX: MetricAggregation
METRIC_AGGREGATION_SUM: MetricAggregation
METRIC_AGGREGATION_LAST: MetricAggregation
METRIC_AGGREGATION_FIRST: MetricAggregation
METRIC_AGGREGATION_COUNT: MetricAggregation
BIOLOGICAL_SEX_UNSPECIFIED: BiologicalSex
BIOLOGICAL_SEX_FEMALE: BiologicalSex
BIOLOGICAL_SEX_MALE: BiologicalSex
BIOLOGICAL_SEX_OTHER: BiologicalSex
TSS_PREFERENCE_UNSPECIFIED: TSSPreference
TSS_PREFERENCE_AUTO: TSSPreference
TSS_PREFERENCE_POWER: TSSPreference
TSS_PREFERENCE_PACE: TSSPreference
TSS_PREFERENCE_HEART_RATE: TSSPreference
SETTINGS_SECTION_UNSPECIFIED: SettingsSection
SETTINGS_SECTION_PROFILE: SettingsSection
SETTINGS_SECTION_THRESHOLDS: SettingsSection
SETTINGS_SECTION_MERGE_POLICIES: SettingsSection
SETTINGS_SECTION_AUTO_REIMPORT: SettingsSection
SETTINGS_SECTION_POLLING: SettingsSection
SETTINGS_SECTION_PRIVACY: SettingsSection
SETTINGS_SECTION_TSS_PREFERENCES: SettingsSection
SETTINGS_SECTION_BEST_EFFORTS: SettingsSection

class Metric(_message.Message):
    __slots__ = ("id", "user_id", "key", "ts", "period_seconds", "value_numeric", "value_struct", "provider", "external_account_id", "external_id", "source_worker_name", "source_worker_version", "activity_id", "tags", "notes", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    VALUE_NUMERIC_FIELD_NUMBER: _ClassVar[int]
    VALUE_STRUCT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_WORKER_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    key: str
    ts: _timestamp_pb2.Timestamp
    period_seconds: int
    value_numeric: float
    value_struct: _struct_pb2.Struct
    provider: str
    external_account_id: str
    external_id: str
    source_worker_name: str
    source_worker_version: str
    activity_id: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    notes: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., key: _Optional[str] = ..., ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., period_seconds: _Optional[int] = ..., value_numeric: _Optional[float] = ..., value_struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider: _Optional[str] = ..., external_account_id: _Optional[str] = ..., external_id: _Optional[str] = ..., source_worker_name: _Optional[str] = ..., source_worker_version: _Optional[str] = ..., activity_id: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., notes: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListMetricsRequest(_message.Message):
    __slots__ = ("keys", "time_range", "providers", "external_account_id", "activity_id", "page", "sort")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    time_range: _common_pb2.TimeRange
    providers: _containers.RepeatedScalarFieldContainer[str]
    external_account_id: str
    activity_id: str
    page: _common_pb2.PageRequest
    sort: MetricSort
    def __init__(self, keys: _Optional[_Iterable[str]] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., providers: _Optional[_Iterable[str]] = ..., external_account_id: _Optional[str] = ..., activity_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ..., sort: _Optional[_Union[MetricSort, str]] = ...) -> None: ...

class ListMetricsResponse(_message.Message):
    __slots__ = ("metrics", "page")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[Metric]
    page: _common_pb2.PageResponse
    def __init__(self, metrics: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class GetLatestMetricsRequest(_message.Message):
    __slots__ = ("keys", "as_of")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    AS_OF_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    as_of: _timestamp_pb2.Timestamp
    def __init__(self, keys: _Optional[_Iterable[str]] = ..., as_of: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetLatestMetricsResponse(_message.Message):
    __slots__ = ("metrics",)
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Metric
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Metric, _Mapping]] = ...) -> None: ...
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.MessageMap[str, Metric]
    def __init__(self, metrics: _Optional[_Mapping[str, Metric]] = ...) -> None: ...

class QueryMetricSeriesRequest(_message.Message):
    __slots__ = ("key", "time_range", "bucket", "aggregation", "max_points", "providers")
    KEY_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    MAX_POINTS_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    key: str
    time_range: _common_pb2.TimeRange
    bucket: MetricBucket
    aggregation: MetricAggregation
    max_points: int
    providers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., bucket: _Optional[_Union[MetricBucket, str]] = ..., aggregation: _Optional[_Union[MetricAggregation, str]] = ..., max_points: _Optional[int] = ..., providers: _Optional[_Iterable[str]] = ...) -> None: ...

class MetricSeriesPoint(_message.Message):
    __slots__ = ("ts", "value", "sample_count")
    TS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ts: _timestamp_pb2.Timestamp
    value: float
    sample_count: int
    def __init__(self, ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ..., sample_count: _Optional[int] = ...) -> None: ...

class QueryMetricSeriesResponse(_message.Message):
    __slots__ = ("key", "bucket", "aggregation", "points")
    KEY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    key: str
    bucket: MetricBucket
    aggregation: MetricAggregation
    points: _containers.RepeatedCompositeFieldContainer[MetricSeriesPoint]
    def __init__(self, key: _Optional[str] = ..., bucket: _Optional[_Union[MetricBucket, str]] = ..., aggregation: _Optional[_Union[MetricAggregation, str]] = ..., points: _Optional[_Iterable[_Union[MetricSeriesPoint, _Mapping]]] = ...) -> None: ...

class UpsertMetricRequest(_message.Message):
    __slots__ = ("id", "key", "ts", "period_seconds", "value_numeric", "value_struct", "provider", "tags", "notes", "dedup_by_natural_key")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    VALUE_NUMERIC_FIELD_NUMBER: _ClassVar[int]
    VALUE_STRUCT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    DEDUP_BY_NATURAL_KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    ts: _timestamp_pb2.Timestamp
    period_seconds: int
    value_numeric: float
    value_struct: _struct_pb2.Struct
    provider: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    notes: str
    dedup_by_natural_key: bool
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., period_seconds: _Optional[int] = ..., value_numeric: _Optional[float] = ..., value_struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., notes: _Optional[str] = ..., dedup_by_natural_key: _Optional[bool] = ...) -> None: ...

class UpsertMetricResponse(_message.Message):
    __slots__ = ("metric",)
    METRIC_FIELD_NUMBER: _ClassVar[int]
    metric: Metric
    def __init__(self, metric: _Optional[_Union[Metric, _Mapping]] = ...) -> None: ...

class DeleteMetricRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteMetricResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkUpsertMetricsRequest(_message.Message):
    __slots__ = ("metrics", "continue_on_error")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[UpsertMetricRequest]
    continue_on_error: bool
    def __init__(self, metrics: _Optional[_Iterable[_Union[UpsertMetricRequest, _Mapping]]] = ..., continue_on_error: _Optional[bool] = ...) -> None: ...

class BulkUpsertMetricsResponse(_message.Message):
    __slots__ = ("created", "updated", "skipped", "errors")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    created: int
    updated: int
    skipped: int
    errors: _containers.RepeatedCompositeFieldContainer[BulkUpsertError]
    def __init__(self, created: _Optional[int] = ..., updated: _Optional[int] = ..., skipped: _Optional[int] = ..., errors: _Optional[_Iterable[_Union[BulkUpsertError, _Mapping]]] = ...) -> None: ...

class BulkUpsertError(_message.Message):
    __slots__ = ("row_index", "code", "message")
    ROW_INDEX_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    row_index: int
    code: str
    message: str
    def __init__(self, row_index: _Optional[int] = ..., code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetUserContextRequest(_message.Message):
    __slots__ = ("as_of",)
    AS_OF_FIELD_NUMBER: _ClassVar[int]
    as_of: _timestamp_pb2.Timestamp
    def __init__(self, as_of: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetUserContextResponse(_message.Message):
    __slots__ = ("settings", "latest_metrics")
    class LatestMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Metric
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Metric, _Mapping]] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LATEST_METRICS_FIELD_NUMBER: _ClassVar[int]
    settings: UserSettings
    latest_metrics: _containers.MessageMap[str, Metric]
    def __init__(self, settings: _Optional[_Union[UserSettings, _Mapping]] = ..., latest_metrics: _Optional[_Mapping[str, Metric]] = ...) -> None: ...

class UserSettings(_message.Message):
    __slots__ = ("user_id", "height_cm", "birthdate", "biological_sex", "max_hr_estimate_bpm", "ftp_cycling_override_w", "lthr_cycling_override_bpm", "lthr_running_override_bpm", "threshold_pace_running_override_s_per_km", "css_swimming_override_s_per_100m", "merge_policy_by_activity_type", "metric_priority_by_key", "auto_reimport_by_provider", "poll_schedule_override_by_provider", "default_activity_privacy", "tss_preference_by_activity_type", "best_effort_windows_by_activity_type", "updated_at")
    class MergePolicyByActivityTypeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ActivityTypeMergePolicy
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ActivityTypeMergePolicy, _Mapping]] = ...) -> None: ...
    class MetricPriorityByKeyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ProviderPriorityList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ProviderPriorityList, _Mapping]] = ...) -> None: ...
    class AutoReimportByProviderEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AutoReimportPolicy
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AutoReimportPolicy, _Mapping]] = ...) -> None: ...
    class PollScheduleOverrideByProviderEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TssPreferenceByActivityTypeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TSSPreference
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TSSPreference, str]] = ...) -> None: ...
    class BestEffortWindowsByActivityTypeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BestEffortWindowSet
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BestEffortWindowSet, _Mapping]] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_CM_FIELD_NUMBER: _ClassVar[int]
    BIRTHDATE_FIELD_NUMBER: _ClassVar[int]
    BIOLOGICAL_SEX_FIELD_NUMBER: _ClassVar[int]
    MAX_HR_ESTIMATE_BPM_FIELD_NUMBER: _ClassVar[int]
    FTP_CYCLING_OVERRIDE_W_FIELD_NUMBER: _ClassVar[int]
    LTHR_CYCLING_OVERRIDE_BPM_FIELD_NUMBER: _ClassVar[int]
    LTHR_RUNNING_OVERRIDE_BPM_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_PACE_RUNNING_OVERRIDE_S_PER_KM_FIELD_NUMBER: _ClassVar[int]
    CSS_SWIMMING_OVERRIDE_S_PER_100M_FIELD_NUMBER: _ClassVar[int]
    MERGE_POLICY_BY_ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    METRIC_PRIORITY_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    AUTO_REIMPORT_BY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    POLL_SCHEDULE_OVERRIDE_BY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ACTIVITY_PRIVACY_FIELD_NUMBER: _ClassVar[int]
    TSS_PREFERENCE_BY_ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    BEST_EFFORT_WINDOWS_BY_ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    height_cm: float
    birthdate: _timestamp_pb2.Timestamp
    biological_sex: BiologicalSex
    max_hr_estimate_bpm: int
    ftp_cycling_override_w: int
    lthr_cycling_override_bpm: int
    lthr_running_override_bpm: int
    threshold_pace_running_override_s_per_km: int
    css_swimming_override_s_per_100m: int
    merge_policy_by_activity_type: _containers.MessageMap[str, ActivityTypeMergePolicy]
    metric_priority_by_key: _containers.MessageMap[str, ProviderPriorityList]
    auto_reimport_by_provider: _containers.MessageMap[str, AutoReimportPolicy]
    poll_schedule_override_by_provider: _containers.ScalarMap[str, str]
    default_activity_privacy: _activity_pb2.Privacy
    tss_preference_by_activity_type: _containers.ScalarMap[str, TSSPreference]
    best_effort_windows_by_activity_type: _containers.MessageMap[str, BestEffortWindowSet]
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., height_cm: _Optional[float] = ..., birthdate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., biological_sex: _Optional[_Union[BiologicalSex, str]] = ..., max_hr_estimate_bpm: _Optional[int] = ..., ftp_cycling_override_w: _Optional[int] = ..., lthr_cycling_override_bpm: _Optional[int] = ..., lthr_running_override_bpm: _Optional[int] = ..., threshold_pace_running_override_s_per_km: _Optional[int] = ..., css_swimming_override_s_per_100m: _Optional[int] = ..., merge_policy_by_activity_type: _Optional[_Mapping[str, ActivityTypeMergePolicy]] = ..., metric_priority_by_key: _Optional[_Mapping[str, ProviderPriorityList]] = ..., auto_reimport_by_provider: _Optional[_Mapping[str, AutoReimportPolicy]] = ..., poll_schedule_override_by_provider: _Optional[_Mapping[str, str]] = ..., default_activity_privacy: _Optional[_Union[_activity_pb2.Privacy, str]] = ..., tss_preference_by_activity_type: _Optional[_Mapping[str, TSSPreference]] = ..., best_effort_windows_by_activity_type: _Optional[_Mapping[str, BestEffortWindowSet]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ActivityTypeMergePolicy(_message.Message):
    __slots__ = ("default_providers", "by_field_group")
    class ByFieldGroupEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ProviderPriorityList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ProviderPriorityList, _Mapping]] = ...) -> None: ...
    DEFAULT_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_GROUP_FIELD_NUMBER: _ClassVar[int]
    default_providers: _containers.RepeatedScalarFieldContainer[str]
    by_field_group: _containers.MessageMap[str, ProviderPriorityList]
    def __init__(self, default_providers: _Optional[_Iterable[str]] = ..., by_field_group: _Optional[_Mapping[str, ProviderPriorityList]] = ...) -> None: ...

class ProviderPriorityList(_message.Message):
    __slots__ = ("providers",)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, providers: _Optional[_Iterable[str]] = ...) -> None: ...

class AutoReimportPolicy(_message.Message):
    __slots__ = ("on_patch", "on_minor", "on_major", "on_manifest_change", "max_per_hour")
    ON_PATCH_FIELD_NUMBER: _ClassVar[int]
    ON_MINOR_FIELD_NUMBER: _ClassVar[int]
    ON_MAJOR_FIELD_NUMBER: _ClassVar[int]
    ON_MANIFEST_CHANGE_FIELD_NUMBER: _ClassVar[int]
    MAX_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    on_patch: bool
    on_minor: bool
    on_major: bool
    on_manifest_change: bool
    max_per_hour: int
    def __init__(self, on_patch: _Optional[bool] = ..., on_minor: _Optional[bool] = ..., on_major: _Optional[bool] = ..., on_manifest_change: _Optional[bool] = ..., max_per_hour: _Optional[int] = ...) -> None: ...

class BestEffortWindowSet(_message.Message):
    __slots__ = ("windows",)
    class Window(_message.Message):
        __slots__ = ("metric", "window_kind", "window_value", "label")
        METRIC_FIELD_NUMBER: _ClassVar[int]
        WINDOW_KIND_FIELD_NUMBER: _ClassVar[int]
        WINDOW_VALUE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        metric: _activity_pb2.BestEffortMetric
        window_kind: _activity_pb2.BestEffortWindowKind
        window_value: int
        label: str
        def __init__(self, metric: _Optional[_Union[_activity_pb2.BestEffortMetric, str]] = ..., window_kind: _Optional[_Union[_activity_pb2.BestEffortWindowKind, str]] = ..., window_value: _Optional[int] = ..., label: _Optional[str] = ...) -> None: ...
    WINDOWS_FIELD_NUMBER: _ClassVar[int]
    windows: _containers.RepeatedCompositeFieldContainer[BestEffortWindowSet.Window]
    def __init__(self, windows: _Optional[_Iterable[_Union[BestEffortWindowSet.Window, _Mapping]]] = ...) -> None: ...

class GetSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: UserSettings
    def __init__(self, settings: _Optional[_Union[UserSettings, _Mapping]] = ...) -> None: ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ("field_mask", "settings")
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    settings: UserSettings
    def __init__(self, field_mask: _Optional[_Iterable[str]] = ..., settings: _Optional[_Union[UserSettings, _Mapping]] = ...) -> None: ...

class UpdateSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: UserSettings
    def __init__(self, settings: _Optional[_Union[UserSettings, _Mapping]] = ...) -> None: ...

class ResetSettingsSectionRequest(_message.Message):
    __slots__ = ("section",)
    SECTION_FIELD_NUMBER: _ClassVar[int]
    section: SettingsSection
    def __init__(self, section: _Optional[_Union[SettingsSection, str]] = ...) -> None: ...

class ResetSettingsSectionResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: UserSettings
    def __init__(self, settings: _Optional[_Union[UserSettings, _Mapping]] = ...) -> None: ...
