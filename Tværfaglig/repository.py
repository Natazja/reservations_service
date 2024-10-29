# repository.py
from models import db, Reservation, RoomReservation

class ReservationRepository:
    @staticmethod
    def add(reservation):
        db.session.add(reservation)
        db.session.commit()

    @staticmethod
    def get_by_id(reservation_id):
        return Reservation.query.get(reservation_id)

    @staticmethod
    def get_all():
        return Reservation.query.all()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(reservation):
        db.session.delete(reservation)
        db.session.commit()

class RoomReservationRepository:
    @staticmethod
    def add(room_reservation):
        db.session.add(room_reservation)
        db.session.commit()

    @staticmethod
    def get_by_reservation_id(reservation_id):
        return RoomReservation.query.filter_by(reservation_id=reservation_id).all()

