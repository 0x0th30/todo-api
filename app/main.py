from fastapi import FastAPI
from app.api.routes import router
from app.common.utils.logger import setup_logging

setup_logging()

app = FastAPI()
app.include_router(router=router, prefix="/tasks")
