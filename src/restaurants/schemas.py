from pydantic import BaseModel


class CreateRestaurant(BaseModel):
    name: str
    description: str
    phone_number: str
    latitude: float
    longitude: float


class RestaurantToDB(BaseModel):
    name: str
    description: str
    phone_number: str
    user_id: str
    rating_sum = 0
    number_of_voters = 0
