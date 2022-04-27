from .stylish_formatter import true_false_none


def is_next_same(key, tree):
    keys = list(tree.keys())
    key_index = keys.index(key)
    next_index = key_index + 1
    if next_index >= len(keys):
        return False, None, None

    key_split = key.split("__")
    next_key = keys[next_index]
    next_key_split = next_key.split("__")
    if key_split[0] == next_key_split[0]:
        return True, isinstance(tree[next_key], dict), tree[next_key]
    else:
        return False, None, None


def plain(tree):    # noqa: C901
    def start(tree, cur_result, parent=None, pass_next=False):
        for key in tree:

            if pass_next:
                pass_next = False
                continue

            split_key = key.split("__")
            last = split_key[-1]
            clear_key = split_key[0]
            key_value = tree[key]
            is_key_dict = isinstance(key_value, dict)

            path = parent + "." + clear_key if parent else clear_key

            next_same, is_next_dict, next_key_value = is_next_same(key, tree)

            next_key_value = true_false_none(next_key_value)

            if not next_same and is_key_dict and last == clear_key:
                cur_result = start(tree[key], cur_result, path)
                continue

            if last == "same":
                continue

            if is_key_dict:
                res1 = "[complex value]"
            else:
                res1 = "'{}'".format(true_false_none(key_value))

            if not next_same:
                if last == "minus":
                    end_row = "was removed\n"
                if last == "plus":
                    end_row = "was added with value: {}\n".format(res1)
            else:

                if is_next_dict:
                    res2 = "[complex value]"
                else:
                    res2 = "'{}'".format(next_key_value)

                if last == "minus":
                    end_row = "was updated. From {} to {}\n".format(res1, res2)
                pass_next = True

            cur_result += "Property '{}' {}".format(path, end_row)

        return cur_result
    
    result = start(tree, "")
    
    return result.strip()
