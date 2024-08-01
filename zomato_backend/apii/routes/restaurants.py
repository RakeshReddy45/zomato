import api
from flask import Blueprint, jsonify, request
from zomato_backend.apii.models import Restaurant
from app import db

restaurants_bp = Blueprint('restaurants_bp', __name__)

@restaurants_bp.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    restaurants = Restaurant.query.paginate(page=page, per_page=limit, error_out=False)

    return jsonify({
        'restaurants': [restaurant.serialize() for restaurant in restaurants.items],
        'totalPages': restaurants.pages
    })

@restaurants_bp.route('/api/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    return jsonify(restaurant.serialize())
