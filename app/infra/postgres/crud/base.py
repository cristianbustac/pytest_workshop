from typing import Any, Dict, Generic, List, Optional

from app.schemas.general import CreateSchemaType, ModelType, UpdateSchemaType


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, *, model: ModelType) -> None:
        self.model = model

    async def get_all(
        self,
        *,
        payload: Dict[str, Any] = {},
        skip: int = 0,
        limit: int = 10,
    ) -> List[Dict[str, Any]]:
        if payload:
            model = (
                await self.model.filter(**payload)
                .offset(skip)
                .limit(limit)
                .order_by("id")
                .all()
                .values()
            )
        else:
            model = (
                await self.model.all().offset(skip).limit(limit).order_by("id").values()
            )
        return model

    async def create(self, *, obj_in: CreateSchemaType) -> Dict[str, Any]:
        obj_in_data = obj_in.dict()
        model = self.model(**obj_in_data)
        await model.save()
        return model

    async def update(self, *, id: int, obj_in: Dict[str, Any]) -> bool:
        model = await self.model.get(id=id)
        await model.update_from_dict(obj_in).save()
        return True

    async def delete(self, *, id: int) -> int:
        deletes = await self.model.filter(id=id).first().delete()
        return deletes

    async def get_by_id(self, *, id: int) -> Optional[Dict[str, Any]]:
        model = await self.model.filter(id=id).first().values()
        if model:
            return model[0]
        return None

    async def count(self, *, payload: Dict[str, Any] = {}) -> int:
        count = await self.model.filter(**payload).all().count()
        return count