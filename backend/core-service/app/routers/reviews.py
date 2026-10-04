from app.services import notification_service
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from app.auth import require_role
from app.services import review_service as svc

router = APIRouter()


class ReviewCreate(BaseModel):
    businessId: str
    foodRating: int = Field(ge=1, le=5)
    hygieneRating: int = Field(ge=1, le=5)
    valueRating: int = Field(ge=1, le=5)
    comment: str | None = Field(default=None, max_length=1000)


class ReviewResponse(BaseModel):
    text: str = Field(min_length=2, max_length=1000)


@router.post("/reviews", status_code=201)
async def create(body: ReviewCreate, user: dict = Depends(require_role("consumer"))):
    review, err = svc.create_review(user["id"], body.model_dump())
    if err == "business_not_found":
        raise HTTPException(status_code=404, detail="Business not found")
    if err == "duplicate":
        raise HTTPException(status_code=409, detail="You already reviewed this business")
    return review


@router.get("/businesses/{business_id}/reviews")
async def list_for_business(business_id: str):
    return svc.list_reviews(business_id)


@router.post("/reviews/{review_id}/respond")
async def respond(review_id: str, body: ReviewResponse, user: dict = Depends(require_role("business"))):
    review, err = svc.respond_to_review(review_id, user["id"], body.text.strip())
    if err == "review_not_found":
        raise HTTPException(status_code=404, detail="Review not found")
    if err == "forbidden":
        raise HTTPException(status_code=403, detail="You do not own this business")

    notification_service.create_notification(
        review["userId"], "review_response", "A business responded to your review", review["id"]
    )
    return review