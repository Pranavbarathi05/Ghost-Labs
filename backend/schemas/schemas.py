"""
Pydantic schemas for request/response validation
"""

from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional
from enum import Enum
import re


# =========================
# User Schemas
# =========================

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    full_name: Optional[str] = Field(default=None, max_length=100)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=64)

    @validator("password")
    def validate_password(cls, v):
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one number")
        return v


class UserResponse(UserBase):
    id: int
    role: UserRole
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    password: str = Field(min_length=8)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None


# =========================
# Room Schemas
# =========================

class RoomCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: Optional[str] = Field(default=None, max_length=300)


class RoomResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    creator_id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# Workspace Schemas
# =========================

class WorkspaceStatus(str, Enum):
    STOPPED = "stopped"
    RUNNING = "running"
    CREATING = "creating"
    ERROR = "error"


class WorkspaceCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)


class WorkspaceResponse(BaseModel):
    id: int
    name: str
    owner_id: int
    container_id: Optional[str]
    status: WorkspaceStatus
    tunnel_url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class WorkspaceAction(BaseModel):
    action: str = Field(min_length=3)  # start, stop, snapshot, restore
    snapshot_name: Optional[str] = None


# =========================
# Message Schemas
# =========================

class ChatMessage(BaseModel):
    room_id: str = Field(min_length=1)
    user_id: str = Field(min_length=1)
    content: str = Field(min_length=1, max_length=1000)
    timestamp: datetime