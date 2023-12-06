from app.common.database import MongoDB
from app.common.utils.load_env import load_env

MONGODB_CONNECTION_STRING = load_env("MONGODB_CONNECTION_STRING")
MONGODB_DATABASE_NAME = load_env("MONGODB_DATABASE_NAME")

mongo_client = MongoDB(MONGODB_CONNECTION_STRING)
database = mongo_client.get_database(MONGODB_DATABASE_NAME)

TaskCollection = database['task']
