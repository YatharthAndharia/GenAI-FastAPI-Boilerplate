from fastapi import FastAPI
from app.routes import api_router

app = FastAPI(
    title="EduAI",
    debug=False,
)
app.include_router(api_router,prefix="")
