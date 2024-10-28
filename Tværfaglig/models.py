# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reservation(db.Model):
    __tablename__ = 'reservations'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    family_name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    days_rented = db.Column(db.Integer, nullable=False)
    season = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
