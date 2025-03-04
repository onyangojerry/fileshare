from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def admin_home():
    return {"message": "Welcome to the admin panel"}
