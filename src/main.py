from fastapi import FastAPI
from src.database import database, metadata, engine

from src.auth.routers import router as auth_router
from src.users.routers import router as users_router
from src.contact_form.routers import router as contact_form_router

app = FastAPI(
    title="IndODish API",
    description="COMP6703001 - Web Application Development and Security (Final Project)",  # noqa: line to long - Flake8(E501)
    version="1.0.0",
)

metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(contact_form_router)


@app.get("/")
def root():
    return {
        "title": "IndODish API",
        "description": "COMP6703001 - Web Application Development and Security (Final Project)",  # noqa: line to long - Flake8(E501)
        "version": "1.0.0",
    }


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
