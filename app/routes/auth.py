from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel, EmailStr
from app.models.auth import LoginCredentials
from app.controller.auth_controller import auth_controller
from app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

'''
This route is used to login a user
'''
@router.post("/login")
async def login(credentials: LoginCredentials, res: Response):
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
async def logout(req: Request, res: Response):
    cookies = req.cookies
    if cookies.get("x-auth-token"):
        return await auth_controller.logout(res)
    else:
        raise HTTPException(status_code=400, detail="You are not logged in")
    try:
        return await auth_controller.logout(res)
    except Exception as e:
        error_message = e.detail if hasattr(e, "detail") else "Something went wrong while logging you out"
        raise HTTPException(status_code=400, detail=error_message)

'''
This route is used to register a user
'''
@router.post("/register")
async def register(recieved_user: User):
    try:
        return await auth_controller.register(recieved_user)
    except Exception as e:
        error_message = e.detail if hasattr(e, "detail") else "Something went wrong while registering you"
        raise HTTPException(status_code=400, detail=error_message)


    