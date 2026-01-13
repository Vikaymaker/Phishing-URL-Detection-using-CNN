# encode.py
# Converts URL string into numerical sequence for CNN input.

from src.utils.config import CHAR_TO_INT, MAX_LEN
from tensorflow.keras.preprocessing.sequence import pad_sequences


def encode_url(url: str):
    """
    Converts a URL into a list of integer-encoded characters.
    Unknown characters become 0.
    """
    url = url.lower().strip()  # normalize URL

    encoded = [CHAR_TO_INT.get(ch, 0) for ch in url]
    return encoded


def encode_and_pad(url: str):
    """
    Encodes URL and pads it to MAX_LEN for model input.
    """
    seq = encode_url(url)
    padded = pad_sequences([seq], maxlen=MAX_LEN)
    return padded
