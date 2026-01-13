# evaluate.py
# Evaluation script for trained CNN Phishing URL Detector

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from src.preprocessing.clean_url import clean_url
from src.preprocessing.encode import encode_url
from src.utils.config import MAX_LEN


def prepare_data(csv_path):
    """
    Loads and processes dataset for evaluation.
    """
    df = pd.read_csv(csv_path)

    df['cleaned_url'] = df['url'].apply(clean_url)
    df['encoded'] = df['cleaned_url'].apply(encode_url)

    X = pad_sequences(df['encoded'].tolist(), maxlen=MAX_LEN)
    y = df['label'].values

    return X, y


def evaluate_model():
    dataset_path = "dataset/processed/final_dataset.csv"
    model_path = "saved_models/cnn_url_model.h5"

    print("[INFO] Loading dataset...")
    X, y = prepare_data(dataset_path)

    print("[INFO] Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    print("[INFO] Loading trained model...")
    model = load_model(model_path)

    print("[INFO] Evaluating model...")
    y_pred_probs = model.predict(X_test)
    y_pred = (y_pred_probs > 0.5).astype(int)

    # Metrics
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)

    print("\n================ Evaluation Results ================")
    print(f"Accuracy: {acc * 100:.2f}%\n")
    print("Confusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(cr)

    return acc, cm, cr


if __name__ == "__main__":
    evaluate_model()
