# https://leetcode.com/problems/longest-palindromic-substring/submissions/

'''
Description
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Example
Example 1:

Input:"abcdzdcab"
Output:"cdzdc"
Example 2:

Input:"aba"
Output:"aba"
Challenge
O(n2) time is acceptable. Can you do it in O(n) time.

'''


# class Solution:
#     """
#     @param s: input string
#     @return: a string as the longest palindromic substring
#     """

#     def longestPalindrome(self, s):
#         # edge case
#         if not s:
#             return ""
#         # back to back two pointers, loop through each letter as middle line
#         # set a maxlength and maxstring
#         max_length = 0
#         max_str = ""
#         s_len = len(s)
#         for middle in range(s_len):
#             # odd number
#             left, right = middle, middle
#             while left >= 0 and right < s_len and s[left] == s[right]:
#                 if max_length < right - left + 1:
#                     max_length = right - left + 1
#                     max_str = s[left:right+1]
#                 left -= 1
#                 right += 1

#             # even number
#             left, right = middle, middle + 1
#             while left >= 0 and right < s_len and s[left] == s[right]:
#                 if max_length < right - left + 1:
#                     max_length = right - left + 1
#                     max_str = s[left: right + 1]
#                 left -= 1
#                 right += 1

#         return max_str


class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        result = ""
        # edge case
        if not s:
            return ""

        # back to back two pointers, loop through each letter as middle line
        for middle in range(len(s)):
            result = max(self.helper(middle, middle, s), self.helper(
                middle, middle + 1, s), result, key=len)
        return result

    def helper(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
