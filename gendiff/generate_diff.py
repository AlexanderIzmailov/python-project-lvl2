import json


def true_and_false(element):
    element = str(element)
    if element == "True" or element == "False":
        return element[0:1].lower() + element[1:]
    else:
        return element


def generate_diff(f1, f2):
    file1 = json.load(open(f1))
    file2 = json.load(open(f2))

    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    uniq_keys = sorted(set(keys1) | set(keys2))

    result = "{\n"
    for n in uniq_keys:
        if n in keys1 and n in keys2:
            resf1 = true_and_false(file1[n])
            resf2 = true_and_false(file2[n])
            if file1[n] == file2[n]:
                result += "\t" + str(n) + ": " + resf1 + "\n"
            else:
                result += "\t" + "- " + str(n) + ": " + resf1 + "\n"
                result += "\t" + "+ " + str(n) + ": " + resf2 + "\n"
        elif n in keys1 and n not in keys2:
            result += "\t" + "- " + str(n) + ": " + resf1 + "\n"
        else:
            result += "\t" + "+ " + str(n) + ": " + resf2 + "\n"

    result += "}"
    print(result)
    return result
