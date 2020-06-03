#!/usr/bin/python3
"""
script that adds all arguments to a Python
list, and then save them to a file
"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
new_items = argv[1:]
try:
    current_items = load_from_json_file(filename)
except FileNotFoundError:
    current_items = []
my_list = current_items + new_items
save_to_json_file(my_list, filename)
