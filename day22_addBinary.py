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


# cleaner way
class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """

    def addBinary(self, a, b):

        res = ''
        carry = 0
        end_a = len(a) - 1
        end_b = len(b) - 1

        while end_a >= 0 or end_b >= 0:
            num_a = int(a[end_a]) if end_a >= 0 else 0
            num_b = int(b[end_b]) if end_b >= 0 else 0

            cur_sum = num_a + num_b + carry
            # should be "%2", not ""==2"
            if cur_sum % 2 == 0:
                res += "0"
                print(f"res is {res}")
            else:
                res += "1"
            carry = cur_sum // 2
            end_a -= 1
            print(end_a)
            end_b -= 1
            print(end_b)

        if carry:
            res += "1"

        return res[::-1]


# use built-in:
    # return'{0:b}'.format(int(a, 2) + int(b, 2))
