# clean_url.py
# Cleans and normalizes URLs + adds domain validation & typo detection.

import re
import tldextract
from difflib import SequenceMatcher

# Trusted brand domains (add more if needed)
TRUSTED_DOMAINS = [
    "google.com", "youtube.com", "facebook.com", "instagram.com", "twitter.com",
    "amazon.com", "paypal.com", "netflix.com", "microsoft.com", "apple.com",
    "linkedin.com", "wikipedia.org", "github.com", "stackoverflow.com"
]

# Similarity threshold for typosquatting detection
SIMILARITY_THRESHOLD = 0.75


def is_similar(a, b):
    """Return similarity ratio between two strings."""
    return SequenceMatcher(None, a, b).ratio()


def is_typosquatted(domain):
    """Detect if domain is a fake version of a trusted brand."""
    for real_domain in TRUSTED_DOMAINS:
        similarity = is_similar(domain, real_domain)
        if similarity >= SIMILARITY_THRESHOLD and domain != real_domain:
            return True
    return False


def clean_url(url: str) -> str:
    """
    Cleans a URL AND applies security checks:
    - Detects invalid domains
    - Detects typosquatting (fake lookalike domains)
    - Removes protocol (http/https)
    - Removes 'www.'
    - Removes trailing slash
    - Converts to lowercase
    """

    if not isinstance(url, str):
        return "INVALID_DOMAIN"

    url = url.lower().strip()

    # Extract domain using tldextract
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"

    # INVALID DOMAIN CHECK
    if extracted.suffix == "":
        return "INVALID_DOMAIN"

    # TYPOSQUATTING CHECK
    if is_typosquatted(domain):
        return "TYPOSQUAT"

    # --- Your original cleaning logic (kept exactly as you wrote it) ---
    url = re.sub(r'^https?:\/\/', '', url)   # Remove http/https
    url = re.sub(r'^www\.', '', url)         # Remove www.

    if url.endswith("/"):
        url = url[:-1]                       # Remove trailing slash
    # -------------------------------------------------------------------

    return url
