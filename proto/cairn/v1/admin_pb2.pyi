import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cairn.v1 import auth_pb2 as _auth_pb2
from cairn.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmailAdapterKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMAIL_ADAPTER_KIND_UNSPECIFIED: _ClassVar[EmailAdapterKind]
    EMAIL_ADAPTER_KIND_NONE: _ClassVar[EmailAdapterKind]
    EMAIL_ADAPTER_KIND_SMTP: _ClassVar[EmailAdapterKind]
    EMAIL_ADAPTER_KIND_SES: _ClassVar[EmailAdapterKind]
    EMAIL_ADAPTER_KIND_RESEND: _ClassVar[EmailAdapterKind]
    EMAIL_ADAPTER_KIND_MAILGUN: _ClassVar[EmailAdapterKind]

class StorageAdapterKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORAGE_ADAPTER_KIND_UNSPECIFIED: _ClassVar[StorageAdapterKind]
    STORAGE_ADAPTER_KIND_MINIO: _ClassVar[StorageAdapterKind]
    STORAGE_ADAPTER_KIND_AWS_S3: _ClassVar[StorageAdapterKind]
    STORAGE_ADAPTER_KIND_GCS: _ClassVar[StorageAdapterKind]
    STORAGE_ADAPTER_KIND_R2: _ClassVar[StorageAdapterKind]
    STORAGE_ADAPTER_KIND_LOCAL_FS: _ClassVar[StorageAdapterKind]

class UserSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_SORT_UNSPECIFIED: _ClassVar[UserSort]
    USER_SORT_USERNAME_ASC: _ClassVar[UserSort]
    USER_SORT_CREATED_AT_DESC: _ClassVar[UserSort]
    USER_SORT_LAST_LOGIN_DESC: _ClassVar[UserSort]

class AuditSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_SEVERITY_UNSPECIFIED: _ClassVar[AuditSeverity]
    AUDIT_SEVERITY_INFO: _ClassVar[AuditSeverity]
    AUDIT_SEVERITY_WARN: _ClassVar[AuditSeverity]
    AUDIT_SEVERITY_HIGH: _ClassVar[AuditSeverity]

class AdminJobStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADMIN_JOB_STATUS_UNSPECIFIED: _ClassVar[AdminJobStatus]
    ADMIN_JOB_STATUS_QUEUED: _ClassVar[AdminJobStatus]
    ADMIN_JOB_STATUS_RUNNING: _ClassVar[AdminJobStatus]
    ADMIN_JOB_STATUS_COMPLETED: _ClassVar[AdminJobStatus]
    ADMIN_JOB_STATUS_FAILED_RETRYING: _ClassVar[AdminJobStatus]
    ADMIN_JOB_STATUS_FAILED_DEAD_LETTER: _ClassVar[AdminJobStatus]
    ADMIN_JOB_STATUS_CANCELLED: _ClassVar[AdminJobStatus]

class HealthState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTH_STATE_UNSPECIFIED: _ClassVar[HealthState]
    HEALTH_STATE_HEALTHY: _ClassVar[HealthState]
    HEALTH_STATE_DEGRADED: _ClassVar[HealthState]
    HEALTH_STATE_UNHEALTHY: _ClassVar[HealthState]

class AdminEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADMIN_EVENT_TYPE_UNSPECIFIED: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_WORKER_REGISTERED: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_WORKER_DEREGISTERED: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_WORKER_OFFLINE: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_WORKER_DEGRADED: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_PROVIDER_CONFLICT_DETECTED: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_JOB_DEAD_LETTERED: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_USER_CREATED: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_USER_SUSPENDED: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_AUTH_FLOOD_DETECTED: _ClassVar[AdminEventType]
    ADMIN_EVENT_TYPE_SYSTEM_HEALTH_DEGRADED: _ClassVar[AdminEventType]

class MaintenanceOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAINTENANCE_OPERATION_UNSPECIFIED: _ClassVar[MaintenanceOperation]
    MAINTENANCE_OPERATION_REMATCH_ALL_SEGMENTS: _ClassVar[MaintenanceOperation]
    MAINTENANCE_OPERATION_RECOMPUTE_BEST_EFFORTS: _ClassVar[MaintenanceOperation]
    MAINTENANCE_OPERATION_RECOMPUTE_ACTIVITY_MERGES: _ClassVar[MaintenanceOperation]
    MAINTENANCE_OPERATION_RECOMPUTE_TRAINING_LOAD: _ClassVar[MaintenanceOperation]
    MAINTENANCE_OPERATION_PURGE_SOFT_DELETED: _ClassVar[MaintenanceOperation]
    MAINTENANCE_OPERATION_GARBAGE_COLLECT_BLOBS: _ClassVar[MaintenanceOperation]
