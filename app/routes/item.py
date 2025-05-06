from fastapi import APIRouter, Depends,HTTPException
from ..model import Item
from sqlmodel import Session,select
from typing import Annotated
from ..db import get_session
from ..schema import UserRead
from ..auth import get_current_user

router=APIRouter()
session=Annotated[Session,Depends(get_session)]
user_dep = Annotated[UserRead, Depends(get_current_user)]

@router.post("/items",tags=["items"])
def CreateItem(item:Item,session:session,user: user_dep):
    db_item=Item(**item.model_dump())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

@router.get("/items",tags=["items"])
def getItem(session:session,user: user_dep):
   items= session.exec(select(Item)).all()
#    filter
#    session.exec(select(Item).where(Item.name=="hello"))
   return items

@router.get("/items/{item_id}",tags=["items"])
def getById(item_id:int,session:session,user: user_dep):
    item=session.get(Item,item_id)
    if not item:
        raise HTTPException(status_code=404 ,detail="item not found")
    return item

@router.patch("/items/{item_id}",tags=["items"])
def updateItem(item_id:int,update_item:Item,session:session,user: user_dep):

    db_item=session.get(Item,item_id)
    if not db_item:
        raise HTTPException(status_code=404,detail='item not found')
    item_data=update_item.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(db_item, key, value)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.delete("/items/{item_id}",tags=["items"])
def deleteItem(item_id:int,session:session,user: user_dep):
    db_item=session.get(Item,item_id)
    if not db_item:
        raise HTTPException(status_code=404,detail="item not found")
    session.delete(db_item)
    session.commit()
    return {"message":"item deleted successfully"}