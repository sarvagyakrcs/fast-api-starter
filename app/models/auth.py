from pydantic import BaseModel, EmailStr

class LoginCredentials(BaseModel):
    email: EmailStr
    password: str

class RegisterUser(BaseModel):
    name: str
    email: EmailStr
    password: str

class VerifyOTP(BaseModel):
    otp: str
    email: EmailStr