EMAIL_ADAPTER_KIND_UNSPECIFIED: EmailAdapterKind
EMAIL_ADAPTER_KIND_NONE: EmailAdapterKind
EMAIL_ADAPTER_KIND_SMTP: EmailAdapterKind
EMAIL_ADAPTER_KIND_SES: EmailAdapterKind
EMAIL_ADAPTER_KIND_RESEND: EmailAdapterKind
EMAIL_ADAPTER_KIND_MAILGUN: EmailAdapterKind
STORAGE_ADAPTER_KIND_UNSPECIFIED: StorageAdapterKind
STORAGE_ADAPTER_KIND_MINIO: StorageAdapterKind
STORAGE_ADAPTER_KIND_AWS_S3: StorageAdapterKind
STORAGE_ADAPTER_KIND_GCS: StorageAdapterKind
STORAGE_ADAPTER_KIND_R2: StorageAdapterKind
STORAGE_ADAPTER_KIND_LOCAL_FS: StorageAdapterKind
USER_SORT_UNSPECIFIED: UserSort
USER_SORT_USERNAME_ASC: UserSort
USER_SORT_CREATED_AT_DESC: UserSort
USER_SORT_LAST_LOGIN_DESC: UserSort
AUDIT_SEVERITY_UNSPECIFIED: AuditSeverity
AUDIT_SEVERITY_INFO: AuditSeverity
AUDIT_SEVERITY_WARN: AuditSeverity
AUDIT_SEVERITY_HIGH: AuditSeverity
ADMIN_JOB_STATUS_UNSPECIFIED: AdminJobStatus
ADMIN_JOB_STATUS_QUEUED: AdminJobStatus
ADMIN_JOB_STATUS_RUNNING: AdminJobStatus
ADMIN_JOB_STATUS_COMPLETED: AdminJobStatus
ADMIN_JOB_STATUS_FAILED_RETRYING: AdminJobStatus
ADMIN_JOB_STATUS_FAILED_DEAD_LETTER: AdminJobStatus
ADMIN_JOB_STATUS_CANCELLED: AdminJobStatus
HEALTH_STATE_UNSPECIFIED: HealthState
HEALTH_STATE_HEALTHY: HealthState
HEALTH_STATE_DEGRADED: HealthState
HEALTH_STATE_UNHEALTHY: HealthState
ADMIN_EVENT_TYPE_UNSPECIFIED: AdminEventType
ADMIN_EVENT_TYPE_WORKER_REGISTERED: AdminEventType
ADMIN_EVENT_TYPE_WORKER_DEREGISTERED: AdminEventType
ADMIN_EVENT_TYPE_WORKER_OFFLINE: AdminEventType
ADMIN_EVENT_TYPE_WORKER_DEGRADED: AdminEventType
ADMIN_EVENT_TYPE_PROVIDER_CONFLICT_DETECTED: AdminEventType
ADMIN_EVENT_TYPE_JOB_DEAD_LETTERED: AdminEventType
ADMIN_EVENT_TYPE_USER_CREATED: AdminEventType
ADMIN_EVENT_TYPE_USER_SUSPENDED: AdminEventType
ADMIN_EVENT_TYPE_AUTH_FLOOD_DETECTED: AdminEventType
ADMIN_EVENT_TYPE_SYSTEM_HEALTH_DEGRADED: AdminEventType
MAINTENANCE_OPERATION_UNSPECIFIED: MaintenanceOperation
MAINTENANCE_OPERATION_REMATCH_ALL_SEGMENTS: MaintenanceOperation
MAINTENANCE_OPERATION_RECOMPUTE_BEST_EFFORTS: MaintenanceOperation
MAINTENANCE_OPERATION_RECOMPUTE_ACTIVITY_MERGES: MaintenanceOperation
MAINTENANCE_OPERATION_RECOMPUTE_TRAINING_LOAD: MaintenanceOperation
MAINTENANCE_OPERATION_PURGE_SOFT_DELETED: MaintenanceOperation
MAINTENANCE_OPERATION_GARBAGE_COLLECT_BLOBS: MaintenanceOperation

