# Reverse ASCII Encoded Strings
# Description
# Given a string which encode by ascii(For example, "ABC" can encode to "656667"), You need to write a function that take an encoded string as input and returns reversed decoded string.

# You can assume there is only uppercase letters in answer string.

# Example
# Example1

# Input: "7976766972"
# Output: "HELLO"
# Example2

# Input: "656667"
# Output: "CBA"

def reverseAsciiEncodedString(encodeString):

    result = ""
    for i in range(0, len(encodeString), 2):
        decodeLetter = chr(
            int(encodeString[i])*10 + int(encodeString[i+1]))
        result += decodeLetter
    return result[::-1]


'''
Decrease To Be Palindrome

Description
Given a string s with a-z. We want to change s into a palindrome with following operations:

1. change 'z' to 'y';
2. change 'y' to 'x';
3. change 'x' to 'w';
................
24. change 'c' to 'b';
25. change 'b' to 'a';
Returns the number of operations needed to change s to a palindrome at least.
'''


class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """

    def numberOfOperations(self, s):
        # Write your code here
        left = 0
        right = len(s)-1
        step = 0
        while left < right:
            step += abs(ord(s[right])-ord(s[left]))
            left += 1
            right -= 1
        return step


# Longest Semi Alternating Substring
'''
Description
You are given a string SS of length NN containing only characters a and b. A substring (contiguous fragment) of SS is called a semi-alternating substring if it does not contain three identical consecutive characters. In other words, it does not contain either aaa or bbb substrings. Note that whole SS is its own substring.

Write a function, which given a string SS, returns the length of the longest semi-alternating substring of SS.

NN is an integer within the range [1,200\,000][1,200000];
string SS consists only of the characters a and/or b.
Example
Example 1

Input: "baaabbabbb"
Output: 7
Explanation: "aabbabb" is the longest semi-alternating substring.
Example 2

Input: "babba"
Output: 5
Explanation: Whole S is semi-alternating.
Example 3

Input: "abaaaa"
Output: 4
Explanation: "abaa" is the longest semi-alternating substring.
'''


class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """

    def longestSemiAlternatingSubstring(self, s):
        # write your code here

        if s is None or len(s) == 0:
            return 0

        maxlen = 1
        count = 1
        left = 0

        for right in range(1, len(s)):
            if s[right-1] == s[right]:
                count += 1
                if count == 3:
                    left = right - 1
                    count = 2
            else:
                count = 1

            maxlen = max(maxlen, right-left+1)
        return maxlen
