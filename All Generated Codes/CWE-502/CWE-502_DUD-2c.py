from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name)

# Configure the database URI (replace with your database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temperature.db'
db = SQLAlchemy(app)

# Define the temperature data model
class TemperatureData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    date = db.Column(db.String(10))
    temperature = db.Column(db.Float)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    if not latitude or not longitude or not date:
        return jsonify({'error': 'Latitude, longitude, and date are required'}), 400

    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return jsonify({'error': 'Invalid latitude or longitude'}), 400

    temperature_record = TemperatureData.query.filter_by(latitude=latitude, longitude=longitude, date=date).first()

    if temperature_record:
        return jsonify({'temperature': temperature_record.temperature})
    else:
        return jsonify({'error': 'Temperature data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)