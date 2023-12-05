from fastapi import APIRouter, Response
from src.use_cases.delete.delete_business import DeleteTask
from src.models.task import TaskCollection

router = APIRouter()
delete_task_business = DeleteTask(TaskCollection)

@router.delete("/{task_id}")
async def handle(task_id: str, response: Response):
    http_response = { "success": False }
    delete_task_response = await delete_task_business.execute(task_id)

    if delete_task_response["success"] and delete_task_response["data"]:
        http_response["success"] = True
        http_response["data"] = { "task_id": delete_task_response["data"]["task_id"] }

        response.status_code = 200
        return http_response

    http_response["success"] = False
    http_response["message"] = "Failed by internal/unknown reasons!"

    response.status_code = 500
    return http_response
