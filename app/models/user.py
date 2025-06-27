from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from typing import Optional
from typing_extensions import Literal
from datetime import datetime

class UserRole(str, Enum):
    ADMIN: Literal["ADMIN"] = "ADMIN"
    USER: Literal["USER"] = "USER"
    UNAUTHENTICATED_USER : Literal["UNAUTHENTICATED_USER"] = "UNAUTHENTICATED_USER"

class User(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = Field(default=None, max_length=255)
    email: EmailStr
    emailVerified: Optional[datetime] = Field(default_factory=datetime.now)
    profilePic: Optional[str] = None
    password: Optional[str] = None
    role: Literal[UserRole.ADMIN, UserRole.USER] = Field(default=UserRole.USER) # type: ignore
    createdAt: Optional[datetime] = Field(default_factory=datetime.now)
    updatedAt: Optional[datetime] = Field(default_factory=datetime.now)