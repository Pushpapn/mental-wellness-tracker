import json
import os

DATA_FILE = "entries.json"

def save_entry(entry):
    data = load_entries()
    data.append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def load_entries():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
