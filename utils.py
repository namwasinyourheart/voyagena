
from typing import List, Dict
from schemas import TripPlan, DayPlan, Activity, UserInput
import requests

from constants import SERVER_URL

def extract_itinerary(response: str):
    import json
    import re

    match = re.search(r'```json(.*?)```', response, re.DOTALL)
    if match:
        itinerary_str = match.group(1).strip()
        # print(itinerary_str)

    itinerary_json = json.loads(itinerary_str)
    return itinerary_json

def convert_to_trip_plan(itinerary_json: List[Dict]) -> TripPlan:
    """
    Converts raw trip data into a TripPlan Pydantic model.

    Args:
        raw_data (List[Dict]): The raw data containing day plans and activities.

    Returns:
        TripPlan: A Pydantic model representing the trip plan.
    """
    return TripPlan(
        itinerary=[
            DayPlan(
                day=day['day'],
                date=day['date'],
                activities=[
                    Activity(place=activity[0], activity=activity[1]) for activity in day['activities']
                ]
            )
            for day in itinerary_json
        ]
    )


def send_requests(user_input: UserInput):
    response = requests.post(f"{SERVER_URL}/generate-itinerary/", data=user_input.json())
    return response.json() if response.status_code == 200 else {"status": "Error", "message": "Backend not reachable"}

