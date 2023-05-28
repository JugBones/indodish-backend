from wand.image import Image
import os

img_dir = os.path.join("img", "restaurant_image")

img_file_with_ext = os.listdir(img_dir)
img_file = [i.split(".")[0] for i in os.listdir(img_dir)]

for image_ext, image in zip(img_file_with_ext, img_file):
    with open(f"{os.path.join(img_dir, image_ext)}", "rb") as f:
        with Image(blob=f.read()) as img:
            for index, size in enumerate([500, 300, 200]):
                print(os.path.join(img_dir, f"{image}-w{size}-h{size}.webp"))
                with img.clone() as i:
                    i.transform(resize="%dx%d>" % (size, size))
                    i.save(
                        filename=f"{os.path.join(img_dir, f'{image}-{size}.webp')}"  # noqa
                    )
