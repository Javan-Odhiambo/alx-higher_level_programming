#!/usr/bin/python3
"""
returns JSON representation of an object(string)
"""

import json


def to_json_string(my_obj):
    """returns the json representation of my_obj"""
    return json.dumps(my_obj)
