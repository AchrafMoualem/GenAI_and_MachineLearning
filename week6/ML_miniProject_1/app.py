from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import os

app = Flask(__name__)
CORS(app)
print("Python executable being used:")
import sys
print(sys.executable)

# -------- Load model --------
data = np.load("pricing_model_sgd.npz", allow_pickle=True)

model = {
    "theta": data["theta"],
    "X_mean": data["X_mean"],
    "X_std": data["X_std"],
    "features": data["features"].tolist()
}

# -------- Prediction function --------
def predict(input_data):
    x = np.array([input_data[f] for f in model["features"]]).reshape(1, -1)
    x_scaled = (x - model["X_mean"]) / model["X_std"]
    x_scaled = np.hstack([np.ones((1, 1)), x_scaled])  # bias
    y_pred = x_scaled.dot(model["theta"])
    return float(y_pred[0, 0])

# -------- Routes --------
@app.route("/")
def home():
    return send_from_directory(os.getcwd(), "index.html")

@app.route("/predict", methods=["POST"])
def predict_route():
    data = request.json
    prediction = predict(data)
    return jsonify({"prediction": prediction})

# -------- Run app --------
if __name__ == "__main__":
    app.run(debug=True)
