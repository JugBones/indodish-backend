from pydantic import BaseModel


class UserProfileUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
