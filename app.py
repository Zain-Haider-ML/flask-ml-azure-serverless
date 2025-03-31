import joblib
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    model = None


@app.route("/", methods=["GET"])
def home():
    return "Flask ML Model API is running!"


@app.route("/predict", methods=["POST"])
def predict():
    if not model:
        return jsonify({"error": "Model not found. Train and save it as 'model.pkl'"}), 500

    try:
        # Get JSON input
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)  # Convert to NumPy array

        # Make a prediction
        prediction = model.predict(features)
        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
