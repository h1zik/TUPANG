from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, Pariwisata!"})

@app.route('/events', methods=['GET'])
def get_events():
    response = requests.get('http://localhost:5001/events')
    return jsonify(response.json())

@app.route('/hotels', methods=['GET'])
def get_hotels():
    response = requests.get('http://localhost:5002/hotels')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
