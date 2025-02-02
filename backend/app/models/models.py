from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Ingredient(BaseModel):
    name: str
    quantity: str

class Recipe(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    name: str = Field(index = True)
    ingredients: str = Field(index = True)

class ShoppingList(BaseModel):
    ingredients: dict[str, Ingredient]
