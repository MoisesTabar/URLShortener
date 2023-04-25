from repositories.repository import IRepository
from pymongo import database
from models import URLs
from typing import Any

class UrlsRepository(IRepository[URLs]):

    def __init__(self, db_context: database.Database) -> None:
        self.db_context = db_context

    def get(self):
        return self.db_context.urls.find()
    
    def get_one(self, key: str | int | Any):
        return self.db_context.urls.find_one(key)
    
    def add(self, model: URLs):
        document = self.db_context.urls.insert_one(model.to_json)

        return document
    
    def update(self, query: dict, values: dict):
        document = self.db_context.urls.find_one_and_update(query, values)

        return document