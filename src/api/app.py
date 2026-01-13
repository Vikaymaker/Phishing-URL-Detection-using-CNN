# app.py
# Flask API for real-time phishing URL detection

import sys
import os
import webbrowser

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from flask import Flask, request, jsonify, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import joblib
from flask_cors import CORS

from src.preprocessing.clean_url import clean_url
from src.preprocessing.encode import encode_url
from src.utils.config import MAX_LEN

app = Flask(__name__)
CORS(app)

# Path to UI folder
UI_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../ui"))

# Load trained CNN model
MODEL_PATH = "saved_models/cnn_url_model.h5"
TOKENIZER_PATH = "saved_models/tokenizer.pkl"

print("[INFO] Loading model...")
model = load_model(MODEL_PATH)

print("[INFO] Loading tokenizer...")
CHAR_TO_INT = joblib.load(TOKENIZER_PATH)


# -----------------------------
# ★ Serve index.html as homepage
# -----------------------------
@app.route("/")
def serve_home():
    return send_from_directory(UI_FOLDER, "index.html")


# -----------------------------
# ★ Serve CSS & JS (frontend assets)
# -----------------------------
@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(UI_FOLDER, filename)


# -----------------------------
# ★ API Endpoint for prediction
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "url" not in data:
        return jsonify({"error": "URL missing in request"}), 400

    url = data["url"]
    print(f"[INFO] Predicting for URL: {url}")

    # Step 1: Clean URL
    cleaned = clean_url(url)
    # Handle invalid domains
    if cleaned == "INVALID_DOMAIN":
        return jsonify({
        "url": url,
        "prediction": "invalid",
        "probability": 1.0,
        "reason": "Malformed or invalid domain"
    })

    # Handle typosquatting
    if cleaned == "TYPOSQUAT":
        return jsonify({
        "url": url,
        "prediction": "phishing",
        "probability": 0.99,
        "reason": "Suspicious domain impersonation detected"
    })


    # Step 2: Encode
    encoded = [CHAR_TO_INT.get(c, 0) for c in cleaned]

    # Step 3: Pad
    padded = pad_sequences([encoded], maxlen=MAX_LEN)

    # Step 4: Predict
    prob = model.predict(padded)[0][0]
    label = "phishing" if prob > 0.6 else "legitimate"

    return jsonify({
        "url": url,
        "cleaned_url": cleaned,
        "prediction": label,
        "probability": float(prob)
    })


if __name__ == "__main__":
    print("[INFO] Starting Flask server...")

    # AUTO-OPEN UI IN BROWSER
    webbrowser.open("http://localhost:5000/")

    app.run(host="0.0.0.0", port=5000, debug=True)
