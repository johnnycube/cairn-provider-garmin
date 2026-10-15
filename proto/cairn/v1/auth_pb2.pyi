import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DateFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATE_FORMAT_UNSPECIFIED: _ClassVar[DateFormat]
    DATE_FORMAT_ISO: _ClassVar[DateFormat]
    DATE_FORMAT_US: _ClassVar[DateFormat]
    DATE_FORMAT_EU: _ClassVar[DateFormat]

class TimeFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIME_FORMAT_UNSPECIFIED: _ClassVar[TimeFormat]
    TIME_FORMAT_24H: _ClassVar[TimeFormat]
    TIME_FORMAT_12H: _ClassVar[TimeFormat]

class UserRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_ROLE_UNSPECIFIED: _ClassVar[UserRole]
    USER_ROLE_USER: _ClassVar[UserRole]
    USER_ROLE_ADMIN: _ClassVar[UserRole]

class UserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_STATUS_UNSPECIFIED: _ClassVar[UserStatus]
    USER_STATUS_ACTIVE: _ClassVar[UserStatus]
    USER_STATUS_INVITED: _ClassVar[UserStatus]
    USER_STATUS_SUSPENDED: _ClassVar[UserStatus]
    USER_STATUS_DELETED: _ClassVar[UserStatus]

class UnitSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNIT_SYSTEM_UNSPECIFIED: _ClassVar[UnitSystem]
    UNIT_SYSTEM_METRIC: _ClassVar[UnitSystem]
    UNIT_SYSTEM_IMPERIAL: _ClassVar[UnitSystem]

class TwoFactorMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TWO_FACTOR_METHOD_UNSPECIFIED: _ClassVar[TwoFactorMethod]
    TWO_FACTOR_METHOD_WEBAUTHN: _ClassVar[TwoFactorMethod]

class AuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_METHOD_UNSPECIFIED: _ClassVar[AuthMethod]
    AUTH_METHOD_PASSWORD: _ClassVar[AuthMethod]
    AUTH_METHOD_PASSWORD_WITH_WEBAUTHN_2FA: _ClassVar[AuthMethod]
    AUTH_METHOD_WEBAUTHN_PASSKEY: _ClassVar[AuthMethod]
    AUTH_METHOD_OIDC: _ClassVar[AuthMethod]
    AUTH_METHOD_PERSONAL_ACCESS_TOKEN: _ClassVar[AuthMethod]

class ExternalAccountStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXTERNAL_ACCOUNT_STATUS_UNSPECIFIED: _ClassVar[ExternalAccountStatus]
    EXTERNAL_ACCOUNT_STATUS_ACTIVE: _ClassVar[ExternalAccountStatus]
    EXTERNAL_ACCOUNT_STATUS_AUTH_INVALID: _ClassVar[ExternalAccountStatus]
    EXTERNAL_ACCOUNT_STATUS_WORKER_OFFLINE: _ClassVar[ExternalAccountStatus]
    EXTERNAL_ACCOUNT_STATUS_RATE_LIMITED: _ClassVar[ExternalAccountStatus]
    EXTERNAL_ACCOUNT_STATUS_NEEDS_MIGRATION: _ClassVar[ExternalAccountStatus]
    EXTERNAL_ACCOUNT_STATUS_DISABLED: _ClassVar[ExternalAccountStatus]

class AvailableFieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AVAILABLE_FIELD_TYPE_UNSPECIFIED: _ClassVar[AvailableFieldType]
    AVAILABLE_FIELD_TYPE_TEXT: _ClassVar[AvailableFieldType]
    AVAILABLE_FIELD_TYPE_SECRET: _ClassVar[AvailableFieldType]
    AVAILABLE_FIELD_TYPE_URL: _ClassVar[AvailableFieldType]
    AVAILABLE_FIELD_TYPE_NUMBER: _ClassVar[AvailableFieldType]
    AVAILABLE_FIELD_TYPE_BOOL: _ClassVar[AvailableFieldType]
    AVAILABLE_FIELD_TYPE_SELECT: _ClassVar[AvailableFieldType]
    AVAILABLE_FIELD_TYPE_MULTI_SELECT: _ClassVar[AvailableFieldType]
    AVAILABLE_FIELD_TYPE_DATE: _ClassVar[AvailableFieldType]

class AvailableAuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AVAILABLE_AUTH_METHOD_UNSPECIFIED: _ClassVar[AvailableAuthMethod]
    AVAILABLE_AUTH_METHOD_NONE: _ClassVar[AvailableAuthMethod]
    AVAILABLE_AUTH_METHOD_OAUTH2: _ClassVar[AvailableAuthMethod]
    AVAILABLE_AUTH_METHOD_API_KEY: _ClassVar[AvailableAuthMethod]
    AVAILABLE_AUTH_METHOD_BASIC: _ClassVar[AvailableAuthMethod]
    AVAILABLE_AUTH_METHOD_CUSTOM: _ClassVar[AvailableAuthMethod]
DATE_FORMAT_UNSPECIFIED: DateFormat
DATE_FORMAT_ISO: DateFormat
DATE_FORMAT_US: DateFormat
DATE_FORMAT_EU: DateFormat
TIME_FORMAT_UNSPECIFIED: TimeFormat
TIME_FORMAT_24H: TimeFormat
TIME_FORMAT_12H: TimeFormat
USER_ROLE_UNSPECIFIED: UserRole
USER_ROLE_USER: UserRole
USER_ROLE_ADMIN: UserRole
USER_STATUS_UNSPECIFIED: UserStatus
USER_STATUS_ACTIVE: UserStatus
USER_STATUS_INVITED: UserStatus
USER_STATUS_SUSPENDED: UserStatus
USER_STATUS_DELETED: UserStatus
UNIT_SYSTEM_UNSPECIFIED: UnitSystem
UNIT_SYSTEM_METRIC: UnitSystem
UNIT_SYSTEM_IMPERIAL: UnitSystem
TWO_FACTOR_METHOD_UNSPECIFIED: TwoFactorMethod
TWO_FACTOR_METHOD_WEBAUTHN: TwoFactorMethod
AUTH_METHOD_UNSPECIFIED: AuthMethod
AUTH_METHOD_PASSWORD: AuthMethod
AUTH_METHOD_PASSWORD_WITH_WEBAUTHN_2FA: AuthMethod
AUTH_METHOD_WEBAUTHN_PASSKEY: AuthMethod
AUTH_METHOD_OIDC: AuthMethod
AUTH_METHOD_PERSONAL_ACCESS_TOKEN: AuthMethod
EXTERNAL_ACCOUNT_STATUS_UNSPECIFIED: ExternalAccountStatus
EXTERNAL_ACCOUNT_STATUS_ACTIVE: ExternalAccountStatus
EXTERNAL_ACCOUNT_STATUS_AUTH_INVALID: ExternalAccountStatus
EXTERNAL_ACCOUNT_STATUS_WORKER_OFFLINE: ExternalAccountStatus
EXTERNAL_ACCOUNT_STATUS_RATE_LIMITED: ExternalAccountStatus
EXTERNAL_ACCOUNT_STATUS_NEEDS_MIGRATION: ExternalAccountStatus
EXTERNAL_ACCOUNT_STATUS_DISABLED: ExternalAccountStatus
AVAILABLE_FIELD_TYPE_UNSPECIFIED: AvailableFieldType
AVAILABLE_FIELD_TYPE_TEXT: AvailableFieldType
AVAILABLE_FIELD_TYPE_SECRET: AvailableFieldType
AVAILABLE_FIELD_TYPE_URL: AvailableFieldType
AVAILABLE_FIELD_TYPE_NUMBER: AvailableFieldType
AVAILABLE_FIELD_TYPE_BOOL: AvailableFieldType
AVAILABLE_FIELD_TYPE_SELECT: AvailableFieldType
AVAILABLE_FIELD_TYPE_MULTI_SELECT: AvailableFieldType
AVAILABLE_FIELD_TYPE_DATE: AvailableFieldType
AVAILABLE_AUTH_METHOD_UNSPECIFIED: AvailableAuthMethod
AVAILABLE_AUTH_METHOD_NONE: AvailableAuthMethod
AVAILABLE_AUTH_METHOD_OAUTH2: AvailableAuthMethod
AVAILABLE_AUTH_METHOD_API_KEY: AvailableAuthMethod
AVAILABLE_AUTH_METHOD_BASIC: AvailableAuthMethod
AVAILABLE_AUTH_METHOD_CUSTOM: AvailableAuthMethod

