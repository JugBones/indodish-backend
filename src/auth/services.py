from src.database import database
from sqlalchemy import insert, select
from src.auth.schemas import NewUser
from src.auth.security import hash_password
from src.users.models import User
from databases.interfaces import Record


async def create_user(new_user: NewUser) -> Record | None:
    insert_query = (
        insert(User)
        .values(
            {
                "first_name": new_user.first_name,
                "last_name": new_user.last_name,
                "email": new_user.email,
                "hashed_password": hash_password(new_user.password),
            }
        )
        .returning(User)
    )

    return await database.fetch_one(insert_query)


async def get_user_by_email(email: str) -> Record | None:
    select_query = select(User).where(User.email == email)

    return await database.fetch_one(select_query)
