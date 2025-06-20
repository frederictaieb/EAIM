from fastapi import APIRouter

router = APIRouter()

@router.get("/api/helloworld")
async def helloworld():
    return {"message": "Hello from FastAPI!"}