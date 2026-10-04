from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from app.auth import require_role
from app.services import product_service as svc

router = APIRouter()


class ProductCreate(BaseModel):
    barcode: str = Field(pattern=r"^\d{8,14}$")
    name: str = Field(min_length=2)
    brand: str | None = None
    ingredients: str | None = None
    allergens: list[str] | None = None


@router.get("/products/{product_id}")
async def get_one(product_id: str):
    p = svc.get_product(product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return p


@router.post("/products", status_code=201)
async def create(body: ProductCreate, user: dict = Depends(require_role("business"))):
    product, err = svc.create_product(user["id"], body.model_dump())
    if err == "duplicate_barcode":
        raise HTTPException(status_code=409, detail="Product with this barcode already exists")
    return product


@router.get("/products/{product_id}/batches")
async def get_batches(product_id: str):
    items = svc.list_batches(product_id)
    if items is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return items