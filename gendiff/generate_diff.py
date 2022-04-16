from .gendiff_parser import parser
import json


def generate_diff(f1, f2):
    f1_open = open(f1)
    f2_open = open(f2)

    if len(f1_open.read()) == 0 or len(f2_open.read()) == 0:
        return

    f1_open.close()
    f2_open.close()

    file1 = json.load(open(f1))
    file2 = json.load(open(f2))

    keys1 = list(file1.keys())
    keys2 = list(file2.keys())

    if len(keys1) == 0 and len(keys2) == 0:
        return

    result = parser(file1, file2)

    print(result)
    return result
