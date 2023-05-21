from pydantic import BaseModel


class InsertDishToCart(BaseModel):
    dish_id: str
    quantity: str


class RemoveDishFromCart(BaseModel):
    dish_id: str


class UpdateCartItem(BaseModel):
    cart_item_id: str
    quantity: int
