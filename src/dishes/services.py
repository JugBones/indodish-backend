from src.database import database
from sqlalchemy import select
from src.dishes.models import dish


async def get_popular_cuisine():
    select_query = select([dish]).order_by(dish.c.rating_sum / dish.c.number_of_voters)

    results = await database.fetch_all(select_query)
    return [
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
