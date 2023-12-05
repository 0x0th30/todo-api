from fastapi import APIRouter
from src.use_cases.create import create_middleware
from src.use_cases.read import read_middleware
from src.use_cases.update import update_middleware
from src.use_cases.delete import delete_middleware

router = APIRouter()
router.include_router(create_middleware.router, prefix="", tags=[])
router.include_router(read_middleware.router, prefix="", tags=[])
router.include_router(update_middleware.router, prefix="", tags=[])
router.include_router(delete_middleware.router, prefix="", tags=[])
