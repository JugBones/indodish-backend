from fastapi import APIRouter
from src.dishes import services
import urllib.parse

router = APIRouter(prefix="/dishes", tags=["dishes"])


@router.get("/popular-cuisine")
async def get_popular_cuisine():
    return await services.get_popular_cuisine()


@router.get("/{dish_name}")
async def get_dish(dish_name: str):
    return await services.get_dish(urllib.parse.unquote(dish_name))


@router.get("/search/{dish_name}")
async def get_dishes(dish_name: str):
    return await services.get_dishes(urllib.parse.unquote(dish_name))


@router.get("/region/{region_name}")
async def get_region_dishes(region_name: str):
    return await services.get_region_dishes(region_name)
