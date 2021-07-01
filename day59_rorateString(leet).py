# https://leetcode.com/problems/rotate-string/

'''
We are given two strings, s and goal.

A shift on s consists of taking string s and moving the leftmost character to the rightmost position. For example, if s = 'abcde', then it will be 'bcdea' after one shift on s. Return true if and only if s can become goal after some number of shifts on s.

Example 1:
Input: s = 'abcde', goal = 'cdeab'
Output: true

Example 2:
Input: s = 'abcde', goal = 'abced'
Output: false
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if not s and not goal:
            return True

        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if s[i] != goal[0]:
                continue

            if s[i:] + s[:i] == goal:
                return True
            else:
                continue

        return False


# Another way
# class Solution(object):
#     def rotateString(self, A, B):
#         return len(A) == len(B) and B in A+A
