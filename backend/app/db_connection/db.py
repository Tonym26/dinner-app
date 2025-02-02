from sqlmodel import Session, SQLModel, create_engine
from fastapi import Depends
from typing import Annotated

DB_NAME = "temp.db"
DB_URL = f"sqlite:///{DB_NAME}"

connect_args = {"check_same_thread": False}
engine = create_engine(DB_URL, connect_args=connect_args)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]