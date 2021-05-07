# https: // leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    # len_list = []
    # for l in strs:
    #     length = len(l)
    #     len_list.append(length)
    # len_min = min(len_list)

    # result = ""

    # for i in range(len_min):
    #     for j in range(len(strs)-1):
    #         if strs[j][i] != strs[j+1][i]:
    #             return result
    #     result = result + strs[0][i]

    # return result

    short_word = min(strs, key=len)
    for x in range(len(short_word)):
        letter = short_word[x]
        for word in strs:
            if word[x] != letter:
                return short_word[:x]
    return short_word


print(longestCommonPrefix(["flower", "flow", "flight"]))
