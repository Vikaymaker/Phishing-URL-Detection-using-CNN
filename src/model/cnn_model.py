# cnn_model.py
# CNN model for Phishing URL Detection

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, MaxPooling1D, GlobalMaxPooling1D, Dense, Dropout
from src.utils.config import VOCAB_SIZE, MAX_LEN, EMBEDDING_DIM


def build_cnn_model():
    """
    Builds and returns a 1D CNN model for URL classification.
    """
    model = Sequential([
        Embedding(
            input_dim=VOCAB_SIZE,
            output_dim=EMBEDDING_DIM,
            input_length=MAX_LEN
        ),

        Conv1D(filters=256, kernel_size=5, activation='relu'),
        MaxPooling1D(pool_size=2),

        Conv1D(filters=128, kernel_size=3, activation='relu'),
        GlobalMaxPooling1D(),

        Dense(64, activation='relu'),
        Dropout(0.3),

        Dense(1, activation='sigmoid')  # Output layer: 0 = safe, 1 = phishing
    ])

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model
