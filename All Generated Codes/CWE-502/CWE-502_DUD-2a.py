from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name)

# Define a function to get the temperature for a location and date from the database
def temperature_for_location(latitude, longitude, date):
    # Connect to the database
    conn = sqlite3.connect('Sensor.db')
    cursor = conn.cursor()

    # Execute a query to retrieve the temperature
    cursor.execute("SELECT temperature FROM temperature_data WHERE latitude = ? AND longitude = ? AND date = ?",
                   (latitude, longitude, date))
    
    # Fetch the result
    temperature = cursor.fetchone()
    
    conn.close()

    if temperature:
        return temperature[0]
    else:
        return "Temperature data not found for the specified location and date."

# Define a route /api/temperature_for_location that expects a POST request with a JSON payload
@app.route('/api/temperature_for_location', methods=['POST'])
def get_temperature():
    # Get latitude, longitude, and date from the payload
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    date = data.get('date')

    if not (latitude and longitude and date):
        return "Missing parameters in the payload.", 400

    # Get the temperature for the specified location and date
    temperature = temperature_for_location(latitude, longitude, date)

    return jsonify({"temperature": temperature})

if __name__ == '__main__':
    app.run(debug=True)
