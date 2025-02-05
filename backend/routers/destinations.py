from fastapi import APIRouter
#from services.google_maps import get_cities
def G_M(): # defined by me 
    from backend.services.google_maps import get_cities  # ✅ Import moved inside
    return get_cities()


router = APIRouter(prefix="/destinations", tags=["Destinations"])

@router.get("/")
async def fetch_destinations():
    return get_cities()
