# app/deps.py
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from app.schemas.db.db_session import DbSession

db_session = DbSession()
SessionDep = Annotated[Session, Depends(db_session.get_session)]
