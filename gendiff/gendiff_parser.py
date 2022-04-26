from .stylish_formatter import stylish, change_keys
from .plain_formatter import plain


def compare(d1, d2):    # noqa: C901
    result = {}

    def start(d1, d2, result_cur):
        for key1 in d1:
            key2 = key1 in d2
            is_key1_dict = isinstance(d1[key1], dict)
            is_key2_dict = isinstance(d2[key1], dict) if key2 else None

            if not key2:
                result_cur[key1 + "__minus"] = d1[key1]

            elif is_key1_dict and is_key2_dict:
                result_cur[key1] = {}
                start(d1[key1], d2[key1], result_cur[key1])

            elif not is_key1_dict and not is_key2_dict:
                if d1[key1] != d2[key1]:
                    result_cur[key1 + "__minus"] = d1[key1]
                    result_cur[key1 + "__plus"] = d2[key1]
                else:
                    result_cur[key1 + "__same"] = d1[key1]

            elif is_key1_dict and not is_key2_dict:
                result_cur[key1 + "__minus"] = {}
                result_cur[key1 + "__minus"] = d1[key1]
                result_cur[key1 + "__plus"] = d2[key1]

            elif not is_key1_dict and is_key2_dict:
                result_cur[key1 + "__minus"] = d1[key1]
                result_cur[key1 + "__plus"] = {}
                result_cur[key1 + "__plus"] = d2[key1]

    start(d1, d2, result)
    return compare_second(d1, d2, result)


def compare_second(d1, d2, result):
    total_result = result

    def start(d1, d2, result_cur):
        for key2 in d2:
            key1 = key2 in d1
            is_key1_dict = isinstance(d1[key2], dict) if key1 else None
            is_key2_dict = isinstance(d2[key2], dict)

            if not key1:
                if is_key2_dict:
                    result_cur[key2 + "__plus"] = {}
                    result_cur[key2 + "__plus"] = d2[key2]
                else:
                    result_cur[key2 + "__plus"] = d2[key2]
            elif is_key1_dict and is_key2_dict:
                start(d1[key2], d2[key2], result_cur[key2])

    start(d1, d2, total_result)
    return total_result


def sort_dict(tree):
    result = {}

    def start(tree, result_cur):
        keys = sorted(tree.keys())
        for key in keys:

            is_key_dict = isinstance(tree[key], dict)
            if is_key_dict:
                result_cur[key] = {}
                start(tree[key], result_cur[key])
            else:
                result_cur[key] = tree[key]

    start(tree, result)
    return result


def parser(file1, file2, formatter="stylish"):
    compare_ = compare(file1, file2)
    sort_dict_ = sort_dict(compare_)

    if formatter == "stylish":
        change_keys_ = change_keys(sort_dict_)
        result = stylish(change_keys_)

    if formatter == "plain":
        result = plain(sort_dict_)

    return result
