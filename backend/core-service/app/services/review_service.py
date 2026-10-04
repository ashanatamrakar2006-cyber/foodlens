from datetime import datetime, timezone

from app.mock.data import businesses, reviews


def create_review(user_id: str, data: dict):
    business = next((b for b in businesses if b["id"] == data["businessId"]), None)
    if not business:
        return None, "business_not_found"

    if any(r["userId"] == user_id and r["businessId"] == data["businessId"] for r in reviews):
        return None, "duplicate"

    review = {
        "id": str(len(reviews) + 1),
        "businessId": data["businessId"],
        "userId": user_id,
        "foodRating": data["foodRating"],
        "hygieneRating": data["hygieneRating"],
        "valueRating": data["valueRating"],
        "comment": data.get("comment") or "",
        "verified": False,  # bill verify hone par True hoga
        "response": None,
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }
    reviews.append(review)
    return review, None


def list_reviews(business_id: str):
    items = [r for r in reviews if r["businessId"] == business_id]
    return sorted(items, key=lambda r: r["createdAt"], reverse=True)


def respond_to_review(review_id: str, owner_id: str, text: str):
    review = next((r for r in reviews if r["id"] == review_id), None)
    if not review:
        return None, "review_not_found"

    business = next((b for b in businesses if b["id"] == review["businessId"]), None)
    if not business or business.get("ownerId") != owner_id:
        return None, "forbidden"

    review["response"] = {
        "text": text,
        "respondedAt": datetime.now(timezone.utc).isoformat(),
    }
    return review, None