class User(_message.Message):
    __slots__ = ("id", "username", "email", "email_verified", "display_name", "avatar_url", "locale", "timezone", "units", "role", "status", "created_at", "updated_at", "last_login_at", "date_format", "time_format")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_AT_FIELD_NUMBER: _ClassVar[int]
    DATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TIME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    username: str
    email: str
    email_verified: bool
    display_name: str
    avatar_url: str
    locale: str
    timezone: str
    units: UnitSystem
    role: UserRole
    status: UserStatus
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    last_login_at: _timestamp_pb2.Timestamp
    date_format: DateFormat
    time_format: TimeFormat
    def __init__(self, id: _Optional[str] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., email_verified: _Optional[bool] = ..., display_name: _Optional[str] = ..., avatar_url: _Optional[str] = ..., locale: _Optional[str] = ..., timezone: _Optional[str] = ..., units: _Optional[_Union[UnitSystem, str]] = ..., role: _Optional[_Union[UserRole, str]] = ..., status: _Optional[_Union[UserStatus, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_login_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_format: _Optional[_Union[DateFormat, str]] = ..., time_format: _Optional[_Union[TimeFormat, str]] = ...) -> None: ...

class GetLoginMethodsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLoginMethodsResponse(_message.Message):
    __slots__ = ("password_enabled", "webauthn_enabled", "registration_open", "requires_invite", "oidc_clients")
    PASSWORD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    WEBAUTHN_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_OPEN_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_INVITE_FIELD_NUMBER: _ClassVar[int]
    OIDC_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    password_enabled: bool
    webauthn_enabled: bool
    registration_open: bool
    requires_invite: bool
    oidc_clients: _containers.RepeatedCompositeFieldContainer[OIDCLoginOption]
    def __init__(self, password_enabled: _Optional[bool] = ..., webauthn_enabled: _Optional[bool] = ..., registration_open: _Optional[bool] = ..., requires_invite: _Optional[bool] = ..., oidc_clients: _Optional[_Iterable[_Union[OIDCLoginOption, _Mapping]]] = ...) -> None: ...

class OIDCLoginOption(_message.Message):
    __slots__ = ("id", "display_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class LoginPasswordRequest(_message.Message):
    __slots__ = ("identifier", "password", "remember_me")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    REMEMBER_ME_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    password: str
    remember_me: bool
    def __init__(self, identifier: _Optional[str] = ..., password: _Optional[str] = ..., remember_me: _Optional[bool] = ...) -> None: ...

class LoginPasswordResponse(_message.Message):
    __slots__ = ("session", "challenge")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    session: SessionResult
    challenge: TwoFactorChallenge
    def __init__(self, session: _Optional[_Union[SessionResult, _Mapping]] = ..., challenge: _Optional[_Union[TwoFactorChallenge, _Mapping]] = ...) -> None: ...

class TwoFactorChallenge(_message.Message):
    __slots__ = ("challenge_token", "methods")
    CHALLENGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    challenge_token: str
    methods: _containers.RepeatedScalarFieldContainer[TwoFactorMethod]
    def __init__(self, challenge_token: _Optional[str] = ..., methods: _Optional[_Iterable[_Union[TwoFactorMethod, str]]] = ...) -> None: ...

class Complete2FARequest(_message.Message):
    __slots__ = ("challenge_token", "method", "remember_me")
    CHALLENGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REMEMBER_ME_FIELD_NUMBER: _ClassVar[int]
    challenge_token: str
    method: TwoFactorMethod
    remember_me: bool
    def __init__(self, challenge_token: _Optional[str] = ..., method: _Optional[_Union[TwoFactorMethod, str]] = ..., remember_me: _Optional[bool] = ...) -> None: ...

class Complete2FAResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: SessionResult
    def __init__(self, session: _Optional[_Union[SessionResult, _Mapping]] = ...) -> None: ...

class SessionResult(_message.Message):
    __slots__ = ("session_id", "session_token", "expires_at", "user")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    session_token: str
    expires_at: _timestamp_pb2.Timestamp
    user: User
    def __init__(self, session_id: _Optional[str] = ..., session_token: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ("username", "email", "password", "display_name", "locale", "timezone", "units", "invite_code")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    INVITE_CODE_FIELD_NUMBER: _ClassVar[int]
    username: str
    email: str
    password: str
    display_name: str
    locale: str
    timezone: str
    units: UnitSystem
    invite_code: str
    def __init__(self, username: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., display_name: _Optional[str] = ..., locale: _Optional[str] = ..., timezone: _Optional[str] = ..., units: _Optional[_Union[UnitSystem, str]] = ..., invite_code: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("user", "requires_email_verification", "session")
    USER_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_EMAIL_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    user: User
    requires_email_verification: bool
    session: SessionResult
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., requires_email_verification: _Optional[bool] = ..., session: _Optional[_Union[SessionResult, _Mapping]] = ...) -> None: ...

class ChangePasswordRequest(_message.Message):
    __slots__ = ("current_password", "new_password")
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    current_password: str
    new_password: str
    def __init__(self, current_password: _Optional[str] = ..., new_password: _Optional[str] = ...) -> None: ...

class ChangePasswordResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestPasswordResetRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class RequestPasswordResetResponse(_message.Message):
    __slots__ = ("email_dispatch_attempted",)
    EMAIL_DISPATCH_ATTEMPTED_FIELD_NUMBER: _ClassVar[int]
    email_dispatch_attempted: bool
    def __init__(self, email_dispatch_attempted: _Optional[bool] = ...) -> None: ...

class ConfirmPasswordResetRequest(_message.Message):
    __slots__ = ("reset_token", "new_password")
    RESET_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    reset_token: str
    new_password: str
    def __init__(self, reset_token: _Optional[str] = ..., new_password: _Optional[str] = ...) -> None: ...

class ConfirmPasswordResetResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: SessionResult
    def __init__(self, session: _Optional[_Union[SessionResult, _Mapping]] = ...) -> None: ...

class StartOIDCLoginRequest(_message.Message):
    __slots__ = ("oidc_client_id", "post_login_redirect")
    OIDC_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    POST_LOGIN_REDIRECT_FIELD_NUMBER: _ClassVar[int]
    oidc_client_id: str
    post_login_redirect: str
    def __init__(self, oidc_client_id: _Optional[str] = ..., post_login_redirect: _Optional[str] = ...) -> None: ...

class StartOIDCLoginResponse(_message.Message):
    __slots__ = ("authorize_url", "state")
    AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    authorize_url: str
    state: str
    def __init__(self, authorize_url: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class StartOIDCLinkRequest(_message.Message):
    __slots__ = ("oidc_client_id",)
    OIDC_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    oidc_client_id: str
    def __init__(self, oidc_client_id: _Optional[str] = ...) -> None: ...

class StartOIDCLinkResponse(_message.Message):
    __slots__ = ("authorize_url", "state")
    AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    authorize_url: str
    state: str
    def __init__(self, authorize_url: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class UnlinkOIDCIdentityRequest(_message.Message):
    __slots__ = ("identity_id",)
    IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    identity_id: str
    def __init__(self, identity_id: _Optional[str] = ...) -> None: ...

class UnlinkOIDCIdentityResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLinkedIdentitiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLinkedIdentitiesResponse(_message.Message):
    __slots__ = ("identities",)
    IDENTITIES_FIELD_NUMBER: _ClassVar[int]
    identities: _containers.RepeatedCompositeFieldContainer[LinkedIdentity]
    def __init__(self, identities: _Optional[_Iterable[_Union[LinkedIdentity, _Mapping]]] = ...) -> None: ...

class LinkedIdentity(_message.Message):
    __slots__ = ("id", "oidc_client_id", "oidc_client_display_name", "subject", "email", "linked_at", "last_used_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    OIDC_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    OIDC_CLIENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LINKED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    oidc_client_id: str
    oidc_client_display_name: str
    subject: str
    email: str
    linked_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., oidc_client_id: _Optional[str] = ..., oidc_client_display_name: _Optional[str] = ..., subject: _Optional[str] = ..., email: _Optional[str] = ..., linked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ("all_devices",)
    ALL_DEVICES_FIELD_NUMBER: _ClassVar[int]
    all_devices: bool
    def __init__(self, all_devices: _Optional[bool] = ...) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentUserRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentUserResponse(_message.Message):
    __slots__ = ("user", "permissions")
    USER_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    user: User
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateUserPreferencesRequest(_message.Message):
    __slots__ = ("date_format", "time_format", "units")
    DATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TIME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    date_format: DateFormat
    time_format: TimeFormat
    units: UnitSystem
    def __init__(self, date_format: _Optional[_Union[DateFormat, str]] = ..., time_format: _Optional[_Union[TimeFormat, str]] = ..., units: _Optional[_Union[UnitSystem, str]] = ...) -> None: ...

class UpdateUserPreferencesResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UpdateProfileRequest(_message.Message):
    __slots__ = ("field_mask", "display_name", "email", "locale", "timezone", "units", "avatar_url")
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    email: str
    locale: str
    timezone: str
    units: UnitSystem
    avatar_url: str
    def __init__(self, field_mask: _Optional[_Iterable[str]] = ..., display_name: _Optional[str] = ..., email: _Optional[str] = ..., locale: _Optional[str] = ..., timezone: _Optional[str] = ..., units: _Optional[_Union[UnitSystem, str]] = ..., avatar_url: _Optional[str] = ...) -> None: ...

class UpdateProfileResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("id", "user_agent_summary", "ip_address", "ip_geo_summary", "created_at", "last_seen_at", "expires_at", "is_current", "auth_method")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_GEO_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_agent_summary: str
    ip_address: str
    ip_geo_summary: str
    created_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    is_current: bool
    auth_method: AuthMethod
    def __init__(self, id: _Optional[str] = ..., user_agent_summary: _Optional[str] = ..., ip_address: _Optional[str] = ..., ip_geo_summary: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_current: _Optional[bool] = ..., auth_method: _Optional[_Union[AuthMethod, str]] = ...) -> None: ...

class ListSessionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]] = ...) -> None: ...

class RevokeSessionRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RevokeSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PersonalAccessToken(_message.Message):
    __slots__ = ("id", "name", "scopes", "created_at", "expires_at", "last_used_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreatePersonalAccessTokenRequest(_message.Message):
    __slots__ = ("name", "scopes", "expires_at")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreatePersonalAccessTokenResponse(_message.Message):
    __slots__ = ("token", "secret")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    token: PersonalAccessToken
    secret: str
    def __init__(self, token: _Optional[_Union[PersonalAccessToken, _Mapping]] = ..., secret: _Optional[str] = ...) -> None: ...

class ListPersonalAccessTokensRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPersonalAccessTokensResponse(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[PersonalAccessToken]
    def __init__(self, tokens: _Optional[_Iterable[_Union[PersonalAccessToken, _Mapping]]] = ...) -> None: ...

class RevokePersonalAccessTokenRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RevokePersonalAccessTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalAccount(_message.Message):
    __slots__ = ("id", "user_id", "provider", "provider_account_id", "display_label", "assigned_worker_name", "status", "status_reason", "config", "has_valid_credentials", "access_token_expires_at", "granted_scopes", "webhook_subscribed", "webhook_subscribed_at", "webhook_subscription_id", "rate_limit", "created_at", "updated_at", "last_sync_at", "last_successful_sync_at")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ConfigValueMeta
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ConfigValueMeta, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LABEL_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_REASON_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    HAS_VALID_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    GRANTED_SCOPES_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SUBSCRIBED_AT_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_SYNC_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    provider: str
    provider_account_id: str
    display_label: str
    assigned_worker_name: str
    status: ExternalAccountStatus
    status_reason: str
    config: _containers.MessageMap[str, ConfigValueMeta]
    has_valid_credentials: bool
    access_token_expires_at: _timestamp_pb2.Timestamp
    granted_scopes: _containers.RepeatedScalarFieldContainer[str]
    webhook_subscribed: bool
    webhook_subscribed_at: _timestamp_pb2.Timestamp
    webhook_subscription_id: str
    rate_limit: ExternalAccountRateLimit
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    last_sync_at: _timestamp_pb2.Timestamp
    last_successful_sync_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., provider: _Optional[str] = ..., provider_account_id: _Optional[str] = ..., display_label: _Optional[str] = ..., assigned_worker_name: _Optional[str] = ..., status: _Optional[_Union[ExternalAccountStatus, str]] = ..., status_reason: _Optional[str] = ..., config: _Optional[_Mapping[str, ConfigValueMeta]] = ..., has_valid_credentials: _Optional[bool] = ..., access_token_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., granted_scopes: _Optional[_Iterable[str]] = ..., webhook_subscribed: _Optional[bool] = ..., webhook_subscribed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., webhook_subscription_id: _Optional[str] = ..., rate_limit: _Optional[_Union[ExternalAccountRateLimit, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_sync_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_successful_sync_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ConfigValueMeta(_message.Message):
    __slots__ = ("has_value", "value", "is_secret")
    HAS_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_SECRET_FIELD_NUMBER: _ClassVar[int]
    has_value: bool
    value: str
    is_secret: bool
    def __init__(self, has_value: _Optional[bool] = ..., value: _Optional[str] = ..., is_secret: _Optional[bool] = ...) -> None: ...

class ExternalAccountRateLimit(_message.Message):
    __slots__ = ("short_remaining", "short_limit", "short_reset_at", "long_remaining", "long_limit", "long_reset_at")
    SHORT_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SHORT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SHORT_RESET_AT_FIELD_NUMBER: _ClassVar[int]
    LONG_REMAINING_FIELD_NUMBER: _ClassVar[int]
    LONG_LIMIT_FIELD_NUMBER: _ClassVar[int]
    LONG_RESET_AT_FIELD_NUMBER: _ClassVar[int]
    short_remaining: int
    short_limit: int
    short_reset_at: _timestamp_pb2.Timestamp
    long_remaining: int
    long_limit: int
    long_reset_at: _timestamp_pb2.Timestamp
    def __init__(self, short_remaining: _Optional[int] = ..., short_limit: _Optional[int] = ..., short_reset_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., long_remaining: _Optional[int] = ..., long_limit: _Optional[int] = ..., long_reset_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListExternalAccountsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListExternalAccountsResponse(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[ExternalAccount]
    def __init__(self, accounts: _Optional[_Iterable[_Union[ExternalAccount, _Mapping]]] = ...) -> None: ...

class ListAvailableProvidersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAvailableProvidersResponse(_message.Message):
    __slots__ = ("providers",)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[AvailableProvider]
    def __init__(self, providers: _Optional[_Iterable[_Union[AvailableProvider, _Mapping]]] = ...) -> None: ...

class AvailableProvider(_message.Message):
    __slots__ = ("provider_id", "display_name", "description", "icon_url", "setup_docs_url", "config_fields", "auth_method", "supports_webhooks", "supports_backfill", "primary_worker_name", "has_conflict")
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    SETUP_DOCS_URL_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELDS_FIELD_NUMBER: _ClassVar[int]
    AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_BACKFILL_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    HAS_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    display_name: str
    description: str
    icon_url: str
    setup_docs_url: str
    config_fields: _containers.RepeatedCompositeFieldContainer[AvailableConfigField]
    auth_method: AvailableAuthMethod
    supports_webhooks: bool
    supports_backfill: bool
    primary_worker_name: str
    has_conflict: bool
    def __init__(self, provider_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., icon_url: _Optional[str] = ..., setup_docs_url: _Optional[str] = ..., config_fields: _Optional[_Iterable[_Union[AvailableConfigField, _Mapping]]] = ..., auth_method: _Optional[_Union[AvailableAuthMethod, str]] = ..., supports_webhooks: _Optional[bool] = ..., supports_backfill: _Optional[bool] = ..., primary_worker_name: _Optional[str] = ..., has_conflict: _Optional[bool] = ...) -> None: ...

class AvailableConfigField(_message.Message):
    __slots__ = ("key", "label", "help_text", "type", "required", "validation_regex", "options", "computed_by_core", "placeholder", "default_value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_REGEX_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    COMPUTED_BY_CORE_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    help_text: str
    type: AvailableFieldType
    required: bool
    validation_regex: str
    options: _containers.RepeatedScalarFieldContainer[str]
    computed_by_core: bool
    placeholder: str
    default_value: str
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., help_text: _Optional[str] = ..., type: _Optional[_Union[AvailableFieldType, str]] = ..., required: _Optional[bool] = ..., validation_regex: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ..., computed_by_core: _Optional[bool] = ..., placeholder: _Optional[str] = ..., default_value: _Optional[str] = ...) -> None: ...

class CreateExternalAccountRequest(_message.Message):
    __slots__ = ("provider", "display_label", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LABEL_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    provider: str
    display_label: str
    config: _containers.ScalarMap[str, str]
    def __init__(self, provider: _Optional[str] = ..., display_label: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateExternalAccountResponse(_message.Message):
    __slots__ = ("account", "authorize_url")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
    account: ExternalAccount
    authorize_url: str
    def __init__(self, account: _Optional[_Union[ExternalAccount, _Mapping]] = ..., authorize_url: _Optional[str] = ...) -> None: ...

class UpdateExternalAccountConfigRequest(_message.Message):
    __slots__ = ("id", "config", "display_label", "assigned_worker_name")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LABEL_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_WORKER_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    config: _containers.ScalarMap[str, str]
    display_label: str
    assigned_worker_name: str
    def __init__(self, id: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ..., display_label: _Optional[str] = ..., assigned_worker_name: _Optional[str] = ...) -> None: ...

class UpdateExternalAccountConfigResponse(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: ExternalAccount
    def __init__(self, account: _Optional[_Union[ExternalAccount, _Mapping]] = ...) -> None: ...

class StartExternalAccountReauthorizeRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class StartExternalAccountReauthorizeResponse(_message.Message):
    __slots__ = ("authorize_url",)
    AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
    authorize_url: str
    def __init__(self, authorize_url: _Optional[str] = ...) -> None: ...

class SetExternalAccountEnabledRequest(_message.Message):
    __slots__ = ("id", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., enabled: _Optional[bool] = ...) -> None: ...

class SetExternalAccountEnabledResponse(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: ExternalAccount
    def __init__(self, account: _Optional[_Union[ExternalAccount, _Mapping]] = ...) -> None: ...

class DeleteExternalAccountRequest(_message.Message):
    __slots__ = ("id", "delete_exclusive_activities")
    ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_EXCLUSIVE_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    delete_exclusive_activities: bool
    def __init__(self, id: _Optional[str] = ..., delete_exclusive_activities: _Optional[bool] = ...) -> None: ...

class DeleteExternalAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TriggerSyncRequest(_message.Message):
    __slots__ = ("id", "since")
    ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    since: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TriggerSyncResponse(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class RotateWebhookTokenRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RotateWebhookTokenResponse(_message.Message):
    __slots__ = ("unregister_job_id", "register_job_id")
    UNREGISTER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    unregister_job_id: str
    register_job_id: str
    def __init__(self, unregister_job_id: _Optional[str] = ..., register_job_id: _Optional[str] = ...) -> None: ...
