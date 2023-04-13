#!/usr/bin/python3
"""
Scripts that adds all arguments to json file
"""

from sys import argv
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_l = load(filename)
except:
    json_l = []

for arg in argv[1:]:
    json_l.append(arg)

save(json_l, filename)
