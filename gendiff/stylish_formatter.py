def true_false_none(element):
    element = str(element)
    if element == "True" or element == "False":
        return element.lower()
    elif element == "None":
        return "null"
    else:
        return element


def stylish(tree):
    level = 1
    sep = "\t"

    def start(tree, cur_result, cur_level, sep):
        for key in tree.keys():
            is_key_dict = isinstance(tree[key], dict)

            if is_key_dict:
                cur_result += "{}{}: {{\n".format(cur_level * sep, key)
                cur_level += 1
                cur_result = start(tree[key], cur_result, cur_level, sep)
                cur_level -= 1
                cur_result += "{}}}\n".format(cur_level * sep)
            else:
                value = true_false_none(tree[key])
                cur_result += "{}{}: {}\n".format(cur_level * sep, key, value)
        return cur_result

    return start(tree, "\n{\n", level, sep) + "}"


def change_keys(tree):
    result = {}

    def start(tree, cur_result):
        for key in tree:
            is_key_dict = isinstance(tree[key], dict)
            split_key = key.split("__")
            if split_key[-1] == "minus":
                result_key = "- " + split_key[0]
            elif split_key[-1] == "plus":
                result_key = "+ " + split_key[0]
            else:
                result_key = "  " + split_key[0]

            if is_key_dict:
                cur_result[result_key] = {}
                start(tree[key], cur_result[result_key])
            else:
                cur_result[result_key] = tree[key]

    start(tree, result)
    return result
