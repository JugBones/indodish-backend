from src.database import database
from sqlalchemy import select
from src.auth.schemas import JWTData
from src.cart.schemas import InsertDishToCart, RemoveDishFromCart, UpdateCartItem
from src.cart.models import cart
from src.dishes.models import dish


async def get_from_cart(jwt_data: JWTData):
    select_query = (
        select(cart)
        .where(cart.c.user_id == jwt_data.user_id)
        .join(dish)
        .filter(dish.c.id == cart.c.dish_id)
    )

    return await database.fetch_all(select_query)


async def upsert_to_cart(jwt_data: JWTData, dish_info: InsertDishToCart):
    transaction = await database.transaction()

    try:
        select_query = cart.select().where(
            cart.c.dish_id == dish_info.dish_id and cart.c.user_id == jwt_data.user_id
        )

        cart_item = await database.fetch_one(select_query)

        if cart_item is None:
            insert_query = cart.insert().values(
                {
                    "user_id": jwt_data.user_id,
                    "dish_id": dish_info.dish_id,
                    "quantity": dish_info.quantity,
                }
            )

            return await database.execute(insert_query)

        update_query = (
            cart.update()
            .where(
                cart.c.dish_id == dish_info.dish_id
                and cart.c.user_id == jwt_data.user_id
            )
            .values(
                {
                    "user_id": jwt_data.user_id,
                    "dish_id": dish_info.dish_id,
                    "quantity": dish_info.quantity,
                }
            )
        )

        return await database.execute(update_query)

    except Exception as e:
        await transaction.rollback()
        raise e

    else:
        await transaction.commit()


async def update_to_cart(jwt_data: JWTData, dish_info: UpdateCartItem):
    update_query = (
        cart.update()
        .where(
            cart.c.dish_id == dish_info.dish_id and cart.c.user_id == jwt_data.user_id
        )
        .values(
            {
                "user_id": jwt_data.user_id,
                "dish_id": dish_info.dish_id,
                "quantity": dish_info.quantity,
            }
        )
    )

    return await database.execute(update_query)


async def remove_from_cart(jwt_data: JWTData, dish_info: RemoveDishFromCart):
    delete_query = cart.delete().where(
        cart.c.dish_id == dish_info.dish_id and cart.c.user_id == jwt_data.user_id
    )

    return await database.execute(delete_query)
