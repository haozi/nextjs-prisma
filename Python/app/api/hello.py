from fastapi import APIRouter

router = APIRouter()


@router.get("/api/hello")
def read_root():
    return {"Hello": "World"}


@router.get("/api/hello2")
def read_root():
    return {"Hello": "World222"}
