from src.database import database
from sqlalchemy import select
from src.auth.schemas import JWTData
from src.cart.schemas import InsertDishToCart, RemoveDishFromCart, UpdateCartItem
from src.cart.models import cart
from src.dishes.models import dish


async def get_from_cart(jwt_data: JWTData):
    select_query = (
        select([cart, dish]).join(dish).filter(cart.c.user_id == jwt_data.user_id)
    )

    results = await database.fetch_all(select_query)

    return [
        {
            "id": r.id,
            "name": r.name,
            "quantity": r.quantity,
            "price": r.price,
        }
        for r in results
    ]


async def insert_to_cart(jwt_data: JWTData, dish_info: InsertDishToCart):
    insert_query = cart.insert().values(
        {
            "user_id": jwt_data.user_id,
            "dish_id": dish_info.dish_id,
            "quantity": dish_info.quantity,
        }
    )

    return await database.execute(insert_query)


async def update_to_cart(jwt_data: JWTData, dish_info: UpdateCartItem):
    update_query = (
        cart.update()
        .where(cart.c.id == dish_info.cart_item_id)
        .values(
            {
                "quantity": dish_info.quantity,
            }
        )
    )

    return await database.execute(update_query)


async def remove_from_cart(jwt_data: JWTData, dish_info: RemoveDishFromCart):
    delete_query = cart.delete().where(cart.c.id == dish_info.cart_item_id)

    return await database.execute(delete_query)
