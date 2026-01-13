# tokenizer.py
# Helper functions for encoding and decoding URL characters.

from src.utils.config import CHAR_TO_INT, INT_TO_CHAR


def text_to_sequence(text: str):
    """
    Converts a URL string into a list of integer-encoded characters.
    Characters not in the vocabulary become 0.
    """
    text = text.lower().strip()
    return [CHAR_TO_INT.get(ch, 0) for ch in text]


def sequence_to_text(sequence: list):
    """
    Converts a list of integers back into text.
    Useful for debugging.
    """
    return "".join([INT_TO_CHAR.get(i, "?") for i in sequence])


def print_tokenizer_summary():
    """
    Prints tokenizer vocabulary size and sample mapping.
    """
    print("========= TOKENIZER SUMMARY =========")
    print(f"Total Characters in Vocabulary: {len(CHAR_TO_INT)}")
    print("\nCharacter to Integer Mapping (First 10):")
    sample = list(CHAR_TO_INT.items())[:10]
    for ch, idx in sample:
        print(f"'{ch}' → {idx}")
    print("=====================================")
