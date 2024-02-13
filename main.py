from flask import Flask, request, jsonify
from flask_cors import CORS
from server import util

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Route to get location names
@app.route('/get_location_names')
def get_location_names():
    try:
        locations = util.get_location_names()
        response = jsonify({
            'locations': locations
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)})

# Route to predict home price
# @app.route('/predict_home_price', methods=['POST'])
@app.route('/predict_home_price', methods=['POST'])

def predict_home_price():
    try:
        # Parse input parameters from the POST request
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        # Use the util function to get the estimated price
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        # Return the result in the response
        response = jsonify({
            'estimated_price': estimated_price
        })
        return response
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    try:
        print('Starting Python Flask Server for Bangalore Home Price Prediction...')
        # Load artifacts before starting the server
        util.load_saved_artifacts()
        app.run()

    except Exception as e:
        print('Error starting the Flask server:', str(e))
