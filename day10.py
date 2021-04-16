# Your goal is to create a function that removes the first and last character of a string. You're given one parameter, the original string. All input strings will be two characters or longer.

def remove_char(s):
    arrs = list(s)
    arrs.pop(0)
    arrs.pop()
    return ''.join(arrs)
    # return s[1:-1]


# Find the greatest common divisor of two positive integers without using a Python library. The integers may be large, so after you write a brute force solution, try to find a more efficient solution.
# The inputs x and y are always greater or equal to 1, so the greatest common divisor will always be an integer that is greater than or equal to 1.

def mygcd(x, y):
    if y == 0:
        return x
    else:
        return mygcd(y, x % y)
    # return math.gcd(x, y)


# Given a string of words, you need to find the highest scoring word. Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string. If two words score the same, return the word that appears first in the original string. All letters will be lowercase and all inputs will be valid.

def highest(s):
    # slist = s.split(' ')
    # sdic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
    #     'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    peak = [0, '']
    for word in s.split():
        ss = sum(ord(x)-96 for x in word)
        if ss > ans[0]:
            peak[0] = ss
            peak[1] = word
    return peak[1]
