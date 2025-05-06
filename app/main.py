from fastapi import FastAPI
from .db import create_db_and_tables
from app.routes import user_router,auth_router,hero_router,item,team


app=FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(hero_router)
app.include_router(item)
app.include_router(team)