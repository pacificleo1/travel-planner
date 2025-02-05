from fastapi import APIRouter
from services.pdf_generator import generate_pdf
from services.google_maps import fetch_places
from fastapi.responses import FileResponse

router = APIRouter(prefix="/itinerary", tags=["Itinerary"])

@router.get("/generate")
async def generate_itinerary(destination: str, days: int, meals_per_day: int):
    """Generate a travel schedule and return a downloadable PDF."""
    sights = await fetch_places(destination, "tourist attractions")
    restaurants = await fetch_places(destination, "restaurants")
    markets = await fetch_places(destination, "shopping malls")

    itinerary = {"destination": destination, "days": days, "sights": sights, "restaurants": restaurants, "markets": markets}
    
    pdf_path = generate_pdf(itinerary)
    return FileResponse(pdf_path, media_type="application/pdf", filename="trip_schedule.pdf")
