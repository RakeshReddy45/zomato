from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(255))
    country_code = db.Column(db.String(10))
    city = db.Column(db.String(100))
    address = db.Column(db.String(255))
    locality = db.Column(db.String(100))
    locality_verbose = db.Column(db.String(255))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    cuisines = db.Column(db.String(255))
    average_cost_for_two = db.Column(db.Integer)
    currency = db.Column(db.String(10))
    has_table_booking = db.Column(db.String(3))
    has_online_delivery = db.Column(db.String(3))
    is_delivering = db.Column(db.String(3))
    switch_to_order_menu = db.Column(db.String(3))
    price_range = db.Column(db.Integer)
    aggregate_rating = db.Column(db.Float)
    rating_color = db.Column(db.String(10))
    rating_text = db.Column(db.String(50))
    votes = db.Column(db.Integer)
