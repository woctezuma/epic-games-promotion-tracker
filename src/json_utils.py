import json
from pathlib import Path


def load_json(fname):
    with open(fname, encoding='utf8') as f:
        data = json.load(f)
    return data


def load_json_failsafe(fname):
    try:
        data = load_json(fname)
    except FileNotFoundError:
        data = {}
    return data


def save_json(data, fname, prettify=False):
    Path(fname).parent.mkdir(parents=True, exist_ok=True)

    with open(fname, 'w', encoding='utf8') as f:
        if prettify:
            json.dump(data, f, indent=2, sort_keys=True)
        else:
            json.dump(data, f)
