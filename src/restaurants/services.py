from sqlalchemy import insert
from src.database import database
from src.address.models import address
from src.users.models import user
from src.restaurants.models import restaurant
from src.restaurants.schemas import CreateRestaurant
from geopy.geocoders import Nominatim
from src.config import settings
from src.auth.schemas import JWTData
from src.dishes.models import dish
from src.dishes.schemas import CreateDish


async def create_restaurant(restaurant_info: CreateRestaurant, jwt_data: JWTData):
    geolocation = Nominatim(user_agent=settings.GEOPY_USER_AGENT)
    location = geolocation.reverse(
        (restaurant_info.latitude, restaurant_info.longitude)
    )

    transaction = await database.transaction()

    try:
        insert_address_query = (
            insert(address)
            .values(
                {
                    "description": restaurant_info.name,
                    "street_address": location.address,
                    "country": location._raw["address"]["country"],
                    "city": location._raw["address"]["city"],
                    "city_district": location._raw["address"]["city_district"],
                    "postal_code": location._raw["address"]["postcode"],
                    "longitude": eval(location._raw["lon"]),
                    "latitude": eval(location._raw["lat"]),
                }
            )
            .returning(address.c.id)
        )

        restaurant_address = await database.fetch_one(insert_address_query)

        insert_restaurant_query = (
            insert(restaurant)
            .values(
                {
                    "name": restaurant_info.name,
                    "description": restaurant_info.description,
                    "user_id": jwt_data.user_id,
                    "phone_number": restaurant_info.phone_number,
                    "address_id": restaurant_address.id,
                    "rating_sum": 0,
                    "number_of_voters": 0,
                }
            )
            .returning(restaurant.c.id)
        )

        restaurant_id = await database.fetch_one(insert_restaurant_query)

        update_user_query = (
            user.update()
            .where(user.c.id == jwt_data.user_id)
            .values({"restaurant_id": restaurant_id})
        )

        await database.fetch_one(update_user_query)

    except Exception as e:
        await transaction.rollback()
        raise e
    else:
        await transaction.commit()

        return restaurant_id


async def insert_restaurant_menu(dish_info: CreateDish, restaurant_id: str):
    insert_query = (
        insert(dish)
        .values(
            {
                "name": dish_info.name,
                "description": dish_info.description,
                "restaurant_id": restaurant_id,
                "category": dish_info.category.value,
                "rating_sum": dish_info.rating_sum,
                "number_of_voters": dish_info.number_of_voters,
            }
        )
        .returning(dish.c.id)
    )

    return await database.fetch_one(insert_query)
