from fastapi import APIRouter

from .endpoints import stocks

router = APIRouter()
router.include_router(stocks.V1, prefix="/stock", tags=["Stock"])