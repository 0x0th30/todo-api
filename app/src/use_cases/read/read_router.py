from typing import Optional
from fastapi import APIRouter, Response
from src.use_cases.read.read_business import ReadTask
from src.models.task import TaskCollection
from src.common.exceptions.task_exception import NotFoundTask

router = APIRouter()
read_task_business = ReadTask(TaskCollection)

@router.get("/")
@router.get("/{task_id}")
async def handle(response: Response, task_id: Optional[str] = None):
    http_response = { "success": False }
    read_task_response = await read_task_business.execute(task_id)

    if read_task_response["success"] and read_task_response["data"]:
        http_response["success"] = True
        http_response["data"] = { "tasks": read_task_response["data"]["tasks"] }

        response.status_code = 200
        return http_response

    if not read_task_response["success"] and isinstance(read_task_response["error"], NotFoundTask):
        http_response["success"] = True
        http_response["message"] = "Cannot found no one task with specified id!"

        response.status_code = 404
        return http_response

    http_response["success"] = False
    http_response["message"] = "Failed by internal/unknown reasons!"

    response.status_code = 500
    return http_response
