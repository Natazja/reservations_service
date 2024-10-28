# app.py
from flask import Flask, request, jsonify
from config import Config
from models import db, Reservation
from repository import ReservationRepository

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Opret ny reservation
@app.route('/api/v1/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    reservation = Reservation(
        first_name=data['first_name'],
        family_name=data['family_name'],
        country=data['country'],
        room_type=data['room_type'],
        days_rented=data['days_rented'],
        season=data['season'],
        price=data['price']
    )
    ReservationRepository.add(reservation)
    return jsonify({'message': 'Reservation created successfully'}), 201

# Hent alle reservationer
@app.route('/api/v1/reservations', methods=['GET'])
def get_reservations():
    reservations = ReservationRepository.get_all()
    return jsonify([{
        'id': r.id,
        'first_name': r.first_name,
        'family_name': r.family_name,
        'country': r.country,
        'room_type': r.room_type,
        'days_rented': r.days_rented,
        'season': r.season,
        'price': r.price
    } for r in reservations])

# Hent specifik reservation
@app.route('/api/v1/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    reservation = ReservationRepository.get_by_id(reservation_id)
    if reservation:
        return jsonify({
            'id': reservation.id,
            'first_name': reservation.first_name,
            'family_name': reservation.family_name,
            'country': reservation.country,
            'room_type': reservation.room_type,
            'days_rented': reservation.days_rented,
            'season': reservation.season,
            'price': reservation.price
        })
    return jsonify({'message': 'Reservation not found'}), 404

# Opdater en reservation
@app.route('/api/v1/reservations/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    reservation = ReservationRepository.get_by_id(reservation_id)
    if reservation:
        data = request.get_json()
        reservation.first_name = data['first_name']
        reservation.family_name = data['family_name']
        reservation.country = data['country']
        reservation.room_type = data['room_type']
        reservation.days_rented = data['days_rented']
        reservation.season = data['season']
        reservation.price = data['price']
        ReservationRepository.update()
        return jsonify({'message': 'Reservation updated successfully'})
    return jsonify({'message': 'Reservation not found'}), 404

# Slet en reservation
@app.route('/api/v1/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    reservation = ReservationRepository.get_by_id(reservation_id)
    if reservation:
        ReservationRepository.delete(reservation)
        return jsonify({'message': 'Reservation deleted successfully'})
    return jsonify({'message': 'Reservation not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
