from flask import Blueprint, request, jsonify
from app.services.ai_service import recommend_crop

bp = Blueprint('crops', __name__)

@bp.route('/recommend-crop', methods=['GET'])
def recommend_crop_route():
    climate_condition = request.args.get('condition', 'drought-resistant')
    recommended_crop = recommend_crop(climate_condition)
    return jsonify({"recommended_crop": recommended_crop})
