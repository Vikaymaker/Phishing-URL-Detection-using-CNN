# train.py
# Training script for CNN-based Phishing URL Detection
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from src.preprocessing.clean_url import clean_url
from src.preprocessing.encode import encode_url
from src.model.cnn_model import build_cnn_model
from src.utils.config import MAX_LEN
from tensorflow.keras.preprocessing.sequence import pad_sequences
import joblib
import os


def prepare_data(csv_path):
    """
    Loads and preprocesses dataset:
    - Cleans URLs
    - Encodes them
    - Pads sequences
    """
    df = pd.read_csv(csv_path)

    print("[INFO] Cleaning URLs...")
    df['cleaned_url'] = df['url'].apply(clean_url)

    print("[INFO] Encoding URLs...")
    df['encoded'] = df['cleaned_url'].apply(encode_url)

    print("[INFO] Padding sequences...")
    X = pad_sequences(df['encoded'].tolist(), maxlen=MAX_LEN)
    y = df['label'].values

    return X, y


def train_model():
    dataset_path = "dataset/processed/final_dataset.csv"

    print("[INFO] Loading dataset...")
    X, y = prepare_data(dataset_path)

    # Split dataset
    print("[INFO] Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    # Build model
    print("[INFO] Building CNN model...")
    model = build_cnn_model()

    # Train
    print("[INFO] Training model...")
    history = model.fit(
        X_train, y_train,
        epochs=5,
        batch_size=128,
        validation_data=(X_test, y_test)
    )

    # Create folder if missing
    if not os.path.exists("saved_models"):
        os.makedirs("saved_models")

    # Save model
    model.save("saved_models/cnn_url_model.h5")
    print("[INFO] Model saved as cnn_url_model.h5")

    # Save tokenizer-like encoder using joblib
    print("[INFO] Saving character encoder (CHAR_TO_INT)...")
    from src.utils.config import CHAR_TO_INT
    joblib.dump(CHAR_TO_INT, "saved_models/tokenizer.pkl")

    print("[INFO] Training Complete!")
    return history


if __name__ == "__main__":
    train_model()
