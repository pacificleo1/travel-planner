import httpx
from config import GOOGLE_MAPS_API_KEY
PLACES_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

async def fetch_places(destination: str, category: str):
    """Fetch places (attractions, restaurants, markets) for a city."""
    url = f"{PLACES_URL}?query={category} in {destination}&key={GOOGLE_MAPS_API_KEY}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        places = response.json().get("results", [])
        return [{"name": p["name"], "address": p["formatted_address"]} for p in places[:10]]

#new 
def get_cities():
    from backend.services.other_module import G_M  # ✅ Import moved inside 
    return ["Dubai", "London", "New York"]
