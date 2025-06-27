from fastapi import FastAPI
from app.service.user_service import user
from app.models.user import User
app = FastAPI()

@app.get("/")
async def read_root():
    target_user = await user.get_user_by_email("thesarvagyakumar@gmail.com")
    if not target_user:
        return {"message": "User not found"}
    return {"user": target_user}

@app.post("/register")
async def register(recieved_user: User):
    return await user.create_user(recieved_user)