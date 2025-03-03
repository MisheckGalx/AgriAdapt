from flask import Blueprint, request, jsonify
import requests
from app import Config

bp = Blueprint('weather', __name__)

@bp.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location', 'Nairobi')
    API_KEY = Config.OPENWEATHERMAP_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    return jsonify({
        "location": location,
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    })
