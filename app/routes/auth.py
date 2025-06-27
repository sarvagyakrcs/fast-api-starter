from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel, EmailStr
from app.models.auth import LoginCredentials
from app.controller.auth_controller import auth_controller
from app.models.auth import RegisterUser, VerifyOTP

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

'''
This route is used to login a user
'''
@router.post("/login")
async def login(credentials: LoginCredentials, req: Request, res: Response):
    cookies = req.cookies
    if cookies.get("x-auth-token"):
        raise HTTPException(status_code=400, detail="You are already logged in")
    try:
        return await auth_controller.login(credentials, res)
    except Exception as e:
        print(e)
        error_message = e.detail if hasattr(e, "detail") else "Something went wrong while logging you in"
        raise HTTPException(status_code=400, detail=error_message)

'''
This route is used to logout a user
'''
@router.get("/logout")
async def logout(res: Response):
    try:
        return await auth_controller.logout(res)
    except Exception as e:
        error_message = e.detail if hasattr(e, "detail") else "Something went wrong while logging you out"
        raise HTTPException(status_code=400, detail=error_message)

'''
This route is used to register a user
'''
@router.post("/register")
async def register(recieved_user: RegisterUser):
    try:
        return await auth_controller.register(recieved_user)
    except Exception as e:
        error_message = e.detail if hasattr(e, "detail") else "Something went wrong while registering you"
        raise HTTPException(status_code=400, detail=error_message)

'''
This route is used to verify a user's OTP
'''
@router.post("/verify-otp")
async def verify_otp(verify_otp: VerifyOTP):
    try:
        return await auth_controller.verify_otp(verify_otp.otp, verify_otp.email)
    except Exception as e:
        print(e)
        error_message = e.detail if hasattr(e, "detail") else "Something went wrong while verifying your OTP"
        raise HTTPException(status_code=400, detail=error_message)
    
    