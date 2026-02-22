"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from enum import Enum


# User Schemas
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    role: UserRole
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None


# Room Schemas
class RoomCreate(BaseModel):
    name: str
    description: Optional[str] = None


class RoomResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    creator_id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


# Workspace Schemas
class WorkspaceStatus(str, Enum):
    STOPPED = "stopped"
    RUNNING = "running"
    CREATING = "creating"
    ERROR = "error"


class WorkspaceCreate(BaseModel):
    name: str


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
    action: str  # start, stop, snapshot, restore
    snapshot_name: Optional[str] = None


# Message Schemas
class ChatMessage(BaseModel):
    room_id: str
    user_id: str
    content: str
    timestamp: datetime
