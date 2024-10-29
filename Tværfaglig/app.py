# app.py
from flask import Flask, request, jsonify
from config import Config
from models import db, Reservation, RoomReservation
from repository import ReservationRepository, RoomReservationRepository

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint til at oprette ny reservation
@app.route('/api/v1/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    reservation = Reservation(
        check_in_date=data['check_in_date'],
        check_out_date=data['check_out_date'],
        status=data['status'],
        price=data['price'],
        payment_status=data['payment_status']
    )
    ReservationRepository.add(reservation)
    return jsonify({'message': 'Reservation created successfully', 'reservation_id': reservation.reservationID}), 201

# Endpoint til at tilføje værelse til reservation
@app.route('/api/v1/reservations/<int:reservation_id>/rooms', methods=['POST'])
def add_room_to_reservation(reservation_id):
    reservation = ReservationRepository.get_by_id(reservation_id)
    if reservation:
        data = request.get_json()
        room_id = data['room_id']
        reservation.add_room(room_id)
        return jsonify({'message': 'Room added to reservation successfully'}), 201
    return jsonify({'message': 'Reservation not found'}), 404

# Hent alle reservationer
@app.route('/api/v1/reservations', methods=['GET'])
def get_reservations():
    reservations = ReservationRepository.get_all()
    return jsonify([{
        'reservationID': r.reservationID,
        'check_in_date': r.check_in_date,
        'check_out_date': r.check_out_date,
        'status': r.status,
        'price': r.price,
        'payment_status': r.payment_status
    } for r in reservations])

# Hent værelser for en specifik reservation
@app.route('/api/v1/reservations/<int:reservation_id>/rooms', methods=['GET'])
def get_rooms_for_reservation(reservation_id):
    room_reservations = RoomReservationRepository.get_by_reservation_id(reservation_id)
    return jsonify([{
        'id': rr.id,
        'room_id': rr.room_id,
        'reservation_id': rr.reservation_id
    } for rr in room_reservations])
