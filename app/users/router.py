from fastapi import APIRouter, HTTPException
from app.users.dao import UserDAO
from app.users.shemas import SUserRegister
from app.users.auth import get_password_hash

router = APIRouter(prefix="/auth", tags=["Авторизация"])


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)
