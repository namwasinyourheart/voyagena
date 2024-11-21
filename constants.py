SERVER_URL = "http://127.0.0.1:8000"


example_user_inputs = [
  {
    "destination": "Hanoi",
    "trip_type": "solo trip",
    "with_pets": "No",
    "interests": [
      "must-see attraction", 
      "cultural landmarks", 
      "great food", 
      "hidden gems", 
      "shopping"
    ],
    "other_interests": "Photography",
    "duration": "4 days",
    "start_date": "01/12/2025",
    "end_date": "01/16/2025"
  },
  {
    "destination": "Ho Chi Minh City",
    "trip_type": "partner trip",
    "with_pets": "No",
    "interests": [
      "must-see attraction", 
      "nightlife", 
      "great food", 
      "water sports", 
      "shopping"
    ],
    "other_interests": "Romance",
    "duration": "5 days",
    "start_date": "02/20/2025",
    "end_date": "02/24/2025"
  },
  {
    "destination": "Da Nang",
    "trip_type": "family trip",
    "with_pets": "No",
    "interests": [
      "scenic beaches", 
      "water sports", 
      "cultural landmarks", 
      "adventure and sports", 
      "wellness & spas"
    ],
    "other_interests": "Family bonding",
    "duration": "6 days",
    "start_date": "03/10/2025",
    "end_date": "03/15/2025"
  }
]


example_trip_plan = {'itinerary': [{'day': 1,
   'date': '01/12/2025',
   'activities': [{'place': 'Hoan Kiem Lake',
     'activity': 'Arrive in Hanoi and take a leisurely stroll around Hoan Kiem Lake, a must-see attraction.'},
    {'place': 'Ngoc Son Temple',
     'activity': 'Visit Ngoc Son Temple located on an island in the lake.'},
    {'place': 'Old Quarter',
     'activity': 'Explore the Old Quarter for shopping and hidden gems.'},
    {'place': 'Street Food Tour',
     'activity': 'Join a street food tour in the evening to taste local delicacies.'}]},
  {'day': 2,
   'date': '01/13/2025',
   'activities': [{'place': 'Ho Chi Minh Mausoleum',
     'activity': "Visit the Ho Chi Minh Mausoleum and learn about Vietnam's history."},
    {'place': 'One Pillar Pagoda',
     'activity': 'Explore the One Pillar Pagoda, a cultural landmark.'},
    {'place': 'Vietnamese Coffee',
     'activity': 'Enjoy a traditional Vietnamese coffee at a local café.'},
    {'place': 'Dong Xuan Market',
     'activity': 'Shop for souvenirs and local products at Dong Xuan Market.'}]},
  {'day': 3,
   'date': '01/14/2025',
   'activities': [{'place': 'Temple of Literature',
     'activity': "Visit the Temple of Literature, Vietnam's first university."},
    {'place': 'Vietnam Museum of Ethnology',
     'activity': 'Explore the Vietnam Museum of Ethnology to learn about diverse cultures.'},
    {'place': 'Lunch at Cha Ca La Vong',
     'activity': 'Have lunch at Cha Ca La Vong, famous for its grilled fish.'},
    {'place': 'Photography Walk',
     'activity': 'Take a photography walk around the West Lake area in the evening.'}]},
  {'day': 4,
   'date': '01/15/2025',
   'activities': [{'place': 'Thang Long Water Puppet Theatre',
     'activity': 'Attend a water puppet show in the morning.'},
    {'place': 'Shopping in the Old Quarter',
     'activity': 'Spend the afternoon shopping for unique handicrafts.'},
    {'place': 'Bun Cha Huong Lien',
     'activity': 'Enjoy dinner at Bun Cha Huong Lien, known for its bun cha.'},
    {'place': 'Night Market',
     'activity': 'Explore the night market for local snacks and souvenirs.'}]}]}