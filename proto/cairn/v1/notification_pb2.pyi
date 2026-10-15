import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cairn.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_SEVERITY_UNSPECIFIED: _ClassVar[NotificationSeverity]
    NOTIFICATION_SEVERITY_INFO: _ClassVar[NotificationSeverity]
    NOTIFICATION_SEVERITY_WARN: _ClassVar[NotificationSeverity]
    NOTIFICATION_SEVERITY_ERROR: _ClassVar[NotificationSeverity]

class NotificationEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_EVENT_TYPE_UNSPECIFIED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SECURITY_LOGIN_NEW_DEVICE: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SECURITY_PASSWORD_CHANGED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SECURITY_PASSKEY_ADDED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SECURITY_PASSKEY_REMOVED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SECURITY_OIDC_IDENTITY_LINKED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SECURITY_OIDC_IDENTITY_UNLINKED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SECURITY_PAT_CREATED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SECURITY_PAT_REVOKED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_AUTH_EXPIRED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_AUTH_INVALID: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_DISABLED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_NEEDS_MIGRATION: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_ADDED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_REMOVED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYNC_RATE_LIMITED_SUSTAINED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYNC_WORKER_OFFLINE_FOR_ACCOUNT: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYNC_BULK_IMPORT_COMPLETED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYNC_REIMPORT_FAILED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYNC_AUTO_REIMPORT_COMPLETED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYNC_UPLOAD_PROCESSED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYNC_UPLOAD_FAILED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACHIEVEMENT_NEW_PERSONAL_RECORD: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACHIEVEMENT_SEGMENT_PR: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACHIEVEMENT_SEGMENT_KOM: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_ACHIEVEMENT_MILESTONE_REACHED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYSTEM_WORKER_VERSION_AVAILABLE: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYSTEM_BREAKING_CHANGE_MIGRATION_NEEDED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYSTEM_INSTANCE_UPDATE_AVAILABLE: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_SYSTEM_WORKER_CONFLICT_DETECTED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_REPORT_WEEKLY_SUMMARY: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_REPORT_MONTHLY_SUMMARY: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TYPE_REPORT_YEAR_IN_REVIEW: _ClassVar[NotificationEventType]

class NotificationChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_CHANNEL_UNSPECIFIED: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_IN_APP: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_EMAIL: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_WEBHOOK: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_PUSH: _ClassVar[NotificationChannel]

class DeliveryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DELIVERY_STATUS_UNSPECIFIED: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_QUEUED: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_SENT: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_FAILED_RETRYABLE: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_FAILED_PERMANENT: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_SUPPRESSED_QUIET_HOURS: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_SUPPRESSED_PREFERENCE: _ClassVar[DeliveryStatus]
NOTIFICATION_SEVERITY_UNSPECIFIED: NotificationSeverity
NOTIFICATION_SEVERITY_INFO: NotificationSeverity
NOTIFICATION_SEVERITY_WARN: NotificationSeverity
NOTIFICATION_SEVERITY_ERROR: NotificationSeverity
NOTIFICATION_EVENT_TYPE_UNSPECIFIED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SECURITY_LOGIN_NEW_DEVICE: NotificationEventType
NOTIFICATION_EVENT_TYPE_SECURITY_PASSWORD_CHANGED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SECURITY_PASSKEY_ADDED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SECURITY_PASSKEY_REMOVED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SECURITY_OIDC_IDENTITY_LINKED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SECURITY_OIDC_IDENTITY_UNLINKED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SECURITY_PAT_CREATED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SECURITY_PAT_REVOKED: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_AUTH_EXPIRED: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_AUTH_INVALID: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_DISABLED: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_NEEDS_MIGRATION: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_ADDED: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACCOUNT_EXTERNAL_REMOVED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYNC_RATE_LIMITED_SUSTAINED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYNC_WORKER_OFFLINE_FOR_ACCOUNT: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYNC_BULK_IMPORT_COMPLETED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYNC_REIMPORT_FAILED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYNC_AUTO_REIMPORT_COMPLETED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYNC_UPLOAD_PROCESSED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYNC_UPLOAD_FAILED: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACHIEVEMENT_NEW_PERSONAL_RECORD: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACHIEVEMENT_SEGMENT_PR: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACHIEVEMENT_SEGMENT_KOM: NotificationEventType
NOTIFICATION_EVENT_TYPE_ACHIEVEMENT_MILESTONE_REACHED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYSTEM_WORKER_VERSION_AVAILABLE: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYSTEM_BREAKING_CHANGE_MIGRATION_NEEDED: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYSTEM_INSTANCE_UPDATE_AVAILABLE: NotificationEventType
NOTIFICATION_EVENT_TYPE_SYSTEM_WORKER_CONFLICT_DETECTED: NotificationEventType
NOTIFICATION_EVENT_TYPE_REPORT_WEEKLY_SUMMARY: NotificationEventType
NOTIFICATION_EVENT_TYPE_REPORT_MONTHLY_SUMMARY: NotificationEventType
NOTIFICATION_EVENT_TYPE_REPORT_YEAR_IN_REVIEW: NotificationEventType
NOTIFICATION_CHANNEL_UNSPECIFIED: NotificationChannel
NOTIFICATION_CHANNEL_IN_APP: NotificationChannel
NOTIFICATION_CHANNEL_EMAIL: NotificationChannel
NOTIFICATION_CHANNEL_WEBHOOK: NotificationChannel
NOTIFICATION_CHANNEL_PUSH: NotificationChannel
DELIVERY_STATUS_UNSPECIFIED: DeliveryStatus
DELIVERY_STATUS_QUEUED: DeliveryStatus
DELIVERY_STATUS_SENT: DeliveryStatus
DELIVERY_STATUS_FAILED_RETRYABLE: DeliveryStatus
DELIVERY_STATUS_FAILED_PERMANENT: DeliveryStatus
DELIVERY_STATUS_SUPPRESSED_QUIET_HOURS: DeliveryStatus
DELIVERY_STATUS_SUPPRESSED_PREFERENCE: DeliveryStatus

class NotificationEvent(_message.Message):
    __slots__ = ("id", "user_id", "type", "severity", "title_i18n_key", "body_i18n_key", "i18n_params", "activity_id", "segment_id", "external_account_id", "worker_name", "dedup_key", "coalesce_count", "read", "read_at", "created_at", "updated_at")
    class I18nParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TITLE_I18N_KEY_FIELD_NUMBER: _ClassVar[int]
    BODY_I18N_KEY_FIELD_NUMBER: _ClassVar[int]
    I18N_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    DEDUP_KEY_FIELD_NUMBER: _ClassVar[int]
    COALESCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    type: NotificationEventType
    severity: NotificationSeverity
    title_i18n_key: str
    body_i18n_key: str
    i18n_params: _containers.ScalarMap[str, str]
    activity_id: str
    segment_id: str
    external_account_id: str
    worker_name: str
    dedup_key: str
    coalesce_count: int
    read: bool
    read_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., type: _Optional[_Union[NotificationEventType, str]] = ..., severity: _Optional[_Union[NotificationSeverity, str]] = ..., title_i18n_key: _Optional[str] = ..., body_i18n_key: _Optional[str] = ..., i18n_params: _Optional[_Mapping[str, str]] = ..., activity_id: _Optional[str] = ..., segment_id: _Optional[str] = ..., external_account_id: _Optional[str] = ..., worker_name: _Optional[str] = ..., dedup_key: _Optional[str] = ..., coalesce_count: _Optional[int] = ..., read: _Optional[bool] = ..., read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class NotificationPreference(_message.Message):
    __slots__ = ("user_id", "event_type", "channel", "enabled", "min_severity", "updated_at")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    event_type: NotificationEventType
    channel: NotificationChannel
    enabled: bool
    min_severity: NotificationSeverity
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., event_type: _Optional[_Union[NotificationEventType, str]] = ..., channel: _Optional[_Union[NotificationChannel, str]] = ..., enabled: _Optional[bool] = ..., min_severity: _Optional[_Union[NotificationSeverity, str]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class QuietHours(_message.Message):
    __slots__ = ("enabled", "start_minute", "end_minute", "days_of_week")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    START_MINUTE_FIELD_NUMBER: _ClassVar[int]
    END_MINUTE_FIELD_NUMBER: _ClassVar[int]
    DAYS_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    start_minute: int
    end_minute: int
    days_of_week: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, enabled: _Optional[bool] = ..., start_minute: _Optional[int] = ..., end_minute: _Optional[int] = ..., days_of_week: _Optional[_Iterable[int]] = ...) -> None: ...

