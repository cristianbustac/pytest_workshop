from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional

from app.schemas.general import CreateSchemaType, UpdateSchemaType


class IServiceBase(Generic[CreateSchemaType, UpdateSchemaType], ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def create(self, *, obj_in: CreateSchemaType) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *, id: int, obj_in: Dict[str, Any]) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *, id: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *, id: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_all(
        self, *, payload: Optional[Dict[str, Any]], skip: int, limit: int
    ) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def count(self, *, payload: Optional[Dict[str, Any]]) -> int:
        raise NotImplementedError