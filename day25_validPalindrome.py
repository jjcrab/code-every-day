# https: // leetcode.com/problems/valid-palindrome/
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
def isPalindrome(s):
    # s_lower = s.lower()
    # s_list = list(s_lower)
    # new_list = []
    # for letter in s_list:
    #     if letter.isalnum():
    #         new_list.append(letter)
    # return new_list == new_list[::-1]

    # s = [c.lower() for c in s if c.isalnum()]
    # return s == s[::-1]

    # left, right = 0, len(s)-1
    # while left < right:
    #     if not s[left].isalnum():
    #         left += 1
    #     if not s[right].isalnum():
    #         right -= 1
    #     if s[left].isalnum() and s[right].isalnum():
    #         if s[left].lower() == s[right].lower():
    #             left += 1
    #             right -= 1
    #         else:
    #             return False
    # return True

    s = ''.join(c for c in s if c.isalnum()).lower()
    start, end = 0, len(s)-1
    while (start < end):
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("a"))
print(isPalindrome(" "))
