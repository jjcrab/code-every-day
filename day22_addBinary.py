# https: // leetcode.com/problems/add-binary/
# Given two binary strings a and b, return their sum as a binary string.


def addBinary(a, b):
    # return bin(int(a, 2)+int(b, 2))[2:]

    # n = max(len(a), len(b))
    # a, b = a.zfill(n), b.zfill(n)

    # carry = 0
    # answers = []
    # for i in reversed(range(n)):
    #     if a[i] == '1':
    #         carry += 1
    #     if b[i] == '1':
    #         carry += 1

    #     if carry % 2 == 0:
    #         answers.append('0')
    #     else:
    #         answers.append('1')

    #     carry = carry//2

    # if carry == 1:
    #     answers.append("1")

    # return ''.join(reversed(answers))

    x, y = int(a, 2), int(b, 2)
    while y:
        x, y = x ^ y, (x & y) << 1
    return bin(x)[2:]


print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
