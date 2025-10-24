from flask import Flask, request, jsonify
from joblib import load
import numpy as np


app = Flask(__name__)

# Load the model when the app starts
try:
    model = load('model.joblib')
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from POST request
        data = request.get_json()
        years_exp = data.get('years_experience')
        if years_exp is None:
            return jsonify({'error': 'No years_experience provided'}), 400
        # Convert to numpy array and reshape
        X = np.array(years_exp).reshape(-1, 1)
        # Make prediction
        prediction = model.predict(X)
        # Convert numpy array to list for JSON serialization
        return jsonify({
            'predicted_salaries': prediction.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)