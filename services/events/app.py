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

@app.route('/events', methods=['GET'])
def get_events():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    conn.close()
    return jsonify(events)

@app.route('/events', methods=['POST'])
def add_event():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events (name, date, location) VALUES (%s, %s, %s)",
                   (data['name'], data['date'], data['location']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Event added"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
