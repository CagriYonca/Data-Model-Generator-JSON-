import json
import sys


FILE_PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]

def json_parser(input_json, data_structure):
    '''Parsing keys inside a json'''
    for key, value in input_json.items():
        if key not in data_structure.keys():
            if isinstance(value, dict):
                if key not in data_structure.keys():
                    data_structure[key] = {}
                data_structure[key] = json_parser(input_json[key], data_structure[key])
            else:
                data_structure[key] = type(value).__name__
        else:
            if type(value).__name__ != data_structure[key]:
                if isinstance(type(data_structure[key]), dict) and type(value).__name__ == 'dict':
                    pass
                elif isinstance(type(data_structure[key]), list):
                    if type(value).__name__ not in data_structure[key]:
                        data_structure[key].append(type(value).__name__)
                    else:
                        data_structure[key] = [data_structure[key]] + [type(value).__name__]
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
