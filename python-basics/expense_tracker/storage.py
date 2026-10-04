"""Storage helpers for the Smart Expense Tracker.

This module is responsible for reading and writing JSON data files.
It guards against missing or corrupt files so the application always
starts with valid data.
"""

import json
import os


def load_json(filename, default):
    """Load JSON from *filename* or return *default* if it does not exist."""
    if not os.path.exists(filename):
        return default
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print(f"Warning: {filename} could not be read. Starting fresh.")
        return default


def save_json(filename, data):
    """Save *data* to *filename* as formatted JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
