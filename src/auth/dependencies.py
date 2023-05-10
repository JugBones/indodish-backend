from src.auth import services
from src.auth.schemas import NewUser
from src.auth.exceptions import EmailTaken


async def valid_user_create(new_user: NewUser):
    if await services.get_user_by_email(new_user.email):
        raise EmailTaken()

    return new_user
