# https: // leetcode.com/problems/plus-one/

# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

def plusOne(digits):
    # method 1
    # sum = 0
    # for v in digits:
    #     sum = sum*10 + v

    # sum = sum + 1
    # list_result = []

    # while sum > 0:
    #     last = sum % 10
    #     list_result.append(last)
    #     sum = sum//10

    # return list_result[::-1]

    # method 2
    # sum = 0
    # for v in digits:
    #     sum = sum * 10 + v

    # sum += 1
    # result = []
    # for i in str(sum):
    #     result.append(int(i))

    # return result

    # method 3
    if digits[-1] != 9:
        digits[-1] = digits[-1] + 1
        return digits
    for i in reversed(range(len(digits))):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits


print(plusOne([1, 2, 3]))
print(plusOne([9, 9, 9]))
