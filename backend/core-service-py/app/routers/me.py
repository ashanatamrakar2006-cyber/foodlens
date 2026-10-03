from fastapi import APIRouter, Depends

from app.auth import get_current_user

router = APIRouter()


@router.get("/me")
async def me(user: dict = Depends(get_current_user)):
    return user