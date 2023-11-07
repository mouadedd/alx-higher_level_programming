#!/usr/bin/python3
'''this is a test'''


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    itm = load_from_json_file("add_item.json")
except FileNotFoundError:
    itm = []
for ar in argv[1:]:
    itm.append(ar)
save_to_json_file(itm, "add_item.json")
