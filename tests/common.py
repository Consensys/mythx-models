import json
from pathlib import Path


def get_test_case(path):
    with open(str(Path(__file__).parent / path)) as f:
        json_data = f.read()
        dict_data = json.loads(json_data)
    return json_data, dict_data
