from fastapi import APIRouter
from src.restaurants import services
import urllib

router = APIRouter(prefix="/restaurants", tags=["restaurants"])


@router.get("/nearby-restaurants")
async def get_nearby_restaurants(latitude: float = None, longitude: float = None):
    return await services.get_nearby_restaurants(latitude, longitude)


@router.get("/{restaurant_name}")
async def get_restaurant_by_name(restaurant_name: str):
    return await services.get_restaurant(urllib.parse.unquote(restaurant_name))


@router.get("/search/{restaurant_name}")
async def get_restaurants_by_name(restaurant_name: str):
    return await services.get_restaurants(urllib.parse.unquote(restaurant_name))
