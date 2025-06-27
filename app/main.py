from fastapi import FastAPI
from app.service.user_service import user_service
from app.models.user import User
from app.utils.prisma import prisma
from app.routes.auth import router as auth_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

@app.get("/")
async def read_root():
    target_user = await user_service.get_user_by_email("thesarvagyakumar@gmail.com")
    if not target_user:
        return {"message": "User not found"}
    return {"user": target_user}

@app.post("/register")
async def register(recieved_user: User):
    return await user_service.create_user(recieved_user)

app.include_router(auth_router)