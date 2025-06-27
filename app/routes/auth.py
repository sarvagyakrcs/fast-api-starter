from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel, EmailStr
from app.models.auth import LoginCredentials
from app.controller.auth_controller import auth_controller

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
async def login(credentials: LoginCredentials, res: Response):
    try:
        return await auth_controller.login(credentials, res)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Something went wrong while logging you in")


    