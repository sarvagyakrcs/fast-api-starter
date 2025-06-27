from app.models.user import User
import asyncio
from app.utils.prisma import prisma
from typing import Optional

class UserService:
    def __init__(self):
        pass

    async def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            await prisma.connect()
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
                    emailVerified=user.emailVerified,
                    profilePic=user.profilePic,
                    role=user.role,
                )
            return None
        except Exception as e:
            raise e
        finally:
            await prisma.disconnect()

    async def create_user(self, user: User) -> User:
        try:
            await prisma.connect()
            return await prisma.user.create(
                data={
                    "email": user.email,
                    "password": user.password,
                    "name": user.name,
                    "role": user.role,
                    "emailVerified": user.emailVerified,
                }
            )
        except Exception as e:
            raise e
        finally:
            await prisma.disconnect()

user = UserService()