from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='pariwisata'
    )

@app.route('/hotels', methods=['GET'])
def get_hotels():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM hotels")
    hotels = cursor.fetchall()
    conn.close()
    return jsonify(hotels)

@app.route('/hotels', methods=['POST'])
def add_hotel():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hotels (name, location, price) VALUES (%s, %s, %s)",
                   (data['name'], data['location'], data['price']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Hotel added"}), 201

@app.route('/hotels/<int:hotel_id>', methods=['PUT'])
def update_hotel(hotel_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE hotels 
        SET name = %s, location = %s, price = %s
        WHERE id = %s
    """, (data['name'], data['location'], data['price'], hotel_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Hotel updated"})

@app.route('/hotels/<int:hotel_id>', methods=['DELETE'])
def delete_hotel(hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hotels WHERE id = %s", (hotel_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Hotel deleted"})

@app.route('/bookings', methods=['POST'])
def book_hotel():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hotel_bookings (user_id, hotel_id, booking_date, nights) VALUES (%s, %s, %s, %s)",
                   (data['user_id'], data['hotel_id'], data['booking_date'], data['nights']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Booking successful"}), 201

@app.route('/bookings/<int:booking_id>', methods=['PUT'])
def update_hotel_booking(booking_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE hotel_bookings
        SET user_id = %s, hotel_id = %s, booking_date = %s, nights = %s
        WHERE id = %s
    """, (data['user_id'], data['hotel_id'], data['booking_date'], data['nights'], booking_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Booking updated"})

@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_hotel_booking(booking_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hotel_bookings WHERE id = %s", (booking_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Booking deleted"})

@app.route('/bookings/<int:user_id>', methods=['GET'])
def get_user_bookings(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT hb.id, h.name, h.location, h.price, hb.booking_date, hb.nights
        FROM hotel_bookings hb
        JOIN hotels h ON hb.hotel_id = h.id
        WHERE hb.user_id = %s
    """, (user_id,))
    bookings = cursor.fetchall()
    conn.close()
    return jsonify(bookings)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
