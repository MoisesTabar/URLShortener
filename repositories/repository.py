from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

T = TypeVar('T')

class IRepository(ABC, Generic[T]):

    @abstractmethod
    def get(self):
        raise NotImplemented
    
    @abstractmethod
    def get_one(self, key: str | int | Any):
        raise NotImplemented
    
    @abstractmethod
    def add(self, model: T):
        raise NotImplemented
    
    @abstractmethod
    def update(self, query: dict, values: dict):
        raise NotImplemented
