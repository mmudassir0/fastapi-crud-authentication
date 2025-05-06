from fastapi import APIRouter, Depends, HTTPException,Header
from typing import Annotated
from sqlmodel import Session, select
from ..model import Hero,Team
from ..db import get_session
from ..schema import HeroCreate, HeroRead,UserRead
from ..auth import get_current_user

user_dep = Annotated[UserRead, Depends(get_current_user)]
session_dep= Annotated[Session, Depends(get_session)] 

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# router=APIRouter()
router = APIRouter(
    prefix="/heroes",
    tags=["heroes"],
dependencies=[],
    responses={404: {"description": "Not found"}},
)

# CREATE - POST /heroes/
@router.post("/", response_model=HeroRead,tags=["heroes"])
def create_hero(hero: HeroCreate,user:user_dep, session: session_dep):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

# READ ALL - GET /heroes/
@router.get("/",tags=["heroes"])
def read_heroes(user:user_dep,session: session_dep):
    result=session.exec(select(Hero).where(Hero.name=="string"))
    # results = session.exec(select(Hero,Team).outerjoin(Team)).all()
    # heroes = [{"hero": hero, "team": team} for hero, team in results]
    # print(heroes)
    hero_string= result.one()
    statement=session.exec(select(Team).where(Team.id==hero_string.team_id))
    team=statement.first()
    return {"hero":hero_string,"team":team}

# READ ONE - GET /heroes/{hero_id}
@router.get("/{hero_id}", response_model=HeroRead,tags=["heroes"])
def read_hero(hero_id: int,user:user_dep, session: session_dep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

# UPDATE - PATCH /heroes/{hero_id}
@router.patch("/{hero_id}", response_model=HeroRead,tags=["heroes"])
def update_hero(
    hero_id: int, 
    hero_update: HeroCreate,
    user:user_dep, 
    session: session_dep
):
    db_hero = session.get(Hero, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    hero_data = hero_update.dict(exclude_unset=True)
    for key, value in hero_data.items():
        setattr(db_hero, key, value)
    
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

# DELETE - DELETE /heroes/{hero_id}
@router.delete("/{hero_id}",tags=["heroes"])
def delete_hero(hero_id: int,user:user_dep, session: session_dep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    session.delete(hero)
    session.commit()
    return {"message": "Hero deleted successfully"}