from pymongo import MongoClient
from pymongo.database import Database

class MongoDB:
    def __init__(self, connection_string: str):
        self.client = MongoClient(connection_string)
    def get_database(self, database: str) -> Database:
        return self.client[database]
