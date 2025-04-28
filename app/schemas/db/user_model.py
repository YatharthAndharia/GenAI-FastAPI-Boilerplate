import datetime
from sqlalchemy import Column, String
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True,nullable=False)
    email: str | None = Field(sa_column=Column("email",String,unique=True,index=True))
    password: str=Field(min_length=5,nullable=False)
    created_at:datetime.datetime=Field(default=datetime.datetime.now(),nullable=False)
