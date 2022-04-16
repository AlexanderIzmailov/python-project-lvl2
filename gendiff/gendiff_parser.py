def true_and_false(element):
    element = str(element)
    if element == "True" or element == "False":
        return element.lower()
    else:
        return element


def parser(data1, data2):
    keys1 = list(data1)
    keys2 = list(data2)
    uniq_keys = sorted(set(keys1) | set(keys2))

    result = "{\n"
    for n in uniq_keys:
        val1_lower = true_and_false(data1.get(n))
        val2_lower = true_and_false(data2.get(n))

        if n in keys1 and n in keys2:
            if data1[n] == data2[n]:
                result += "\t  {}: {}\n".format(str(n), val1_lower)
            else:
                result += "\t- {}: {}\n".format(str(n), val1_lower)
                result += "\t+ {}: {}\n".format(str(n), val2_lower)
        elif n in keys1 and n not in keys2:
            result += "\t- {}: {}\n".format(str(n), val1_lower)
        else:
            result += "\t+ {}: {}\n".format(str(n), val2_lower)

    result += "}"
    return result
