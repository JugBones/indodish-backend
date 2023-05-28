import os
from wand.image import Image
from sqlalchemy import insert
from src.database import database
from src.images.models import image as image_model
from uuid import uuid4


async def insert_image(image: bytes):
    id = uuid4()
    img_path = os.path.join("img", "restaurant_image", f"{id}")

    images = []

    with Image(blob=image) as img:
        for index, size in enumerate([500, 350, 250]):
            with img.clone() as i:
                i.resize(int(size), int(size))
                i.save(filename=f"{img_path}-w{size}-h{size}.webp")
                img_id = await database.execute(
                    insert(image_model)
                    .values(
                        {
                            "url": f"{img_path}-w{size}-h{size}.webp",
                            "alt": str(id),
                            "width": size,
                            "height": size,
                        }
                    )
                    .returning(image_model.c.id)
                )
                images.append(img_id)

    return images
