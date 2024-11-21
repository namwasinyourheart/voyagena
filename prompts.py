from langchain_core.prompts import ChatPromptTemplate

gen_itinerary_prompt_template = """
You are a helpful travel assistant. Your task is to create a day-by-day trip itinerary based on user input. 
The user input includes destination, start date, end date, kind of trip (solo, partner, friendship, or family), with pets or not, interests.
The itinerary should be concise, include suggested activities for each day, and tailored to the user's preferences.
Here is the user input, where some fields may be blank.
- Destination: {destination}
- Trip type: {trip_type}
- With pets: {with_pets}
- Interests: {interests}
- Other interests: {other_interests}
- Duration: {duration}
- Start date: {start_date}
- End date: {end_date}

Your output MUST be format of a list of dict as follows:
```json
[
{{"day": <e.g., 1>, 
"date": <e.g., 08/11/2024>, 
"activities": <e.g., [["", "Arrive in Danang and check into your accommodation."], ["Bánh Mì Phượng", "Enjoy breakfast at Bánh Mì Phượng for a delicious Vietnamese sandwich."], ["Dragon Bridge", "Visit the Dragon Bridge and take photos of this iconic landmark."]],
}},
...
]
```
where:
- day: the order of day in the itinerary
- date: the exact date
- activities:  list of lists, each list containing a str of proper noun for the place and a str of corresponding activity

Now start to generate itinerary.
"""

gen_itinerary_prompt = ChatPromptTemplate.from_template(gen_itinerary_prompt_template)