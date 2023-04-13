#!/usr/bin/python3
"""
Writing an object to a file using json rep.
"""

import json


def save_to_json_file(my_obj, filename):
    """Saves  my_obj to filename using json"""
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
