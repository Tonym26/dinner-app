import json

from fastapi import APIRouter, Query
from sqlmodel import select
from typing import Annotated

from ..db_connection import db
from ..models import models


router = APIRouter()

@router.get("/")
def root():
    """
    Returns a list of all recipes
    """
    return {"message": "Welcome to the Dinner App"}

@router.get("/recipes")
def get_recipes(session: db.SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[models.Recipe]:
    query = select(models.Recipe).offset(offset).limit(limit)
    response = session.exec(query)
    return response

@router.get("/plan")
def create_plan(days: int):
    """
    Create a meal plan for a given number of days.
    Returns a shopping list of needed ingredients.
    """
    return days

@router.post("/recipes")
def create_recipe(recipe: models.Recipe, session: db.SessionDep) -> models.Recipe:
    """
    Add a recipe to the database
    """
    data = json.loads(recipe.model_dump_json())

    new_recipe = models.Recipe(name=data["name"], ingredients=data["ingredients"])
    session.add(new_recipe)
    session.commit()
    session.refresh(new_recipe)
    return {"message": f"Recipe: {recipe.name} created"}
