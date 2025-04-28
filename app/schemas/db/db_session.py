import os
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from app.schemas.db.user_model import User
from dotenv import load_dotenv
load_dotenv()

class DbSession():
    def __init__(
            self,
            db_host:Optional[str]=None,
            db_port:Optional[int]="5432",
            db_name:Optional[str]=None,
            db_user:Optional[str]=None,
            db_password:Optional[str]=None,
            db_schema:Optional[any]=None,
            db_engine:Optional[any]=None
    ):
        self.db_host=os.getenv("DB_HOST")
        self.db_port=os.getenv("DB_PORT")
        self.db_name=os.getenv("DB_NAME")
        self.db_user=os.getenv("DB_USER")
        self.db_password=os.getenv("DB_PASSWORD")
        self.db_schema="public"
        self.db_engine=create_engine(
            url=f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}',
            connect_args={
                "options":'-csearch_path={}'.format(self.db_schema)
                }
        )

    def get_session(self):
        with Session(self.db_engine) as session:
            yield session

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.db_engine)