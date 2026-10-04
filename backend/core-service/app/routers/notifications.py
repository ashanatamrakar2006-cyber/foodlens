from fastapi import APIRouter, Depends, HTTPException

from app.auth import get_current_user
from app.services import notification_service as svc

router = APIRouter()


@router.get("/notifications")
async def list_all(user: dict = Depends(get_current_user)):
    items = svc.list_notifications(user["id"])
    return {"notifications": items, "unread": len([n for n in items if not n["read"]])}


@router.patch("/notifications/{notification_id}/read")
async def read(notification_id: str, user: dict = Depends(get_current_user)):
    n, err = svc.mark_read(notification_id, user["id"])
    if err == "not_found":
        raise HTTPException(status_code=404, detail="Notification not found")
    if err == "forbidden":
        raise HTTPException(status_code=403, detail="Not your notification")
    return n