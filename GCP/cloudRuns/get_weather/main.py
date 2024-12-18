import requests
from flask import jsonify

def get_weather(request):
    data = request.get_json()
    location = data['location']
    api_key = ""

    # API Call to OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    weather_data = requests.get(url).json()
    
    response = {
        "location": location,
        "temperature": weather_data['main']['temp'],
        "condition": weather_data['weather'][0]['description']
    }
    return jsonify(response)
