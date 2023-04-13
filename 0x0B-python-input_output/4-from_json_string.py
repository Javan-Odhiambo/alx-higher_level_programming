#!/usr/bin/python3
"""
Returns an object represented by a json string
"""

import json


def from_json_string(my_str):
    """converts my_str to a python object"""
    return json.loads(my_str)
