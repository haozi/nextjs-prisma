from typing import Union

from fastapi import APIRouter

router = APIRouter()


@router.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
