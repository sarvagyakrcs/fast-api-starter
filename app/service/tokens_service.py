import random
import string
from app.models.user import User
from app.utils.prisma import prisma
from datetime import datetime, timedelta, timezone
from app.core.config import OTP_EXPIRE_MINUTES
from fastapi import HTTPException

class TokensService:
    def __init__(self):
        pass

    async def generate_otp(self, user : User, digits: int = 6):
        try:
            otp = ''.join(random.choices(string.digits, k=digits))
            await prisma.otp.create(
            data={
                "email": user.email,
                "otp": otp,
                "expiresAt": datetime.now(timezone.utc) + timedelta(minutes=OTP_EXPIRE_MINUTES)
                }   
            )
            return otp
        except Exception as e:
            raise e

    async def verify_otp(self, otp: str, email: str):
        try:
            otp_record = await prisma.otp.find_unique(
                where={
                    "email_otp": {
                        "email": email,
                        "otp": otp
                    }
                }
            )
            if not otp_record:
                raise HTTPException(status_code=400, detail="Invalid OTP")
            if otp_record.expiresAt < datetime.now(timezone.utc):
                raise HTTPException(status_code=400, detail="OTP expired")
            
            # Mark user as verified and delete the OTP
            await prisma.user.update(
                where={"email": email},
                data={"emailVerified": datetime.now(timezone.utc)}
            )
            
            await prisma.otp.delete(
                where={
                    "email_otp": {
                        "email": email,
                        "otp": otp
                    }
                }
            )
            
            return {"message": "Email verified successfully"}
        except Exception as e:
            raise e
        
tokens_service = TokensService()