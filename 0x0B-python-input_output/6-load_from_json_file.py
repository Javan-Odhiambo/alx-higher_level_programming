#!/usr/bin/python3
"""
Returns an object from json string
"""

import json


def load_from_json_file(filename):
    """Creates object from filename"""
    with open(filename, 'r') as f:
        return json.load(f)
