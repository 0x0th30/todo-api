from fastapi import FastAPI
from src.api.routes import router
from src.common.utils.logger import setup_logging

setup_logging()

app = FastAPI()
app.include_router(router=router, prefix="/tasks")
