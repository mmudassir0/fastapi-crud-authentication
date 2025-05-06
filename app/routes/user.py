from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated,List
from fastapi import Depends, HTTPException

from .. import schema ,auth,model
router=APIRouter()
from sqlmodel import Session,select
from ..db import get_session
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=schema.UserRead,tags=["authentication"])
def register(user: schema.UserCreate, db: Annotated[Session, Depends(get_session)]):
    # Check if user exists
    existing_user = db.exec(
        select(model.User).where(model.User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    hashed_password = auth.get_password_hash(user.password)
    db_user = model.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/me/", response_model=schema.UserRead, tags=["users"])
def read_users_me(current_user: Annotated[model.User, Depends(auth.get_current_user)]):
    """Get current user information"""
    return current_user

@router.get("/users/", response_model=List[schema.UserRead], tags=["users"])
def read_users(
    db: Annotated[Session, Depends(get_session)],
    current_user: Annotated[model.User, Depends(auth.get_current_user)],
    skip: int = 0, 
    limit: int = 100
):
    """Get all users (requires authentication)"""
    users = db.exec(select(model.User).offset(skip).limit(limit)).all()
    return users