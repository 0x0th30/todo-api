import structlog
from typing import Optional
from bson.objectid import ObjectId
from pymongo.collection import Collection
from app.common.exceptions.task_exception import NotFoundTask

logger = structlog.get_logger()

class ReadTask:
    def __init__(self, collection: Collection):
        self.collection = collection
    async def execute(self, task_id: Optional[str]):
        logger.info("Initializing \"read-task\" use case...")
        response = { "success": False }

        if task_id:
            logger.info(f"Searching by task w/ id \"{task_id}\"...")
            try:
                raw_task = self.collection.find_one({ "_id": ObjectId(task_id) })
                logger.info("Search was successfully performed!")

                if not raw_task:
                    raise NotFoundTask(task_id)

                tasks = [{
                    "id": str(raw_task["_id"]),
                    "name": raw_task["name"],
                    "status": raw_task["status"]
                }]

                response["success"] = True
                response["data"] = { "tasks": tasks }
            except Exception as e:
                logger.error(f"Cannot search task! Details {e}")
                response["success"] = False
                response["error"] = e
        else:
            logger.info("Searching by all tasks...")
            try:
                raw_tasks = self.collection.find({})
                logger.info("Search was successfully performed!")

                tasks = list()
                for raw_task in raw_tasks:
                    task = {
                        "id": str(raw_task["_id"]),
                        "name": raw_task["name"],
                        "status": raw_task["status"]
                    }
                    tasks.append(task)

                response["success"] = True
                response["data"] = { "tasks": tasks }
            except Exception as e:
                logger.error(f"Cannot search tasks! Details {e}")
                response["success"] = False
                response["error"] = e

        logger.info("Finishing \"read-task\" use case...")
        return response
        