# https: // www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(str):
    new_str = ""
    for i in range(len(str)):
        if str[i].lower() not in {"a", "i", "e", "o", "u"}:
            new_str += str[i]

    return new_str
