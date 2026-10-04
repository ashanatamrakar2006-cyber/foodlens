from datetime import datetime, timezone

from app.mock.data import notifications


def create_notification(user_id: str, type_: str, message: str, ref_id: str | None = None):
    n = {
        "id": str(len(notifications) + 1),
        "userId": user_id,
        "type": type_,
        "message": message,
        "refId": ref_id,
        "read": False,
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }
    notifications.append(n)
    return n


def list_notifications(user_id: str):
    items = [n for n in notifications if n["userId"] == user_id]
    return sorted(items, key=lambda n: n["createdAt"], reverse=True)


def mark_read(notification_id: str, user_id: str):
    n = next((x for x in notifications if x["id"] == notification_id), None)
    if not n:
        return None, "not_found"
    if n["userId"] != user_id:
        return None, "forbidden"
    n["read"] = True
    return n, None