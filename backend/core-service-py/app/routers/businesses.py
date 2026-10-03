from fastapi import APIRouter, HTTPException, Query

from app.services import business_service

router = APIRouter()


@router.get("/businesses/search")
async def search(q: str = "", category: str | None = None):
    return business_service.search_businesses(q, category)


@router.get("/businesses/nearby")
async def nearby(
    lat: float = Query(..., ge=-90, le=90),
    lng: float = Query(..., ge=-180, le=180),
    radius: float = Query(5, gt=0, le=100),
):
    return business_service.nearby_businesses(lat, lng, radius)


@router.get("/businesses/{business_id}")
async def detail(business_id: str):
    b = business_service.get_business(business_id)
    if not b:
        raise HTTPException(status_code=404, detail="Business not found")
    return b