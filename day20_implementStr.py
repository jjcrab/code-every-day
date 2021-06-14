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
        # res = haystack.find(needle)
        return res
    else:
        return -1

    # s_len = len(source)
    # t_len = len(target)

    # if not target:
    #     return 0
    # if t_len > s_len:
    #     return -1

    # for i in range(s_len - t_len + 1):
    #     j = 0
    #     while j < t_len:
    #         if target[j] != source[i+j]:
    #             break
    #         j += 1
    #     if j == t_len:
    #         return i
    # return -1


print(strStr('hello', "lo"))
