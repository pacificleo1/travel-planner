from fastapi import APIRouter

router = APIRouter()  # ✅ Ensure this line is present

@router.get("/places")
async def get_places():
    return {"message": "List of places"}
