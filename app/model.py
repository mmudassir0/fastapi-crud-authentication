from sqlmodel import SQLModel, Field,Relationship
from typing import Annotated


class User(SQLModel,table=True):
    id: int|None = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    
class Team(SQLModel,table=True):
    id: int | None = Field(default=None, primary_key=True)
    name:str= Field(index=True)
    headquater:str
    heroes:list["Hero"]=Relationship(back_populates="team")

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team:Team | None = Relationship(back_populates="heroes")


class Item(SQLModel,table=True):
    id:Annotated[int |None,Field(default=None,primary_key=True)]
    name:str
    description:str