from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from typing_extensions import Literal
from datetime import datetime

class User(BaseModel):
    name: Optional[str] = Field(default=None, max_length=255)
    email: EmailStr
    emailVerified: datetime = Field(default_factory=datetime.now)
    profilePic: Optional[str] = None
    password: Optional[str] = None
    role: Literal["ADMIN", "USER"] = "USER"
    createdAt: datetime = Field(default_factory=datetime.now)
    updatedAt: datetime = Field(default_factory=datetime.now)