class OIDCClient(_message.Message):
    __slots__ = ("id", "display_name", "issuer_url", "client_id", "has_client_secret", "scopes", "use_pkce", "audience", "skip_audience_check", "auto_provision", "auto_provision_role")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    USE_PKCE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SKIP_AUDIENCE_CHECK_FIELD_NUMBER: _ClassVar[int]
    AUTO_PROVISION_FIELD_NUMBER: _ClassVar[int]
    AUTO_PROVISION_ROLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    issuer_url: str
    client_id: str
    has_client_secret: bool
    scopes: _containers.RepeatedScalarFieldContainer[str]
    use_pkce: bool
    audience: str
    skip_audience_check: bool
    auto_provision: bool
    auto_provision_role: _auth_pb2.UserRole
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., issuer_url: _Optional[str] = ..., client_id: _Optional[str] = ..., has_client_secret: _Optional[bool] = ..., scopes: _Optional[_Iterable[str]] = ..., use_pkce: _Optional[bool] = ..., audience: _Optional[str] = ..., skip_audience_check: _Optional[bool] = ..., auto_provision: _Optional[bool] = ..., auto_provision_role: _Optional[_Union[_auth_pb2.UserRole, str]] = ...) -> None: ...

class ListOIDCClientsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListOIDCClientsResponse(_message.Message):
    __slots__ = ("clients",)
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[OIDCClient]
    def __init__(self, clients: _Optional[_Iterable[_Union[OIDCClient, _Mapping]]] = ...) -> None: ...

class InstanceSettings(_message.Message):
    __slots__ = ("instance_name", "instance_description", "support_email", "instance_url", "logo_url", "primary_color", "default_locale", "default_timezone", "default_units", "registration_open", "require_invite", "allowed_email_domains", "email_adapter", "email_configured", "email_from_address", "storage_adapter", "storage_configured", "per_user_storage_quota_bytes", "per_user_max_external_accounts", "updated_at")
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_URL_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCALE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_UNITS_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_OPEN_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_INVITE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_EMAIL_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADAPTER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ADAPTER_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    PER_USER_STORAGE_QUOTA_BYTES_FIELD_NUMBER: _ClassVar[int]
    PER_USER_MAX_EXTERNAL_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    instance_description: str
    support_email: str
    instance_url: str
    logo_url: str
    primary_color: str
    default_locale: str
    default_timezone: str
    default_units: _auth_pb2.UnitSystem
    registration_open: bool
    require_invite: bool
    allowed_email_domains: _containers.RepeatedScalarFieldContainer[str]
    email_adapter: EmailAdapterKind
    email_configured: bool
    email_from_address: str
    storage_adapter: StorageAdapterKind
    storage_configured: bool
    per_user_storage_quota_bytes: int
    per_user_max_external_accounts: int
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, instance_name: _Optional[str] = ..., instance_description: _Optional[str] = ..., support_email: _Optional[str] = ..., instance_url: _Optional[str] = ..., logo_url: _Optional[str] = ..., primary_color: _Optional[str] = ..., default_locale: _Optional[str] = ..., default_timezone: _Optional[str] = ..., default_units: _Optional[_Union[_auth_pb2.UnitSystem, str]] = ..., registration_open: _Optional[bool] = ..., require_invite: _Optional[bool] = ..., allowed_email_domains: _Optional[_Iterable[str]] = ..., email_adapter: _Optional[_Union[EmailAdapterKind, str]] = ..., email_configured: _Optional[bool] = ..., email_from_address: _Optional[str] = ..., storage_adapter: _Optional[_Union[StorageAdapterKind, str]] = ..., storage_configured: _Optional[bool] = ..., per_user_storage_quota_bytes: _Optional[int] = ..., per_user_max_external_accounts: _Optional[int] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetInstanceSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInstanceSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: InstanceSettings
    def __init__(self, settings: _Optional[_Union[InstanceSettings, _Mapping]] = ...) -> None: ...

class UpdateInstanceSettingsRequest(_message.Message):
    __slots__ = ("field_mask", "settings")
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    settings: InstanceSettings
    def __init__(self, field_mask: _Optional[_Iterable[str]] = ..., settings: _Optional[_Union[InstanceSettings, _Mapping]] = ...) -> None: ...

class UpdateInstanceSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: InstanceSettings
    def __init__(self, settings: _Optional[_Union[InstanceSettings, _Mapping]] = ...) -> None: ...

class SendTestEmailRequest(_message.Message):
    __slots__ = ("to_address",)
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    to_address: str
    def __init__(self, to_address: _Optional[str] = ...) -> None: ...

