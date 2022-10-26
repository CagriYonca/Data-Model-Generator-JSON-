import json
import sys


FILE_PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]

def json_parser(input_json, data_structure):
    '''Parsing keys from a json'''
    for key, value in input_json.items():
        if key not in data_structure.keys():
            if isinstance(value, dict):
                data_structure[key] = {}
                data_structure[key] = json_parser(value, data_structure[key])
            else:
                data_structure[key] = type(value).__name__
        else:
            if type(value).__name__ == type(data_structure[key]).__name__:
                if type(data_structure[key]).__name__ == 'dict':
                    data_structure[key] = json_parser(value, data_structure[key])
    return data_structure

with open(FILE_PATH, encoding='utf-8') as f:
    data = []
    for json_object in f:
        data.append(json.loads(json_object))
    json_structure = {}
    for current_dict in data:
        json_structure = json_parser(current_dict, json_structure)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as of:
        of.write(json.dumps(json_structure, indent=4))
