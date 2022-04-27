from gendiff.generate_diff import generate_diff


def test_generate_diff_json():
    result = open("tests/fixtures/result")

    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") == result.read()
    result.close()


def test_generate_diff_yml():
    result = open("tests/fixtures/result")

    assert generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yaml") == result.read()
    result.close()


def test_generate_diff_empty():
    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/empty.json") is None


def test_generate_big_diff_json():
    result = open("tests/fixtures/compare_2json_result.json")

    assert generate_diff("tests/fixtures/file1_big.yaml", "tests/fixtures/file2_big.json") == result.read()
    result.close()


def test_plain_big_diff_json():
    result = open("tests/fixtures/plain_result")

    assert generate_diff("tests/fixtures/file1_big.yaml", "tests/fixtures/file2_big.json", "plain") == result.read()
    result.close()


def test_json_big_diff_json():
    result = open("tests/fixtures/json_result")

    assert generate_diff("tests/fixtures/file1_big.yaml", "tests/fixtures/file2_big.json", "json") == result.read()
    result.close()
