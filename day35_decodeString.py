# https: // leetcode.com/problems/decode-string/
'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''


class Solution:
    def decodeString(self, s: str) -> str:
        # create a stack
        stack = []
        for i in s:
            # if not "]", append
            if i != ']':
                stack.append(i)
            # if "]", pop till last digit
            else:
                # pop if alpha
                # cant use string since don't want to reserse the letters in one element
                # letters = ""
                letters = []
                while stack[-1].isalpha():
                    # letters += stack.pop()
                    letters.append(stack.pop())
                # pop "["
                stack.pop()
                # pop if digit
                # more than one digit
                num = 0
                p = 0
                while stack and stack[-1].isdigit():
                    num += int(stack.pop())*(10**p)
                    p += 1
                # times
                letter = ''.join(letters[::-1])
                letter *= num
                # put reversed string back to the stack
                stack.append(letter)
            # print(stack, i)
        # change stack to string
        return "".join(stack)
