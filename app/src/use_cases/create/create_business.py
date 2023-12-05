import structlog
from pymongo.collection import Collection

logger = structlog.get_logger()

class CreateTask:
    def __init__(self, collection: Collection):
        self.collection = collection
    async def execute(self, name: str, status: str):
        logger.info("Initializing \"create-task\" use case...")
        response = { "success": False }

        logger.info(f"Inserting task \"{name}\"...")
        try:
            task = self.collection.insert_one({ "name": name, "status": status }, { "_id": 0 })
 
            logger.info(f"Task \"{name}\" was successfully created.")
            response["success"] = True
            response["data"] = { "task_id": str(task.inserted_id) }
        except Exception as e:
            logger.error(f"Cannot create task \"{name}\"! Details: {e}")
            response["success"] = False
            response["error"] = e

        logger.info("Finishing \"create-task\" use case...")
        return response
