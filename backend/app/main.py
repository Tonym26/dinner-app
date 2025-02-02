from fastapi import FastAPI

from .routers import recipe
from .db_connection import db

db.create_db()

app = FastAPI()

app.include_router(recipe.router)
