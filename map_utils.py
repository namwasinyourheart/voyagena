import requests
from urllib.parse import quote
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ['GEOAPIFY_API_KEY']

def geocode_address(address: str):
    """
    Geocode an address using the Geoapify API.
    
    Args:
        address (str): The address to geocode.
        api_key (str): Your Geoapify API key.
    
    Returns:
        dict: The geocoding results as a dictionary.
              Includes latitude, longitude, and formatted address.
              Returns None if the request fails.
    """
    # Encode the address for use in the URL
    encoded_address = quote(address)
    
    # Build the request URL
    url = f"https://api.geoapify.com/v1/geocode/search?text={encoded_address}&format=json&apiKey={api_key}"
    
    try:
        # Send the GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the first result if available
        if data.get("results"):
            lat = data['results'][0]['lat']
            lon = data['results'][0]['lon']
            # return data["results"][0]  # Return the first result
            return (lat, lon)
        else:
            print("No results found.")
            return (None, None)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return (None, None)

# # Example usage:
# address = "38 Upper Montagu Street, London W1H 1LJ, United Kingdom"
# api_key = "YOUR_API_KEY"

# result = geocode_address(address, api_key)
# if result:
#     print("Geocoding Result:")
#     print(f"Latitude: {result['lat']}, Longitude: {result['lon']}")
#     print(f"Formatted Address: {result['formatted']}")
