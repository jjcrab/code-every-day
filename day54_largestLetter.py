# Description
# Given a string S, find the largest alphabetic character, whose both uppercase and lowercase appear in S. The uppercase character should be returned. If there is no such character, return "NO".

# 1 <= len(s) <= 10 ^ 61 <= len(s) <= 10
# 6

# Example
# Input: S = "admeDCAB"
# Output: "D"

# Input: S = "adme"
# Output: "NO"


class Solution:
    """
    @param s: a string
    @return: a string
    """

    def largestLetter(self, s):
        capital = [0 for _ in range(26)]
        small = [0 for _ in range(26)]
        for l in s:
            if ord("a") <= ord(l) <= ord("z"):
                small[ord(l) - ord("a")] += 1
            else:
                capital[ord(l) - ord("A")] += 1

        for i in range(len(capital) - 1, -1, -1):
            if capital[i] > 0 and small[i] > 0:
                return chr(i + ord("A"))
        return "NO"

# if find the first showed uppercase in the same conditions
        # for l in s:
        #     if ord("A") <= ord(l) <= ord("Z"):
        #         if small[ord(l) + 32 - ord("a")] > 0:
        #             return l

# another way to find the first showed uppercase
        # letterset = set()
        # for l in s:
        #     letterset.add(ord(l))

        # print(letterset)

        # for l in s:
        #     if ord("A") <= ord(l) <= ord("Z"):
        #         if ord(l) + 32 in letterset:
        #             return l
