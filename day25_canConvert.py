# https: // www.lintcode.com/problem/1540 /?_from = ladder & fromId = 184

# Description
# Given two string S and T, determine if S can be changed to T by deleting some letters(including 0 letter)

def canConvert(s, t):
    if s is None:
        return False
    index = 0
    for letter in s:
        if letter == t[index]:
            index += 1
            if index == len(t):
                return True


print(canConvert('lintcode', 'ide'))
print(canConvert(None, 'null'))
