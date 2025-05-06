from fastapi import APIRouter,Depends
from sqlmodel import Session
from typing import Annotated
from ..db import get_session
from ..schema import TeamCreate
from ..model import Team

router=APIRouter()
session=Annotated[Session,Depends(get_session)]

@router.post("/",tags=["teams"])
def create_Team(team:TeamCreate ,db:session):
    db_dict=Team(**team.model_dump())
    db.add(db_dict)
    db.commit()
    db.refresh(db_dict)
    return db_dict