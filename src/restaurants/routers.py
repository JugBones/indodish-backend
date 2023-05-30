from fastapi import APIRouter
from src.restaurants import services

router = APIRouter(prefix="/restaurants", tags=["restaurants"])


@router.get("/nearby-restaurants")
async def get_nearby_restaurants(latitude: float = None, longitude: float = None):
    return await services.get_nearby_restaurants(latitude, longitude)


@router.get("/{restaurant_name}")
async def get_restaurant_by_name(restaurant_name: str):
    return await services.get_restaurant(restaurant_name)
