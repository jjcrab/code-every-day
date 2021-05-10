# https: // leetcode.com/problems/implement-strstr/

def strStr(haystack, needle):
    if needle == "":
        return 0
    # for i in range(len(haystack)-len(needle)+1):
    #     if haystack[i:i+len(needle)] == needle:
    #         print('test')
    #         return i

    # print('nottest')
    # return -1
    if needle in haystack:
        res = haystack.index(needle)
        res = haystack.find(needle)
        return res
    else:
        return -1


print(strStr('hello', "lo"))
