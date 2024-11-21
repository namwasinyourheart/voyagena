from fastapi import FastAPI
from schemas import UserInput, TripPlan
from chains import get_itinerary

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Voyagena, your AI Travel Planner!"}

@app.post("/generate-itinerary/")
async def generate_itinerary(user_input: UserInput) -> TripPlan:
    trip_plan = get_itinerary(user_input)
    return trip_plan

# uvicorn api:app --reload
