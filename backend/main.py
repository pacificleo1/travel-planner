from fastapi import FastAPI
from routers import destinations, places, itinerary

app = FastAPI(title="Travel Planner API")

# Register routers
app.include_router(destinations.router)
app.include_router(places.router)
app.include_router(itinerary.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Travel Planner API"}
