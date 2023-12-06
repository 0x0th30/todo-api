from fastapi import APIRouter, Response
from app.api.schemas.task import TaskModel
from app.use_cases.update.update_business import UpdateTask
from app.models.task import TaskCollection

router = APIRouter()
update_task_business = UpdateTask(TaskCollection)

@router.put("/{task_id}")
async def handle(task_id: str, task: TaskModel, response: Response):
    http_response = { "success": False }
    update_task_response = await update_task_business.execute(task_id, task.name, task.status)

    if update_task_response["success"] and update_task_response["data"]:
        http_response["success"] = True
        http_response["data"] = { "task_id": update_task_response["data"]["task_id"] }
        response.status_code = 201
        return http_response

    http_response["success"] = False
    http_response["message"] = "Failed by internal/unknown reasons!"

    response.status_code = 500
    return http_response
