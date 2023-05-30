from sqlalchemy import select, func
from src.database import database
from src.address.models import address
from src.dishes.models import dish
from src.restaurants.models import restaurant


async def get_nearby_restaurants(latitude: float, longitude: float):
    select_query = select([restaurant, address]).join(
        address, restaurant.c.address_id == address.c.id
    )

    restaurants = await database.fetch_all(select_query)

    return [
        {
            "id": r.id,
            "name": r.name,
            "rating_sum": r.rating_sum,
            "number_of_voters": r.number_of_voters,
        }
        for r in restaurants
    ]


async def get_restaurant(restaurant_name: str):
    select_restaurant_query = (
        select([restaurant, address])
        .where(func.lower(restaurant.c.name).contains(restaurant_name.lower()))
        .join(address, restaurant.c.address_id == address.c.id)
    )

    restaurant_result = await database.fetch_one(select_restaurant_query)

    if restaurant_result is None:
        raise ValueError()

    select_dish_query = select([dish]).where(
        dish.c.restaurant_id == restaurant_result.id
    )

    dish_result = await database.fetch_all(select_dish_query)

    return {
        "name": restaurant_result.name,
        "description": restaurant_result.description,
        "address": restaurant_result.street_address,
        "menu": [
            {
                "id": d.id,
                "name": d.name,
                "description": d.description,
                "price": d.price,
                "category": d.category,
            }
            for d in dish_result
        ],
    }
