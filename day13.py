# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(s):
    result = ""
    for i in range(len(s)):
        letter = f'{s[i].upper()}{s[i].lower()*i}'
        result = result + letter + "-"
    return result[0:len(result)-1]


# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
