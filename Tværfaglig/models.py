from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Reservation(db.Model):
    __tablename__ = 'reservations'
    
    reservationID = db.Column(db.Integer, primary_key=True)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)

    # One-to-Many relationship with RoomReservation
    room_reservations = db.relationship('RoomReservation', backref='reservation', lazy=True)

    def add_room(self, room_id):
        new_room_reservation = RoomReservation(room_id=room_id, reservation_id=self.reservationID)
        db.session.add(new_room_reservation)
        db.session.commit()


class RoomReservation(db.Model):
    __tablename__ = 'room_reservations'
    
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.reservationID'), nullable=False)
    room_id = db.Column(db.Integer, nullable=False)
