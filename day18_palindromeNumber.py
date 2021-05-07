# https: // leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

def isPalindrome(x):
    # if x < 0:
    #     return False
    # else:
    #     x = str(x)
    #     right = len(x)-1
    #     left = 0
    #     while right > left:
    #         if x[right] == x[left]:
    #             right -= 1
    #             left += 1
    #         else:
    #             return False

    #     return True

    # return str(x)[::-1] == str(x)

    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    else:
        rev = 0
        while x > rev:
            rev = rev*10 + x % 10
            x = x//10
        return x == rev or x == rev//10


# '''
# x = 123
# orig = 121
# rev = 0
# while x > 0:
#     rev = rev*10 + x%10
#     x = x//10

# x   x%10 rev  x//10
# 123  3      3    12
# 12   2     32     1
# 1    1     321    0

# rev = 121

# '''
print(isPalindrome(12321))
