# https: // leetcode.com/problems/valid-palindrome-ii/

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


def validPalindrome(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            remove_right = s[left:right]
            remove_left = s[left+1:right+1]
            return remove_right == remove_right[::-1] or remove_left == remove_left[::-1]
        left += 1
        right -= 1
    return True


print(validPalindrome('abca'))
