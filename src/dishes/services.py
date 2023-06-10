from src.database import database
from sqlalchemy import select, func
from src.dishes.models import dish


async def get_popular_cuisine():
    select_query = select([dish])

    results = await database.fetch_all(select_query)
    dishes = [
        {
            "id": r.id,
            "name": r.name,
            "descriptiion": r.description,
            "price": r.price,
            "rating_sum": r.rating_sum,
            "number_of_voters": r.number_of_voters,
        }
        for r in results
    ]

    dishes.sort(key=lambda x: (x["rating_sum"] / x["number_of_voters"]), reverse=True)
    return dishes[0:8]


async def get_dish(dish_name: str):
    select_query = select([dish]).where(
        func.lower(dish.c.name).contains(dish_name.lower())
    )

    result = await database.fetch_one(select_query)

    return {
        "id": result.id,
        "name": result.name,
        "description": result.description,
        "price": result.price,
        "rating_sum": result.rating_sum,
        "number_of_voters": result.number_of_voters,
    }


async def get_dishes(dish_name: str):
    select_query = select([dish]).where(
        func.lower(dish.c.name).contains(dish_name.lower())
    )

    results = await database.fetch_all(select_query)

    return [
        {
            "id": result.id,
            "name": result.name,
            "description": result.description,
            "price": result.price,
            "rating_sum": result.rating_sum,
            "number_of_voters": result.number_of_voters,
        }
        for result in results
    ]


async def get_region_dishes(region_name):
    select_query = select([dish]).where(dish.c.region == region_name)
    results = await database.fetch_all(select_query)
    return [
        {
            "id": r.id,
            "name": r.name,
            "descriptiion": r.description,
            "price": r.price,
            "region": r.region,
            "rating_sum": r.rating_sum,
            "number_of_voters": r.number_of_voters,
        }
        for r in results
    ]
