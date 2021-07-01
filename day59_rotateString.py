'''
Description
Given a string of char array and an offset, rotate the string by offset in place. (from left to right).
In different languages, str will be given in different ways. For example, the string "abc" will be given in following ways:

Java: char[] str = {'a', 'b', 'c'};
Python：str = ['a', 'b', 'c']
C++：string str = "abc";
offset >= 0
the length of str >= 0
In place means you should change strings in the function. You don't return anything.

Example
Example 1:

Input:

str = ""abcdefg"
offset = 3
Output:

"efgabcd"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".

Example 2:

Input:

str = ""abcdefg"
offset = 0
Output:

"abcdefg"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "abcdefg".

Example 3:

Input:

str = ""abcdefg"
offset = 1
Output:

"gabcdef"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "gabcdef".

Example 4:

Input:

str = ""abcdefg"
offset = 2
Output:

"fgabcde"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "fgabcde".

Example 5:

Input:

str = ""abcdefg"
offset = 10
Output:

"efgabcd"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".

'''


class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, str, offset):
        if str:
            offset = offset % len(str)
        temp = str[len(str) - offset:] + str[:len(str) - offset]
        for i in range(len(temp)):
            str[i] = temp[i]

# method 2: use two str
# class Solution:
#     # @param s: a list of char
#     # @param offset: an integer
#     # @return: nothing
#     def rotateString(self, s, offset):
# 	    # write you code here
#         if len(s) > 0:
#             offset = offset % len(s)

#         temp = (s + s)[len(s) - offset: 2 * len(s) - offset]

#         for i in xrange(len(temp)):
#             s[i] = temp[i]
