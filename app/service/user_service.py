from app.models.user import User
from app.models.auth import RegisterUser
import asyncio
from app.utils.prisma import prisma
from typing import Optional
from fastapi import HTTPException
import bcrypt

class UserService:
    def __init__(self):
        pass

    async def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            user = await prisma.user.find_unique(
                where={
                    "email": email
                }
            )
            if user:
                return User(
                    id=user.id,
                    email=user.email,
                    name=user.name,
                    emailVerified=user.emailVerified or None,
                    profilePic=user.profilePic,
                    role=user.role,
                    password=user.password
                )
            return None
        except Exception as e:
            raise e

    async def create_user(self, user: RegisterUser) -> User:
        try:
            existing_user = await self.get_user_by_email(user.email)

            if existing_user is not None:
                raise HTTPException(status_code=400, detail="User already exists")
            
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt)

            created_user = await prisma.user.create(
                data={
                    "email": user.email,
                    "password": hashed_password.decode('utf-8'),
                    "name": user.name,
                }
            )

            return User(
                id=created_user.id,
                email=created_user.email,
                name=created_user.name,
                emailVerified=created_user.emailVerified,
                profilePic=created_user.profilePic,
                role=created_user.role,
                password=created_user.password
            )
        except Exception as e:
            raise e

    async def update_name(self, user_id: str, name: str) -> User:
        try:
            updated_user = await prisma.user.update(
                where={
                    "id": user_id
                },
                data={
                    "name": name
                }
            )
            return User(
                email=updated_user.email,
                name=updated_user.name,
                emailVerified=updated_user.emailVerified,
                profilePic=updated_user.profilePic,
                role=updated_user.role,
                password=updated_user.password
            )
        except Exception as e:
            raise e
        
    async def update_profile_pic(self, user_id: str, profile_pic: str) -> User:
        try:
            updated_user = await prisma.user.update(
                where={
                    "id": user_id
                },
                data={
                    "profilePic": profile_pic
                }
            )
            return User(
                email=updated_user.email,
                name=updated_user.name,
                emailVerified=updated_user.emailVerified,
                profilePic=updated_user.profilePic,
                role=updated_user.role,
                password=updated_user.password
            )
        except Exception as e:  
            raise e
        
    async def check_password(self, entered_password: str, hashed_password: str) -> bool:
        try:
            return bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password.encode('utf-8'))
        except Exception as e:
            raise e

        
user_service = UserService()