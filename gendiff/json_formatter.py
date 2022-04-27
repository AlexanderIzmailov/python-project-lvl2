from .stylish_formatter import true_false_none
import json


def true_false_none_for_tree(tree):
    result = {}

    def start(tree, result):
        for key in tree:
            if isinstance(tree[key], dict):
                result[key] = {}
                start(tree[key], result[key])
            else:
                result[key] = true_false_none(tree[key])
    start(tree, result)

    return json.dumps(result, indent=4)
