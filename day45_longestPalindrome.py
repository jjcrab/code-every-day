# https://leetcode.com/problems/longest-palindrome/

'''
Description
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Assume the length of given string will not exceed 100000.

Example
Example 1:

Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.
'''

import collections


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        odd = 0
        for i in collections.Counter(s).values():
            if i % 2:
                odd += 1
        return len(s) - odd + 1 if odd else len(s)

        # ans = 0
        # cnt = collections.Counter(s)
        # for i in cnt.values():
        #     ans += i // 2 * 2
        #     if ans % 2 == 0 and i % 2 == 1:
        #         ans += 1
        # return ans
