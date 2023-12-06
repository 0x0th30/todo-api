import structlog
from pymongo.collection import Collection
from bson.objectid import ObjectId

logger = structlog.get_logger()

class UpdateTask:
    def __init__(self, collection: Collection):
        self.collection = collection
    async def execute(self, task_id: str, name: str, status: str):
        logger.info("Initializing \"update-task\" use case...")
        response = { "success": False }

        logger.info(f"Inserting task \"{name}\"...")
        try:
            self.collection.find_one_and_update(
                { "_id": ObjectId(task_id) },
                { "$set": { "name": name, "status": status } },
            )
            logger.info(f"Task w/ id \"{task_id}\" was successfully updated.")

            response["success"] = True
            response["data"] = { "task_id": task_id }
        except Exception as e:
            logger.error(f"Cannot update task \"{name}\"! Details: {e}")
            response["success"] = False
            response["error"] = e

        logger.info("Finishing \"update-task\" use case...")
        return response
