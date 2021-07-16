'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        index_remove = set()  # record the index of parentheses needed to be removed
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                # need to record the index also
                stack.append(["(", i])
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    index_remove.add(i)
        # if stack is not empty
        while stack:
            index_remove.add(stack.pop()[1])

        # build the string
        # method 1: replace the element which need to be removed
#         # change s to list
#         s_list = list(s)

#         # replace the element need to remove to " "
#         for i in range(len(s_list)):
#             if i in index_remove:
#                 s_list[i] = " "

#         # turn str to list and remove the space
#         return "".join(s_list).replace(" ", "")

        # method 2: put the element which can't be removed to an empty list
        s_list = []
        for i, l in enumerate(s):
            if i not in index_remove:
                s_list.append(l)

        return "".join(s_list)
