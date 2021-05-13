# https: // leetcode.com/problems/length-of-last-word/
# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
# A word is a maximal substring consisting of non-space characters only


def lengthOfLastWord(s):
    # list_s = s.split()
    # print(list_s)
    # if list_s == []:
    #     return 0
    # return len(list_s[-1])
    if not s or s.isspace():
        return 0
    return len(s.split()[-1])


print(lengthOfLastWord(""))
