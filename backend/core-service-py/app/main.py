import os
from app.routers import business_manage, businesses, me, scan
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import businesses

load_dotenv()

app = FastAPI(title="FoodLens Core Service", version="1.0.0")

origins = [
    o.strip()
    for o in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
    if o.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(businesses.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
app.include_router(me.router)
app.include_router(scan.router)
app.include_router(business_manage.router)
