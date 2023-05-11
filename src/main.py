from fastapi import FastAPI
from src.database import database, engine

from src.users.models import Base as user_models
from src.auth.models import Base as refresh_token_models

from src.auth.routers import router as auth_router

app = FastAPI(
    title="IndODish API",
    description="COMP6703001 - Web Application Development and Security Final Project",
    version="1.0.0",
)

app.include_router(auth_router)

user_models.metadata.create_all(bind=engine)
refresh_token_models.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
