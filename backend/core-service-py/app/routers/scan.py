import re

import httpx
from fastapi import APIRouter, HTTPException

from app.services import scan_service

router = APIRouter()


@router.get("/scan/barcode/{code}")
async def scan_barcode(code: str):
    if not re.fullmatch(r"\d{8,14}", code):
        raise HTTPException(status_code=400, detail="Barcode must be 8 to 14 digits")

    try:
        product = await scan_service.lookup_barcode(code)
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Product lookup service unavailable")

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product