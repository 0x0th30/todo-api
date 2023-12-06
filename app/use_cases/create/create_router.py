from fastapi import APIRouter, Response
from app.api.schemas.task import TaskModel
from app.use_cases.create.create_business import CreateTask
from app.models.task import TaskCollection

router = APIRouter()
create_task_business = CreateTask(TaskCollection)

@router.post("/create")
async def handle(task: TaskModel, response: Response):
    http_response = { "success": False }
    create_task_response = await create_task_business.execute(task.name, task.status)

    if create_task_response["success"] and create_task_response["data"]:
        http_response["success"] = True
        http_response["data"] = { "task_id": create_task_response["data"]["task_id"] }

        response.status_code = 201
        return http_response

    http_response["success"] = False
    http_response["message"] = "Failed by internal/unknown reasons!"

    response.status_code = 500
    return http_response
