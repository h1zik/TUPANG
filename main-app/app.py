from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, Pariwisata!"})

# Events
@app.route('/events', methods=['GET'])
def get_events():
    response = requests.get('http://localhost:5001/events')
    return jsonify(response.json())

@app.route('/events', methods=['POST'])
def add_event():
    data = request.json
    response = requests.post('http://localhost:5001/events', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    response = requests.put(f'http://localhost:5001/events/{event_id}', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    response = requests.delete(f'http://localhost:5001/events/{event_id}')
    return jsonify(response.json()), response.status_code

@app.route('/events/bookings', methods=['POST'])
def book_event():
    data = request.json
    response = requests.post('http://localhost:5001/bookings', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/events/bookings/<int:booking_id>', methods=['PUT'])
def update_event_booking(booking_id):
    data = request.json
    response = requests.put(f'http://localhost:5001/bookings/{booking_id}', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/events/bookings/<int:booking_id>', methods=['DELETE'])
def delete_event_booking(booking_id):
    response = requests.delete(f'http://localhost:5001/bookings/{booking_id}')
    return jsonify(response.json()), response.status_code

@app.route('/events/bookings/<int:user_id>', methods=['GET'])
def get_event_bookings(user_id):
    response = requests.get(f'http://localhost:5001/bookings/{user_id}')
    return jsonify(response.json())

# Hotels
@app.route('/hotels', methods=['GET'])
def get_hotels():
    response = requests.get('http://localhost:5002/hotels')
    return jsonify(response.json())

@app.route('/hotels', methods=['POST'])
def add_hotel():
    data = request.json
    response = requests.post('http://localhost:5002/hotels', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/hotels/<int:hotel_id>', methods=['PUT'])
def update_hotel(hotel_id):
    data = request.json
    response = requests.put(f'http://localhost:5002/hotels/{hotel_id}', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/hotels/<int:hotel_id>', methods=['DELETE'])
def delete_hotel(hotel_id):
    response = requests.delete(f'http://localhost:5002/hotels/{hotel_id}')
    return jsonify(response.json()), response.status_code

@app.route('/hotels/bookings', methods=['POST'])
def book_hotel():
    data = request.json
    response = requests.post('http://localhost:5002/bookings', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/hotels/bookings/<int:booking_id>', methods=['PUT'])
def update_hotel_booking(booking_id):
    data = request.json
    response = requests.put(f'http://localhost:5002/bookings/{booking_id}', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/hotels/bookings/<int:booking_id>', methods=['DELETE'])
def delete_hotel_booking(booking_id):
    response = requests.delete(f'http://localhost:5002/bookings/{booking_id}')
    return jsonify(response.json()), response.status_code

@app.route('/hotels/bookings/<int:user_id>', methods=['GET'])
def get_hotel_bookings(user_id):
    response = requests.get(f'http://localhost:5002/bookings/{user_id}')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)