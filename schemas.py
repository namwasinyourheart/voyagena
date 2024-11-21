from pydantic import BaseModel, Field
from typing import Optional, List

class UserInput(BaseModel):
    destination: str = Field(..., description="The destination the user plans to visit.")
    trip_type: Optional[str] = Field(None, description="Type of trip: solo, partner, friendship, or family.")
    with_pets: Optional[bool] = Field(None, description="Indicates if the trip includes pets.")
    interests: Optional[list[str]] = Field(None, description="List of interests for activities during the trip.")
    other_interests: Optional[str] = Field(None, description="Additional interests provided by the user.")
    duration: Optional[str] = Field(None, description="Duration of the trip, e.g, 1 day, 3 days, 1 week.")
    start_date: Optional[str] = Field(None, description="Start date of the trip in DD-MM-YYYY format.")
    end_date: Optional[str] = Field(None, description="End date of the trip in DD-MM-YYYY format.")

class Activity(BaseModel):
    place: str
    activity: str

class DayPlan(BaseModel):
    day: int
    date: str
    activities: List[Activity]

class TripPlan(BaseModel):
    itinerary: List[DayPlan]
