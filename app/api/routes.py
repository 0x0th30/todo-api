from fastapi import APIRouter
from app.use_cases.create import create_router
from app.use_cases.read import read_router
from app.use_cases.update import update_router
from app.use_cases.delete import delete_router

router = APIRouter()
router.include_router(create_router.router, prefix="", tags=[])
router.include_router(read_router.router, prefix="", tags=[])
router.include_router(update_router.router, prefix="", tags=[])
router.include_router(delete_router.router, prefix="", tags=[])
