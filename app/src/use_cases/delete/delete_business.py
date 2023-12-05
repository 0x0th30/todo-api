import structlog
from bson.objectid import ObjectId
from pymongo.collection import Collection

logger = structlog.get_logger()

class DeleteTask:
    def __init__(self, collection: Collection):
        self.collection = collection
    async def execute(self, task_id: str):
        logger.info("Initializing \"delete-task\" use case...")
        response = { "success": False }

        logger.info(f"Searching by task w/ id \"{task_id}\"...")
        try:
            self.collection.find_one_and_delete({ "_id": ObjectId(task_id) })
            logger.info(f"Task w/ id \"{task_id}\" was successfully deleted.")

            response["success"] = True
            response["data"] = { "task_id": task_id }
        except Exception as e:
            logger.error(f"Cannot delete task! Details {e}")
            response["success"] = False
            response["error"] = e

        logger.info("Finishing \"delete-task\" use case...")
        return response
        