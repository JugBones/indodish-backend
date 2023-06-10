from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from src.config import settings
from src.database import database, metadata, engine
import os

from src.auth.routers import router as auth_router
from src.users.routers import router as users_router
from src.contact_form.routers import router as contact_form_router
from src.restaurants.routers import router as restaurant_router
from src.cart.routers import router as cart_router
from src.restaurant_image.routers import router as restaurant_image_router
from src.images.routers import router as images_router
from src.dishes.routers import router as dish_router

app = FastAPI(
    title="IndODish API",
    description="COMP6703001 - Web Application Development and Security (Final Project)",  # noqa: line to long - Flake8(E501)
    version="1.0.0",
)

metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


app.include_router(auth_router)
app.include_router(restaurant_router)
app.include_router(users_router)
app.include_router(cart_router)
app.include_router(contact_form_router)
app.include_router(restaurant_image_router)
app.include_router(images_router)
app.include_router(dish_router)


@app.get("/", tags=["health"])
def health():
    return {
        "title": "IndODish API",
        "description": "COMP6703001 - Web Application Development and Security (Final Project)",  # noqa: line to long - Flake8(E501)
        "version": "1.0.0",
    }


@app.get("/test")
def get_img():
    return FileResponse(os.path.join("img", "restaurant_image", "ayamsuharti-200.webp"))


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
