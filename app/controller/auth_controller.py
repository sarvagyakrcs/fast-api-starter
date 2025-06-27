from app.service.user_service import user_service
from app.models.user import User
import asyncio
from jose import jwt, JWTError
from app.utils.load_env import env
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM
from datetime import datetime, timedelta
from fastapi import HTTPException, Response
from pydantic import EmailStr
from app.models.auth import LoginCredentials

'''
This class is used to handle the authentication and authorization of the user.
Methods:
- register: Register a new user
- login: Login a user
- update_password: Update the user's password
'''
class AuthController:
    def __init__(self):
        pass

    async def login(self, credentials: LoginCredentials, res: Response) -> dict[str, str]:
        try:
            existing_user = await user_service.get_user_by_email(credentials.email);

            if existing_user is None:
                raise HTTPException(status_code=401, detail="Invalid credentials")
            
            if not user_service.check_password(credentials.password, existing_user.password):
                raise HTTPException(status_code=401, detail="Invalid credentials")
            
            expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            jwt_payload = {
                "id": existing_user.id,
                "role" : existing_user.role,
                "email" : existing_user.email,
                "name" : existing_user.name,
                "profilePic" : existing_user.profilePic,
                "exp": int(expires_delta.timestamp())
            }
            jwt_token = jwt.encode(jwt_payload, env.get_env_variable("AUTH_SECRET"), algorithm=ALGORITHM)
            res.set_cookie(key="x-auth-token", value=jwt_token)
            return {
                "message": "Logged in successfully"
            }
        except Exception as e:
            raise e

auth_controller = AuthController()        