class SendTestEmailResponse(_message.Message):
    __slots__ = ("delivered", "error_message", "duration")
    DELIVERED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    delivered: bool
    error_message: str
    duration: _duration_pb2.Duration
    def __init__(self, delivered: _Optional[bool] = ..., error_message: _Optional[str] = ..., duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("query", "roles", "statuses", "page", "sort")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    query: str
    roles: _containers.RepeatedScalarFieldContainer[_auth_pb2.UserRole]
    statuses: _containers.RepeatedScalarFieldContainer[_auth_pb2.UserStatus]
    page: _common_pb2.PageRequest
    sort: UserSort
    def __init__(self, query: _Optional[str] = ..., roles: _Optional[_Iterable[_Union[_auth_pb2.UserRole, str]]] = ..., statuses: _Optional[_Iterable[_Union[_auth_pb2.UserStatus, str]]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ..., sort: _Optional[_Union[UserSort, str]] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "page")
    USERS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[AdminUserSummary]
    page: _common_pb2.PageResponse
    def __init__(self, users: _Optional[_Iterable[_Union[AdminUserSummary, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class AdminUserSummary(_message.Message):
    __slots__ = ("user", "activity_count", "external_account_count", "storage_bytes_used", "last_activity_at")
    USER_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_COUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BYTES_USED_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_AT_FIELD_NUMBER: _ClassVar[int]
    user: _auth_pb2.User
    activity_count: int
    external_account_count: int
    storage_bytes_used: int
    last_activity_at: _timestamp_pb2.Timestamp
    def __init__(self, user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ..., activity_count: _Optional[int] = ..., external_account_count: _Optional[int] = ..., storage_bytes_used: _Optional[int] = ..., last_activity_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user", "identities", "active_session_count", "storage_bytes_used", "activity_count", "external_account_count")
    USER_FIELD_NUMBER: _ClassVar[int]
    IDENTITIES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SESSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BYTES_USED_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_COUNT_FIELD_NUMBER: _ClassVar[int]
    user: _auth_pb2.User
    identities: _containers.RepeatedCompositeFieldContainer[_auth_pb2.LinkedIdentity]
    active_session_count: int
    storage_bytes_used: int
    activity_count: int
    external_account_count: int
    def __init__(self, user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ..., identities: _Optional[_Iterable[_Union[_auth_pb2.LinkedIdentity, _Mapping]]] = ..., active_session_count: _Optional[int] = ..., storage_bytes_used: _Optional[int] = ..., activity_count: _Optional[int] = ..., external_account_count: _Optional[int] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("username", "email", "display_name", "role", "initial_password", "send_welcome_email", "locale", "timezone", "units")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SEND_WELCOME_EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    username: str
    email: str
    display_name: str
    role: _auth_pb2.UserRole
    initial_password: str
    send_welcome_email: bool
    locale: str
    timezone: str
    units: _auth_pb2.UnitSystem
    def __init__(self, username: _Optional[str] = ..., email: _Optional[str] = ..., display_name: _Optional[str] = ..., role: _Optional[_Union[_auth_pb2.UserRole, str]] = ..., initial_password: _Optional[str] = ..., send_welcome_email: _Optional[bool] = ..., locale: _Optional[str] = ..., timezone: _Optional[str] = ..., units: _Optional[_Union[_auth_pb2.UnitSystem, str]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("user", "invite")
    USER_FIELD_NUMBER: _ClassVar[int]
    INVITE_FIELD_NUMBER: _ClassVar[int]
    user: _auth_pb2.User
    invite: Invite
    def __init__(self, user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ..., invite: _Optional[_Union[Invite, _Mapping]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("id", "field_mask", "email", "display_name", "locale", "timezone", "units")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    id: str
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    email: str
    display_name: str
    locale: str
    timezone: str
    units: _auth_pb2.UnitSystem
    def __init__(self, id: _Optional[str] = ..., field_mask: _Optional[_Iterable[str]] = ..., email: _Optional[str] = ..., display_name: _Optional[str] = ..., locale: _Optional[str] = ..., timezone: _Optional[str] = ..., units: _Optional[_Union[_auth_pb2.UnitSystem, str]] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _auth_pb2.User
    def __init__(self, user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ...) -> None: ...

class ChangeUserRoleRequest(_message.Message):
    __slots__ = ("id", "role")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    role: _auth_pb2.UserRole
    def __init__(self, id: _Optional[str] = ..., role: _Optional[_Union[_auth_pb2.UserRole, str]] = ...) -> None: ...

class ChangeUserRoleResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _auth_pb2.User
    def __init__(self, user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ...) -> None: ...

class SetUserStatusRequest(_message.Message):
    __slots__ = ("id", "status", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: _auth_pb2.UserStatus
    reason: str
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[_auth_pb2.UserStatus, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class SetUserStatusResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _auth_pb2.User
    def __init__(self, user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("id", "confirm_username", "hard_delete")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_USERNAME_FIELD_NUMBER: _ClassVar[int]
    HARD_DELETE_FIELD_NUMBER: _ClassVar[int]
    id: str
    confirm_username: str
    hard_delete: bool
    def __init__(self, id: _Optional[str] = ..., confirm_username: _Optional[str] = ..., hard_delete: _Optional[bool] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = ("activities_deleted", "metrics_deleted", "external_accounts_deleted", "storage_bytes_freed")
    ACTIVITIES_DELETED_FIELD_NUMBER: _ClassVar[int]
    METRICS_DELETED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BYTES_FREED_FIELD_NUMBER: _ClassVar[int]
    activities_deleted: int
    metrics_deleted: int
    external_accounts_deleted: int
    storage_bytes_freed: int
    def __init__(self, activities_deleted: _Optional[int] = ..., metrics_deleted: _Optional[int] = ..., external_accounts_deleted: _Optional[int] = ..., storage_bytes_freed: _Optional[int] = ...) -> None: ...

class ResetUserPasswordRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResetUserPasswordResponse(_message.Message):
    __slots__ = ("temporary_password",)
    TEMPORARY_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    temporary_password: str
    def __init__(self, temporary_password: _Optional[str] = ...) -> None: ...

class RevokeUserCredentialsRequest(_message.Message):
    __slots__ = ("id", "revoke_sessions", "revoke_personal_access_tokens", "revoke_passkeys")
    ID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    REVOKE_PERSONAL_ACCESS_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REVOKE_PASSKEYS_FIELD_NUMBER: _ClassVar[int]
    id: str
    revoke_sessions: bool
    revoke_personal_access_tokens: bool
    revoke_passkeys: bool
    def __init__(self, id: _Optional[str] = ..., revoke_sessions: _Optional[bool] = ..., revoke_personal_access_tokens: _Optional[bool] = ..., revoke_passkeys: _Optional[bool] = ...) -> None: ...

class RevokeUserCredentialsResponse(_message.Message):
    __slots__ = ("sessions_revoked", "pats_revoked", "passkeys_revoked")
    SESSIONS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    PATS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    PASSKEYS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    sessions_revoked: int
    pats_revoked: int
    passkeys_revoked: int
    def __init__(self, sessions_revoked: _Optional[int] = ..., pats_revoked: _Optional[int] = ..., passkeys_revoked: _Optional[int] = ...) -> None: ...

class Invite(_message.Message):
    __slots__ = ("id", "code", "email", "assigned_role", "created_at", "expires_at", "used", "used_at", "used_by_user_id", "created_by_user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ROLE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    USED_AT_FIELD_NUMBER: _ClassVar[int]
    USED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    email: str
    assigned_role: _auth_pb2.UserRole
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    used: bool
    used_at: _timestamp_pb2.Timestamp
    used_by_user_id: str
    created_by_user_id: str
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., email: _Optional[str] = ..., assigned_role: _Optional[_Union[_auth_pb2.UserRole, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., used: _Optional[bool] = ..., used_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., used_by_user_id: _Optional[str] = ..., created_by_user_id: _Optional[str] = ...) -> None: ...

class ListInvitesRequest(_message.Message):
    __slots__ = ("include_used", "include_expired", "page")
    INCLUDE_USED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    include_used: bool
    include_expired: bool
    page: _common_pb2.PageRequest
    def __init__(self, include_used: _Optional[bool] = ..., include_expired: _Optional[bool] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListInvitesResponse(_message.Message):
    __slots__ = ("invites", "page")
    INVITES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    invites: _containers.RepeatedCompositeFieldContainer[Invite]
    page: _common_pb2.PageResponse
    def __init__(self, invites: _Optional[_Iterable[_Union[Invite, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class CreateInviteRequest(_message.Message):
    __slots__ = ("email", "assigned_role", "expires_at", "send_email")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ROLE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    SEND_EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    assigned_role: _auth_pb2.UserRole
    expires_at: _timestamp_pb2.Timestamp
    send_email: bool
    def __init__(self, email: _Optional[str] = ..., assigned_role: _Optional[_Union[_auth_pb2.UserRole, str]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., send_email: _Optional[bool] = ...) -> None: ...

class CreateInviteResponse(_message.Message):
    __slots__ = ("invite",)
    INVITE_FIELD_NUMBER: _ClassVar[int]
    invite: Invite
    def __init__(self, invite: _Optional[_Union[Invite, _Mapping]] = ...) -> None: ...

class RevokeInviteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RevokeInviteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResendInviteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResendInviteResponse(_message.Message):
    __slots__ = ("delivered", "error_message")
    DELIVERED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    delivered: bool
    error_message: str
    def __init__(self, delivered: _Optional[bool] = ..., error_message: _Optional[str] = ...) -> None: ...

class AuditEntry(_message.Message):
    __slots__ = ("id", "ts", "actor_user_id", "actor_username", "actor_pat_id", "ip_address", "action", "severity", "resource_type", "resource_id", "diff", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_USERNAME_FIELD_NUMBER: _ClassVar[int]
    ACTOR_PAT_ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    ts: _timestamp_pb2.Timestamp
    actor_user_id: str
    actor_username: str
    actor_pat_id: str
    ip_address: str
    action: str
    severity: AuditSeverity
    resource_type: str
    resource_id: str
    diff: _struct_pb2.Struct
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., actor_user_id: _Optional[str] = ..., actor_username: _Optional[str] = ..., actor_pat_id: _Optional[str] = ..., ip_address: _Optional[str] = ..., action: _Optional[str] = ..., severity: _Optional[_Union[AuditSeverity, str]] = ..., resource_type: _Optional[str] = ..., resource_id: _Optional[str] = ..., diff: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListAuditEntriesRequest(_message.Message):
    __slots__ = ("time_range", "actor_user_id", "resource_type", "resource_id", "actions", "min_severity", "query", "page")
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_USER_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    time_range: _common_pb2.TimeRange
    actor_user_id: str
    resource_type: str
    resource_id: str
    actions: _containers.RepeatedScalarFieldContainer[str]
    min_severity: AuditSeverity
    query: str
    page: _common_pb2.PageRequest
    def __init__(self, time_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., actor_user_id: _Optional[str] = ..., resource_type: _Optional[str] = ..., resource_id: _Optional[str] = ..., actions: _Optional[_Iterable[str]] = ..., min_severity: _Optional[_Union[AuditSeverity, str]] = ..., query: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListAuditEntriesResponse(_message.Message):
    __slots__ = ("entries", "page")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[AuditEntry]
    page: _common_pb2.PageResponse
    def __init__(self, entries: _Optional[_Iterable[_Union[AuditEntry, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class AdminJob(_message.Message):
    __slots__ = ("id", "job_type", "provider", "user_id", "external_account_id", "status", "worker_id", "worker_name", "priority", "attempt", "max_attempts", "enqueued_at", "started_at", "finished_at", "next_retry_at", "error_class", "error_message", "payload_type_url")
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    ENQUEUED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    NEXT_RETRY_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_CLASS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    job_type: str
    provider: str
    user_id: str
    external_account_id: str
    status: AdminJobStatus
    worker_id: str
    worker_name: str
    priority: str
    attempt: int
    max_attempts: int
    enqueued_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    next_retry_at: _timestamp_pb2.Timestamp
    error_class: str
    error_message: str
    payload_type_url: str
    def __init__(self, id: _Optional[str] = ..., job_type: _Optional[str] = ..., provider: _Optional[str] = ..., user_id: _Optional[str] = ..., external_account_id: _Optional[str] = ..., status: _Optional[_Union[AdminJobStatus, str]] = ..., worker_id: _Optional[str] = ..., worker_name: _Optional[str] = ..., priority: _Optional[str] = ..., attempt: _Optional[int] = ..., max_attempts: _Optional[int] = ..., enqueued_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., next_retry_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error_class: _Optional[str] = ..., error_message: _Optional[str] = ..., payload_type_url: _Optional[str] = ...) -> None: ...

class ListJobsRequest(_message.Message):
    __slots__ = ("statuses", "job_types", "providers", "user_id", "worker_name", "enqueued_range", "page")
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPES_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    ENQUEUED_RANGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedScalarFieldContainer[AdminJobStatus]
    job_types: _containers.RepeatedScalarFieldContainer[str]
    providers: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    worker_name: str
    enqueued_range: _common_pb2.TimeRange
    page: _common_pb2.PageRequest
    def __init__(self, statuses: _Optional[_Iterable[_Union[AdminJobStatus, str]]] = ..., job_types: _Optional[_Iterable[str]] = ..., providers: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ..., worker_name: _Optional[str] = ..., enqueued_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListJobsResponse(_message.Message):
    __slots__ = ("jobs", "page", "count_by_status")
    class CountByStatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    JOBS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    COUNT_BY_STATUS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[AdminJob]
    page: _common_pb2.PageResponse
    count_by_status: _containers.ScalarMap[str, int]
    def __init__(self, jobs: _Optional[_Iterable[_Union[AdminJob, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ..., count_by_status: _Optional[_Mapping[str, int]] = ...) -> None: ...

class GetJobRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetJobResponse(_message.Message):
    __slots__ = ("job", "payload_view", "result_view", "attempts")
    JOB_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_VIEW_FIELD_NUMBER: _ClassVar[int]
    RESULT_VIEW_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    job: AdminJob
    payload_view: _struct_pb2.Struct
    result_view: _struct_pb2.Struct
    attempts: _containers.RepeatedCompositeFieldContainer[JobAttempt]
    def __init__(self, job: _Optional[_Union[AdminJob, _Mapping]] = ..., payload_view: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., result_view: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., attempts: _Optional[_Iterable[_Union[JobAttempt, _Mapping]]] = ...) -> None: ...

class JobAttempt(_message.Message):
    __slots__ = ("attempt", "worker_id", "worker_name", "started_at", "finished_at", "status", "error_class", "error_message")
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_CLASS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    attempt: int
    worker_id: str
    worker_name: str
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    status: AdminJobStatus
    error_class: str
    error_message: str
    def __init__(self, attempt: _Optional[int] = ..., worker_id: _Optional[str] = ..., worker_name: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[AdminJobStatus, str]] = ..., error_class: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class RetryJobRequest(_message.Message):
    __slots__ = ("id", "reset_attempts")
    ID_FIELD_NUMBER: _ClassVar[int]
    RESET_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    reset_attempts: bool
    def __init__(self, id: _Optional[str] = ..., reset_attempts: _Optional[bool] = ...) -> None: ...

class RetryJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: AdminJob
    def __init__(self, job: _Optional[_Union[AdminJob, _Mapping]] = ...) -> None: ...

class CancelJobRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CancelJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: AdminJob
    def __init__(self, job: _Optional[_Union[AdminJob, _Mapping]] = ...) -> None: ...

class ListDeadLetterJobsRequest(_message.Message):
    __slots__ = ("providers", "user_id", "failed_range", "page")
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FAILED_RANGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    failed_range: _common_pb2.TimeRange
    page: _common_pb2.PageRequest
    def __init__(self, providers: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ..., failed_range: _Optional[_Union[_common_pb2.TimeRange, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListDeadLetterJobsResponse(_message.Message):
    __slots__ = ("jobs", "page")
    JOBS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[AdminJob]
    page: _common_pb2.PageResponse
    def __init__(self, jobs: _Optional[_Iterable[_Union[AdminJob, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class RequeueDeadLetterJobRequest(_message.Message):
    __slots__ = ("id", "reset_attempts")
    ID_FIELD_NUMBER: _ClassVar[int]
    RESET_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    reset_attempts: bool
    def __init__(self, id: _Optional[str] = ..., reset_attempts: _Optional[bool] = ...) -> None: ...

class RequeueDeadLetterJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: AdminJob
    def __init__(self, job: _Optional[_Union[AdminJob, _Mapping]] = ...) -> None: ...

class OrphanedSourceGroup(_message.Message):
    __slots__ = ("worker_name", "source_count", "external_account_count", "user_count", "oldest_imported_at")
    WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_COUNT_FIELD_NUMBER: _ClassVar[int]
    OLDEST_IMPORTED_AT_FIELD_NUMBER: _ClassVar[int]
    worker_name: str
    source_count: int
    external_account_count: int
    user_count: int
    oldest_imported_at: _timestamp_pb2.Timestamp
    def __init__(self, worker_name: _Optional[str] = ..., source_count: _Optional[int] = ..., external_account_count: _Optional[int] = ..., user_count: _Optional[int] = ..., oldest_imported_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListOrphanedSourcesRequest(_message.Message):
    __slots__ = ("worker_name",)
    WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    worker_name: str
    def __init__(self, worker_name: _Optional[str] = ...) -> None: ...

class ListOrphanedSourcesResponse(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[OrphanedSourceGroup]
    def __init__(self, groups: _Optional[_Iterable[_Union[OrphanedSourceGroup, _Mapping]]] = ...) -> None: ...

class WebhookSigningTokenInfo(_message.Message):
    __slots__ = ("external_account_id", "user_id", "provider", "last_rotated_at", "last_used_at")
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    LAST_ROTATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    external_account_id: str
    user_id: str
    provider: str
    last_rotated_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    def __init__(self, external_account_id: _Optional[str] = ..., user_id: _Optional[str] = ..., provider: _Optional[str] = ..., last_rotated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListWebhookSigningTokensRequest(_message.Message):
    __slots__ = ("provider", "page")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    provider: str
    page: _common_pb2.PageRequest
    def __init__(self, provider: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListWebhookSigningTokensResponse(_message.Message):
    __slots__ = ("tokens", "page")
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[WebhookSigningTokenInfo]
    page: _common_pb2.PageResponse
    def __init__(self, tokens: _Optional[_Iterable[_Union[WebhookSigningTokenInfo, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class BulkRotateWebhookSigningTokensRequest(_message.Message):
    __slots__ = ("provider", "older_than", "external_account_ids")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    OLDER_THAN_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    provider: str
    older_than: _duration_pb2.Duration
    external_account_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, provider: _Optional[str] = ..., older_than: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., external_account_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class BulkRotateWebhookSigningTokensResponse(_message.Message):
    __slots__ = ("rotated_count", "rotation_jobs")
    ROTATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ROTATION_JOBS_FIELD_NUMBER: _ClassVar[int]
    rotated_count: int
    rotation_jobs: _containers.RepeatedCompositeFieldContainer[WebhookRotationJobs]
    def __init__(self, rotated_count: _Optional[int] = ..., rotation_jobs: _Optional[_Iterable[_Union[WebhookRotationJobs, _Mapping]]] = ...) -> None: ...

class WebhookRotationJobs(_message.Message):
    __slots__ = ("external_account_id", "unregister_job_id", "register_job_id")
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    UNREGISTER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    external_account_id: str
    unregister_job_id: str
    register_job_id: str
    def __init__(self, external_account_id: _Optional[str] = ..., unregister_job_id: _Optional[str] = ..., register_job_id: _Optional[str] = ...) -> None: ...

class GetSystemHealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSystemHealthResponse(_message.Message):
    __slots__ = ("overall", "database", "queue", "storage", "email", "workers_healthy", "workers_degraded", "workers_offline", "jobs_queued", "jobs_running", "jobs_dead_letter", "error_rate_15m", "checked_at")
    OVERALL_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    WORKERS_HEALTHY_FIELD_NUMBER: _ClassVar[int]
    WORKERS_DEGRADED_FIELD_NUMBER: _ClassVar[int]
    WORKERS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    JOBS_QUEUED_FIELD_NUMBER: _ClassVar[int]
    JOBS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    JOBS_DEAD_LETTER_FIELD_NUMBER: _ClassVar[int]
    ERROR_RATE_15M_FIELD_NUMBER: _ClassVar[int]
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    overall: HealthState
    database: ComponentHealth
    queue: ComponentHealth
    storage: ComponentHealth
    email: ComponentHealth
    workers_healthy: int
    workers_degraded: int
    workers_offline: int
    jobs_queued: int
    jobs_running: int
    jobs_dead_letter: int
    error_rate_15m: float
    checked_at: _timestamp_pb2.Timestamp
    def __init__(self, overall: _Optional[_Union[HealthState, str]] = ..., database: _Optional[_Union[ComponentHealth, _Mapping]] = ..., queue: _Optional[_Union[ComponentHealth, _Mapping]] = ..., storage: _Optional[_Union[ComponentHealth, _Mapping]] = ..., email: _Optional[_Union[ComponentHealth, _Mapping]] = ..., workers_healthy: _Optional[int] = ..., workers_degraded: _Optional[int] = ..., workers_offline: _Optional[int] = ..., jobs_queued: _Optional[int] = ..., jobs_running: _Optional[int] = ..., jobs_dead_letter: _Optional[int] = ..., error_rate_15m: _Optional[float] = ..., checked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ComponentHealth(_message.Message):
    __slots__ = ("state", "detail", "measurements")
    class MeasurementsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    state: HealthState
    detail: str
    measurements: _containers.ScalarMap[str, float]
    def __init__(self, state: _Optional[_Union[HealthState, str]] = ..., detail: _Optional[str] = ..., measurements: _Optional[_Mapping[str, float]] = ...) -> None: ...

class StreamAdminEventsRequest(_message.Message):
    __slots__ = ("types",)
    TYPES_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[AdminEventType]
    def __init__(self, types: _Optional[_Iterable[_Union[AdminEventType, str]]] = ...) -> None: ...

class AdminEvent(_message.Message):
    __slots__ = ("id", "type", "severity", "ts", "i18n_key", "i18n_params", "user_id", "worker_name", "job_id")
    class I18nParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    I18N_KEY_FIELD_NUMBER: _ClassVar[int]
    I18N_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: AdminEventType
    severity: AuditSeverity
    ts: _timestamp_pb2.Timestamp
    i18n_key: str
    i18n_params: _containers.ScalarMap[str, str]
    user_id: str
    worker_name: str
    job_id: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[AdminEventType, str]] = ..., severity: _Optional[_Union[AuditSeverity, str]] = ..., ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., i18n_key: _Optional[str] = ..., i18n_params: _Optional[_Mapping[str, str]] = ..., user_id: _Optional[str] = ..., worker_name: _Optional[str] = ..., job_id: _Optional[str] = ...) -> None: ...

class TriggerMaintenanceRequest(_message.Message):
    __slots__ = ("operation", "user_ids", "confirm_phrase")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_PHRASE_FIELD_NUMBER: _ClassVar[int]
    operation: MaintenanceOperation
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    confirm_phrase: str
    def __init__(self, operation: _Optional[_Union[MaintenanceOperation, str]] = ..., user_ids: _Optional[_Iterable[str]] = ..., confirm_phrase: _Optional[str] = ...) -> None: ...

class TriggerMaintenanceResponse(_message.Message):
    __slots__ = ("job_id", "estimated_record_count")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    estimated_record_count: int
    def __init__(self, job_id: _Optional[str] = ..., estimated_record_count: _Optional[int] = ...) -> None: ...
