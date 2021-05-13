# https: // leetcode.com/problems/sqrtx/
# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

import math


def mySqrt(x):
    # return math.floor(math.sqrt(x))
    if x < 2:
        return x
    left = 2
    right = x//2

    while left <= right:
        pivot = (left + right)//2
        if pivot**2 == x:
            return pivot
        elif pivot ** 2 < x:
            left = pivot + 1
        else:
            right = pivot - 1
    return right


print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(10))
