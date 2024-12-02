import streamlit as st
import datetime
# from datetime import datetime
from streamlit_pills import pills

from schemas import UserInput, TripPlan
from utils import send_requests
from map_utils import geocode_address


user_input = {}

st.set_page_config(layout='wide')

st.title("✈️ Voyagena: Your AI Travel Planner")


input_container = st.container(height=450)
with input_container:

    choose_container = st.container()
    with choose_container:
        st.subheader("✍ Describe your trip")

        col1, col2, col3 = st.columns([3,2.5,1.2])
        with col1:
            # col1, col2 = st.columns(2)
            # with col1:

            mc1, mc2 = st.columns([1,4])
            with mc1:
                destination = st.text_input(label="Destination",
                                            placeholder="Choose a city")
                user_input['destination'] = destination


            with mc2: 
                options = [
                    "Hanoi", "Ha Giang", "Sa Pa", "Pu Luong and Mai Chau", 
                    "Halong Bay", "Hue", "Danang",
                    "Hoi An", "Nha Trang", "Dalat", "Ho Chi Minh City", "Con Dao", "Phu Quoc",
                    "Bangkok", "Dubai", "Bali", "London", "Rome", "Paris", "New York"
                ]
                # icons = ["🔍", "🌐", "📝", "📈", "💼", "🌟", "✉️", "🧠  "]

                pill_destination = pills(
                    "Or get started with a popular destination:",
                    options,
                    # clearable=None,  # type: ignore
                    # icons=icons,
                    # index=st.session_state["active_option_index"],
                    key="pills",
                )

                # print(pill_destination)

                if pill_destination:
                    user_input['destination'] = pill_destination


            mc1, mc2 = st.columns([4,1])
            with mc1:
                # print("Destination:", destination)
                trip_type = st.radio("Kind of trip",
                                    ["solo trip", "partner trip", "friendship trip", "family trip"], 
                                    horizontal = True,)
                user_input['trip_type'] = trip_type
            with mc2:
                with_pets = st.checkbox(label="With pets")
                user_input['with_pets'] = with_pets

        with col2:
            interests = st.multiselect("Intersts",
                                ["must-see attraction", "great food", "hidden gems", 
                                "cuban cuisine", "scenic beaches", "water sports",
                                "cultural landmarks", "nightlife",
                                "wellness & spas", "shopping", 
                                "adventure and sports", "arts & theatre"], 
                                placeholder="Tell us what you’re interested in"
                                #  horizontal = True,
                                )
            user_input['interests'] = interests
            
            other_interests = st.text_input("Add other interests",
                                            placeholder="Add other interests")
            user_input['other_interests'] = other_interests

        with col3:
            
            duration = pills(
                "Choose duration",
                options=["1 day", "3 days", "1 week"]
            )

            user_input['duration'] = duration
            # with_pets = st.checkbox(label="I haven't know yet")
            st.write("Or choose a date range, up to 7 days:")

            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input("📅 Start date")
                # print(type(start_date))
                user_input['start_date'] = start_date.strftime("%d/%m/%y")
            # with col2:
                end_date = st.date_input("📅 End date")
                # end_date = datetime.datetime.strptime(end_date, "%m/%d/%Y")
                user_input['end_date'] = end_date.strftime("%d/%m/%y")
    
    nl_expander = st.expander('Or describe your trip in natural language')
    with nl_expander:
        description = st.text_area("", height=70,
                                   placeholder="""e.g., I'm planning a solo trip to Hanoi for 4 days, from December 1st to December 4th. I love exploring cultural landmarks, trying local street food, and taking photos. I won't be bringing any pets.""")
      
gen_itinerary_button = st.button("Generate itinerary",)
     
if gen_itinerary_button:

    places_list = []

    with st.spinner("Generating..."):

        planner_input = UserInput(**user_input)
        trip_plan = send_requests(planner_input)

        # from constants import example_trip_plan
        # trip_plan = example_trip_plan

    itinerary = trip_plan['itinerary']
    # print("trip_plan:", trip_plan)
    print(itinerary)
    # duration = len(itinerary)

    col1, col2 = st.columns([0.45, 0.55])

    with col1: 
        itinerary_container = st.container(height=600)
        with itinerary_container:
            st.subheader("👣 Suggested Itinerary")
            st.text_input("Do you want to adjust anything about the itinerary?")
            st.button("Adjust")

            for day_plan in itinerary:
                day_of_week = datetime.datetime.strptime(day_plan['date'], "%d/%m/%Y").date().strftime("%A")
                expander = st.expander(f"Day {day_plan['day']}: {day_of_week}, {day_plan['date']}")
                # expander.write(day_plan['activities']['place'])
                for activity in day_plan['activities']:
                    lat, lon = geocode_address(activity['place'])
                    if lat and lon:
                        places_list.append((lat, lon))
                    expander.write(activity['activity'])
                # expander.image("https://static.streamlit.io/examples/dice.jpg")


    with col2: 
        map_container = st.container(height=600)
        import folium
        from folium.plugins import Search
        import pandas as pd

        from streamlit_folium import st_folium
        with map_container:

            # # Streamlit app layout
            st.subheader("🌎 Map Viewer")

            # # Latitude and longitude of Vietnam
            # latitude = 12.270549
            # longitude = 109.176954

            # Calculate the average latitude and longitude
            avg_lat = sum(lat for lat, lon in places_list) / len(places_list)
            avg_lon = sum(lon for lat, lon in places_list) / len(places_list)

            # Create a map centered at the average coordinates
            map = folium.Map(location=[avg_lat, avg_lon], zoom_start=8)
                        
            for (lat, lon) in places_list:

                folium.Marker(
                location=[lat, lon]
                ).add_to(map)

            # st_map = st_folium(m)
            st.components.v1.html(folium.Figure().add_child(map).render(),height=500)

            # # User input for latitude and longitude
            # latitude = st.number_input("Enter latitude", min_value=-90.0, max_value=90.0, value=0.0)
            # longitude = st.number_input("Enter longitude", min_value=-180.0, max_value=180.0, value=0.0)

            # # latitude, longitude = 90, 90

            # # Create a map centered at the user input location
            # map_center = [latitude, longitude]
            # my_map = folium.Map(location=map_center, zoom_start=12)

            # # Add a marker to the map at the user location
            # folium.Marker(location=map_center, popup=f"Location: {latitude}, {longitude}").add_to(my_map)

            # # Render the map in the Streamlit app
            # st_folium(my_map, width=700)

            # ## Create a sample DataFrame with latitude and longitude values
            # data = pd.DataFrame({
            #     'latitude': [37.7749, 34.0522, 40.7128],
            #     'longitude': [-122.4194, -118.2437, -74.0060]
            # })

            # # Create a DataFrame with the points you want to highlight
            # highlight = pd.DataFrame({
            #     'latitude': [37.7749],
            #     'longitude': [-122.4194]
            # })
            
            # # Add the highlight points to the map
            # st.map()
