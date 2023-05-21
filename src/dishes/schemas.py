from pydantic import BaseModel
from enum import Enum


class DishCategory(Enum):
    SNACK = "snack"
    APPETIZER = "appetizer"
    MAIN_COURSE = "main_course"
    DESSERT = "dessert"
    BEVERAGE = "beverage"


class CreateDish(BaseModel):
    name: str
    description: str
    category: DishCategory
    rating_sum = 0
    number_of_voters = 0
