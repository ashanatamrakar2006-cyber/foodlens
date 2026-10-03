from typing import Literal

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from app.auth import require_role
from app.services import business_manage_service as svc

router = APIRouter()

Category = Literal["restaurant", "cafe", "street_food", "shop", "other"]


class BusinessCreate(BaseModel):
    name: str = Field(min_length=2)
    category: Category
    lat: float = Field(ge=-90, le=90)
    lng: float = Field(ge=-180, le=180)


class BusinessUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2)
    category: Category | None = None
    lat: float | None = Field(default=None, ge=-90, le=90)
    lng: float | None = Field(default=None, ge=-180, le=180)


only_business = Depends(require_role("business"))


@router.post("/businesses", status_code=201)
async def register(body: BusinessCreate, user: dict = only_business):
    return svc.create_business(user["id"], body.model_dump())


@router.post("/businesses/{business_id}/claim")
async def claim(business_id: str, user: dict = only_business):
    business, err = svc.claim_business(business_id, user["id"])
    if err == "not_found":
        raise HTTPException(status_code=404, detail="Business not found")
    if err == "already_claimed":
        raise HTTPException(status_code=409, detail="Business already claimed by another owner")
    return business


@router.patch("/businesses/{business_id}")
async def update(business_id: str, body: BusinessUpdate, user: dict = only_business):
    fields = body.model_dump(exclude_none=True)
    business, err = svc.update_business(business_id, user["id"], fields)
    if err == "not_found":
        raise HTTPException(status_code=404, detail="Business not found")
    if err == "forbidden":
        raise HTTPException(status_code=403, detail="You do not own this business")
    return business


@router.get("/business/dashboard")
async def dashboard(user: dict = only_business):
    owned = svc.get_owned_businesses(user["id"])
    return {"businesses": owned, "count": len(owned)}