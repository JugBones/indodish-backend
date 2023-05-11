from fastapi import FastAPI
from src.database import database, metadata, engine

from src.auth.routers import router as auth_router

app = FastAPI(
    title="IndODish API",
    description="COMP6703001 - Web Application Development and Security Final Project",
    version="1.0.0",
)

metadata.create_all(bind=engine)

app.include_router(auth_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
