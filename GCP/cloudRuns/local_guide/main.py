import requests
from flask import jsonify

def local_guide(request):
    data = request.get_json()
    location = data['location']  # User input location
    api_key = ""
    
    # First API call for must-visit places
    places_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=must+visit+places+in+{location}&key={api_key}"
    places_response = requests.get(places_url).json()
    
    # Extract top 10 must-visit places
    places = [{"name": place['name'], "address": place['formatted_address']} for place in places_response['results'][:15]]
    
    
    # Return both places and hotels
    return {"places": places}
