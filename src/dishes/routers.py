from fastapi import APIRouter
from src.dishes import services

router = APIRouter(prefix="/dishes", tags=["dishes"])


@router.get("/popular-cuisine")
async def get_popular_cuisine():
    return await services.get_popular_cuisine()


@router.get("/restaurant")
async def get_restaurant_dishes():
    pass
