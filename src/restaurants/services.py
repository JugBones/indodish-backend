from sqlalchemy import select
from src.database import database
from src.address.models import address
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
            "latitude": r.latitude,
            "longitude": r.longitude,
        }
        for r in restaurants
    ]
