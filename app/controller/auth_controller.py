from app.service.user_service import user_service
from app.models.user import User
from app.models.auth import RegisterUser
import asyncio
from jose import jwt, JWTError
from app.utils.load_env import env
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM
from datetime import datetime, timedelta
from fastapi import HTTPException, Response, Request
from pydantic import EmailStr
from app.models.auth import LoginCredentials
from app.utils.emails import email
from app.utils.security import generate_6_digit_code
from app.service.tokens_service import tokens_service
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

    '''
    This method is used to login a user
    '''
    async def login(self, credentials: LoginCredentials, res: Response) -> dict[str, str]:
        try:
            existing_user = await user_service.get_user_by_email(credentials.email);
            if not existing_user.emailVerified:
                otp = await tokens_service.generate_otp(existing_user)
                email.send_verification_email(existing_user.email, otp)
                raise HTTPException(status_code=401, detail="Email not verified, Sent a new verification email")
            
            if existing_user is None:
                raise HTTPException(status_code=401, detail="Invalid credentials")
            
            if not await user_service.check_password(credentials.password, existing_user.password):
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
        
    '''
    This Method is used to logout a user
    '''
    async def logout(self, res: Response) -> dict[str, str]:
        try:
            res.delete_cookie(key="x-auth-token")
            return {
                "message": "Logged out successfully"
            }
        except Exception as e:
            raise e
        
    '''
    This method is used to register a user
    '''
    async def register(self, recieved_user: RegisterUser) -> dict[str, str]:
        try:
            return await user_service.create_user(recieved_user)
        except Exception as e:
            raise e
        
    '''
    This method is used to verify a user's OTP
    '''
    async def verify_otp(self, otp: str, email: EmailStr) -> dict[str, str]:
        try:
            return await tokens_service.verify_otp(otp, email)
        except Exception as e:
            raise e

auth_controller = AuthController()        