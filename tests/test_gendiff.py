from gendiff.generate_diff import generate_diff
import json


def test_generate_diff():
    result = open("tests/fixtures/result.json")
    
    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") == result.read()
    result.close()