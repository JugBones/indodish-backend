import os
from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter(prefix="/images")


@router.get("/restaurant-image")
def get_restaurant_image(restaurant_name: str, size: int = None):
    if size is None:
        return FileResponse(
            os.path.join(
                "img",
                "restaurant_image",
                f"{''.join(restaurant_name.lower().split(' '))}.webp",
            )
        )

    return FileResponse(
        os.path.join(
            "img",
            "restaurant_image",
            f"{''.join(restaurant_name.lower().split(' '))}-{size}.webp",
        )
    )


@router.get("/dish-image")
def get_dish_image(dish_name: str, size: int = None):
    if size is None:
        return FileResponse(
            os.path.join(
                "img",
                "dishes_image",
                f"{''.join(dish_name.lower().split(' '))}-500.webp",  # noqa
            )
        )

    return FileResponse(
        os.path.join(
            "img",
            "dishes_image",
            f"{''.join(dish_name.lower().split(' '))}-{size}.webp",  # noqa
        )
    )
