from fastapi import FastAPI,Depends
from app.routes import api_router
from typing import Annotated
from sqlmodel import Session
from app.schemas.db.db_session import DbSession

db_session=DbSession()

app = FastAPI(
    title="EduAI",
    debug=False,
)

@app.on_event("startup")
def on_startup():
    db_session.create_db_and_tables()

app.include_router(api_router,prefix="")