class WebhookEndpoint(_message.Message):
    __slots__ = ("id", "user_id", "name", "url", "event_types", "min_severity", "enabled", "last_delivery_at", "last_delivery_status_code", "last_delivery_error", "consecutive_failures", "auto_disabled", "auto_disabled_at", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_DELIVERY_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_DELIVERY_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    LAST_DELIVERY_ERROR_FIELD_NUMBER: _ClassVar[int]
    CONSECUTIVE_FAILURES_FIELD_NUMBER: _ClassVar[int]
    AUTO_DISABLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_DISABLED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    name: str
    url: str
    event_types: _containers.RepeatedScalarFieldContainer[NotificationEventType]
    min_severity: NotificationSeverity
    enabled: bool
    last_delivery_at: _timestamp_pb2.Timestamp
    last_delivery_status_code: int
    last_delivery_error: str
    consecutive_failures: int
    auto_disabled: bool
    auto_disabled_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., name: _Optional[str] = ..., url: _Optional[str] = ..., event_types: _Optional[_Iterable[_Union[NotificationEventType, str]]] = ..., min_severity: _Optional[_Union[NotificationSeverity, str]] = ..., enabled: _Optional[bool] = ..., last_delivery_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_delivery_status_code: _Optional[int] = ..., last_delivery_error: _Optional[str] = ..., consecutive_failures: _Optional[int] = ..., auto_disabled: _Optional[bool] = ..., auto_disabled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class NotificationDelivery(_message.Message):
    __slots__ = ("id", "event_id", "user_id", "channel", "webhook_endpoint_id", "email_address", "status", "http_status_code", "error_message", "attempt", "attempted_at", "next_retry_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HTTP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTED_AT_FIELD_NUMBER: _ClassVar[int]
    NEXT_RETRY_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    event_id: str
    user_id: str
    channel: NotificationChannel
    webhook_endpoint_id: str
    email_address: str
    status: DeliveryStatus
    http_status_code: int
    error_message: str
    attempt: int
    attempted_at: _timestamp_pb2.Timestamp
    next_retry_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., event_id: _Optional[str] = ..., user_id: _Optional[str] = ..., channel: _Optional[_Union[NotificationChannel, str]] = ..., webhook_endpoint_id: _Optional[str] = ..., email_address: _Optional[str] = ..., status: _Optional[_Union[DeliveryStatus, str]] = ..., http_status_code: _Optional[int] = ..., error_message: _Optional[str] = ..., attempt: _Optional[int] = ..., attempted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., next_retry_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StreamNotificationsRequest(_message.Message):
    __slots__ = ("since_event_id", "types", "min_severity")
    SINCE_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    since_event_id: str
    types: _containers.RepeatedScalarFieldContainer[NotificationEventType]
    min_severity: NotificationSeverity
    def __init__(self, since_event_id: _Optional[str] = ..., types: _Optional[_Iterable[_Union[NotificationEventType, str]]] = ..., min_severity: _Optional[_Union[NotificationSeverity, str]] = ...) -> None: ...

class ListNotificationsRequest(_message.Message):
    __slots__ = ("types", "min_severity", "only_unread", "time_range", "page")
    TYPES_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    ONLY_UNREAD_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[NotificationEventType]
    min_severity: NotificationSeverity
    only_unread: bool
    time_range: _common_pb2.TimeRange
    page: _common_pb2.PageRequest
    def __init__(self, types: _Optional[_Iterable[_Union[NotificationEventType, str]]] = ..., min_severity: _Optional[_Union[NotificationSeverity, str]] = ..., only_unread: _Optional[bool] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListNotificationsResponse(_message.Message):
    __slots__ = ("notifications", "page")
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[NotificationEvent]
    page: _common_pb2.PageResponse
    def __init__(self, notifications: _Optional[_Iterable[_Union[NotificationEvent, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class CountUnreadNotificationsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CountUnreadNotificationsResponse(_message.Message):
    __slots__ = ("count", "count_info", "count_warn", "count_error")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    COUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    COUNT_WARN_FIELD_NUMBER: _ClassVar[int]
    COUNT_ERROR_FIELD_NUMBER: _ClassVar[int]
    count: int
    count_info: int
    count_warn: int
    count_error: int
    def __init__(self, count: _Optional[int] = ..., count_info: _Optional[int] = ..., count_warn: _Optional[int] = ..., count_error: _Optional[int] = ...) -> None: ...

class MarkNotificationReadRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class MarkNotificationReadResponse(_message.Message):
    __slots__ = ("notification",)
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    notification: NotificationEvent
    def __init__(self, notification: _Optional[_Union[NotificationEvent, _Mapping]] = ...) -> None: ...

class MarkAllNotificationsReadRequest(_message.Message):
    __slots__ = ("types",)
    TYPES_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[NotificationEventType]
    def __init__(self, types: _Optional[_Iterable[_Union[NotificationEventType, str]]] = ...) -> None: ...

class MarkAllNotificationsReadResponse(_message.Message):
    __slots__ = ("marked_count",)
    MARKED_COUNT_FIELD_NUMBER: _ClassVar[int]
    marked_count: int
    def __init__(self, marked_count: _Optional[int] = ...) -> None: ...

class DeleteNotificationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteNotificationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListNotificationPreferencesRequest(_message.Message):
    __slots__ = ("include_defaults",)
    INCLUDE_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    include_defaults: bool
    def __init__(self, include_defaults: _Optional[bool] = ...) -> None: ...

class ListNotificationPreferencesResponse(_message.Message):
    __slots__ = ("preferences",)
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: _containers.RepeatedCompositeFieldContainer[NotificationPreference]
    def __init__(self, preferences: _Optional[_Iterable[_Union[NotificationPreference, _Mapping]]] = ...) -> None: ...

class UpdateNotificationPreferencesRequest(_message.Message):
    __slots__ = ("preferences",)
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: _containers.RepeatedCompositeFieldContainer[NotificationPreference]
    def __init__(self, preferences: _Optional[_Iterable[_Union[NotificationPreference, _Mapping]]] = ...) -> None: ...

class UpdateNotificationPreferencesResponse(_message.Message):
    __slots__ = ("preferences",)
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: _containers.RepeatedCompositeFieldContainer[NotificationPreference]
    def __init__(self, preferences: _Optional[_Iterable[_Union[NotificationPreference, _Mapping]]] = ...) -> None: ...

class GetQuietHoursRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetQuietHoursResponse(_message.Message):
    __slots__ = ("quiet_hours",)
    QUIET_HOURS_FIELD_NUMBER: _ClassVar[int]
    quiet_hours: QuietHours
    def __init__(self, quiet_hours: _Optional[_Union[QuietHours, _Mapping]] = ...) -> None: ...

class UpdateQuietHoursRequest(_message.Message):
    __slots__ = ("quiet_hours",)
    QUIET_HOURS_FIELD_NUMBER: _ClassVar[int]
    quiet_hours: QuietHours
    def __init__(self, quiet_hours: _Optional[_Union[QuietHours, _Mapping]] = ...) -> None: ...

class UpdateQuietHoursResponse(_message.Message):
    __slots__ = ("quiet_hours",)
    QUIET_HOURS_FIELD_NUMBER: _ClassVar[int]
    quiet_hours: QuietHours
    def __init__(self, quiet_hours: _Optional[_Union[QuietHours, _Mapping]] = ...) -> None: ...

class TestNotificationChannelRequest(_message.Message):
    __slots__ = ("channel", "webhook_endpoint_id")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    channel: NotificationChannel
    webhook_endpoint_id: str
    def __init__(self, channel: _Optional[_Union[NotificationChannel, str]] = ..., webhook_endpoint_id: _Optional[str] = ...) -> None: ...

class TestNotificationChannelResponse(_message.Message):
    __slots__ = ("status", "http_status_code", "error_message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HTTP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: DeliveryStatus
    http_status_code: int
    error_message: str
    def __init__(self, status: _Optional[_Union[DeliveryStatus, str]] = ..., http_status_code: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class ListWebhookEndpointsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListWebhookEndpointsResponse(_message.Message):
    __slots__ = ("endpoints",)
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[WebhookEndpoint]
    def __init__(self, endpoints: _Optional[_Iterable[_Union[WebhookEndpoint, _Mapping]]] = ...) -> None: ...

class CreateWebhookEndpointRequest(_message.Message):
    __slots__ = ("name", "url", "event_types", "min_severity")
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    event_types: _containers.RepeatedScalarFieldContainer[NotificationEventType]
    min_severity: NotificationSeverity
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., event_types: _Optional[_Iterable[_Union[NotificationEventType, str]]] = ..., min_severity: _Optional[_Union[NotificationSeverity, str]] = ...) -> None: ...

class CreateWebhookEndpointResponse(_message.Message):
    __slots__ = ("endpoint", "signing_secret")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    SIGNING_SECRET_FIELD_NUMBER: _ClassVar[int]
    endpoint: WebhookEndpoint
    signing_secret: str
    def __init__(self, endpoint: _Optional[_Union[WebhookEndpoint, _Mapping]] = ..., signing_secret: _Optional[str] = ...) -> None: ...

class UpdateWebhookEndpointRequest(_message.Message):
    __slots__ = ("id", "field_mask", "name", "url", "event_types", "min_severity", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    name: str
    url: str
    event_types: _containers.RepeatedScalarFieldContainer[NotificationEventType]
    min_severity: NotificationSeverity
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., field_mask: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., url: _Optional[str] = ..., event_types: _Optional[_Iterable[_Union[NotificationEventType, str]]] = ..., min_severity: _Optional[_Union[NotificationSeverity, str]] = ..., enabled: _Optional[bool] = ...) -> None: ...

class UpdateWebhookEndpointResponse(_message.Message):
    __slots__ = ("endpoint",)
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: WebhookEndpoint
    def __init__(self, endpoint: _Optional[_Union[WebhookEndpoint, _Mapping]] = ...) -> None: ...

class DeleteWebhookEndpointRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteWebhookEndpointResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RotateWebhookEndpointSecretRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RotateWebhookEndpointSecretResponse(_message.Message):
    __slots__ = ("endpoint", "signing_secret")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    SIGNING_SECRET_FIELD_NUMBER: _ClassVar[int]
    endpoint: WebhookEndpoint
    signing_secret: str
    def __init__(self, endpoint: _Optional[_Union[WebhookEndpoint, _Mapping]] = ..., signing_secret: _Optional[str] = ...) -> None: ...

class ReenableWebhookEndpointRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ReenableWebhookEndpointResponse(_message.Message):
    __slots__ = ("endpoint",)
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: WebhookEndpoint
    def __init__(self, endpoint: _Optional[_Union[WebhookEndpoint, _Mapping]] = ...) -> None: ...

class ListWebhookDeliveriesRequest(_message.Message):
    __slots__ = ("webhook_endpoint_id", "time_range", "statuses", "page")
    WEBHOOK_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    webhook_endpoint_id: str
    time_range: _common_pb2.TimeRange
    statuses: _containers.RepeatedScalarFieldContainer[DeliveryStatus]
    page: _common_pb2.PageRequest
    def __init__(self, webhook_endpoint_id: _Optional[str] = ..., time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., statuses: _Optional[_Iterable[_Union[DeliveryStatus, str]]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListWebhookDeliveriesResponse(_message.Message):
    __slots__ = ("deliveries", "page")
    DELIVERIES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    deliveries: _containers.RepeatedCompositeFieldContainer[NotificationDelivery]
    page: _common_pb2.PageResponse
    def __init__(self, deliveries: _Optional[_Iterable[_Union[NotificationDelivery, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...
