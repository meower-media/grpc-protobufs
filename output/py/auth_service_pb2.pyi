from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CheckTokenReq(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class CheckTokenResp(_message.Message):
    __slots__ = ("valid", "session_id", "user_id")
    VALID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    session_id: str
    user_id: str
    def __init__(self, valid: bool = ..., session_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...
