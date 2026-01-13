# dataset_loader.py
# Utility functions for loading phishing URL datasets

import pandas as pd


def load_csv(path: str):
    """
    Loads a CSV file and returns a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
        print(f"[INFO] Loaded dataset: {path} (rows: {len(df)})")
        return df
    except FileNotFoundError:
        print(f"[ERROR] File not found: {path}")
        return None
    except Exception as e:
        print(f"[ERROR] Failed to load CSV: {e}")
        return None


def load_raw_datasets(phishing_path: str, legitimate_path: str):
    """
    Loads phishing.csv and legitimate.csv together.
    Returns a combined DataFrame.
    """
    phishing_df = load_csv(phishing_path)
    legitimate_df = load_csv(legitimate_path)

    if phishing_df is None or legitimate_df is None:
        print("[ERROR] Could not load raw datasets.")
        return None

    combined = pd.concat([phishing_df, legitimate_df], ignore_index=True)
    print(f"[INFO] Combined dataset size: {len(combined)} rows")

    return combined


def load_processed_dataset(path: str):
    """
    Loads processed final_dataset.csv
    """
    return load_csv(path)
