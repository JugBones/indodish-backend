from databases.interfaces import Record

from src.users.models import user
from src.database import database
from src.users.schemas import UserProfileUpdate


async def update_user_profile(user_id: str, user_profile: UserProfileUpdate) -> Record:
    update_query = (
        user.update()
        .value(
            {
                "first_name": user_profile.first_name,
                "last_name": user_profile.last_name,
                "email": user_profile.email,
                "phone_number": user_profile.phone_number,
            }
        )
        .where(user.c.id == user_id)
    )
    return await database.fetch_one(update_query)


async def update_user_password(user_id: str) -> None:
    pass
