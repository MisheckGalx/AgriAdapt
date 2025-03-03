from flask import Blueprint, request, jsonify
from app.models import SensorData, Farmer
from app import db

bp = Blueprint('iot', __name__)

@bp.route('/soil-moisture', methods=['POST'])
def soil_moisture():
    data = request.json
    farmer_id = data.get('farmer_id')
    moisture_level = data.get('moisture_level')
    
    # Save sensor data to the database
    sensor_data = SensorData(farmer_id=farmer_id, moisture_level=moisture_level)
    db.session.add(sensor_data)
    db.session.commit()
    
    # Analyze moisture level and suggest irrigation
    if moisture_level < 30:
        suggestion = "Irrigate immediately"
    elif 30 <= moisture_level < 60:
        suggestion = "Irrigate moderately"
    else:
        suggestion = "No irrigation needed"
    
    return jsonify({"suggestion": suggestion})
