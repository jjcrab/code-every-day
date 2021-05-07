# https://leetcode.com/problems/roman-to-integer/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V(5) and X(10) to make 4 and 9.
# X can be placed before L(50) and C(100) to make 40 and 90.
# C can be placed before D(500) and M(1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


def romanToInt(s):
    # slist = ["I", "V", "X", "L", "C", "D", "M"]
    # dic_indexToVal = {}
    # d_romToIndex = {}
    # l_sToIndex = []
    # sum = 0
    # for i in range(0, len(slist)):
    #     if i % 2 == 0:
    #         val = 10 ** (i//2)
    #     else:
    #         val = 5 * (10 ** ((i-1)//2))
    #     dic_indexToVal[i] = val
    # for i, v in enumerate(slist):
    #     d_romToIndex[v] = i
    # for letter in s:
    #     l_sToIndex.append(d_romToIndex[letter])
    # for i2, v2 in enumerate(l_sToIndex):
    #     if v2 % 2 == 0 and i2+1 < len(l_sToIndex) and (l_sToIndex[i2+1]-v2 == 1 or l_sToIndex[i2+1]-v2 == 2):
    #         sum = sum - dic_indexToVal[v2]
    #     else:
    #         sum = sum + dic_indexToVal[v2]
    # return sum

    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # n = len(s)-1
    # sum = dic[s[n]]
    # while n > 0:
    #     if dic[s[n-1]] < dic[s[n]]:
    #         sum = sum - dic[s[n-1]]
    #     else:
    #         sum = sum + dic[s[n-1]]
    #     n -= 1

    sum = dic[s[-1]]
    for i in reversed(range(len(s)-1)):
        if dic[s[i]] < dic[s[i+1]]:
            sum = sum - dic[s[i]]
        else:
            sum = sum + dic[s[i]]

    return sum


print(romanToInt("MCMXCIV"))
