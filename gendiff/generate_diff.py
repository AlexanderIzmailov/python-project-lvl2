from .gendiff_parser import parser
import json
import yaml


def open_format(file):
    if file.endswith(".yml") or file.endswith(".yaml"):
        return yaml.safe_load(open(file))
    if file.endswith(".json"):
        return json.load(open(file))


def generate_diff(f1, f2, formatter="stylish"):
    with open(f1) as f1_open:
        with open(f2) as f2_open:
            if len(f1_open.read()) == 0 or len(f2_open.read()) == 0:
                return

    file1 = open_format(f1)
    file2 = open_format(f2)

    keys1 = list(file1.keys())
    keys2 = list(file2.keys())

    if len(keys1) == 0 and len(keys2) == 0:
        return

    result = parser(file1, file2, formatter)

    print(result)
    return result
