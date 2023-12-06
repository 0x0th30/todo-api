from app.common.exceptions.application_exception import ApplicationException

class TaskException(ApplicationException):
    pass

class NotFoundTask(TaskException):
    def __init__(self, task_id: str):
        self.task_id = task_id
        self.message = f"Cannot found task with id {task_id}"
        super().__init__(self.message)
