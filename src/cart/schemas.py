from pydantic import BaseModel


class InsertDishToCart(BaseModel):
    dish_id: str
    quantity: int


class RemoveDishFromCart(BaseModel):
    cart_item_id: str


class UpdateCartItem(BaseModel):
    cart_item_id: str
    quantity: int
