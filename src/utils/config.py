# config.py
# Global configuration for CNN Phishing URL Detection project

# Character vocabulary allowed in URLs
VOCAB = "abcdefghijklmnopqrstuvwxyz0123456789/:.?&=%-_"

# Mapping each character to a unique integer
CHAR_TO_INT = {ch: idx + 1 for idx, ch in enumerate(VOCAB)}

# Reverse mapping for debugging
INT_TO_CHAR = {idx + 1: ch for idx, ch in enumerate(VOCAB)}

# Vocabulary size for Embedding layer
VOCAB_SIZE = len(VOCAB) + 1  # +1 for unknown/padding token

# Maximum allowed URL length for padding
MAX_LEN = 200

# Size of embedding vectors learned by the model
EMBEDDING_DIM = 128

# Debug summary
if __name__ == "__main__":
    print("===== CONFIG SUMMARY =====")
    print("Vocabulary:", VOCAB)
    print("VOCAB_SIZE:", VOCAB_SIZE)
    print("MAX_LEN:", MAX_LEN)
    print("Embedding Dim:", EMBEDDING_DIM)
    print("Examples of CHAR_TO_INT:", list(CHAR_TO_INT.items())[:10])
