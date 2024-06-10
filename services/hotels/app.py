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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
