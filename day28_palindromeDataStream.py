# https: // www.lintcode.com/problem/958/
# Description
# There is a data stream coming in, one lowercase letter at a time. Can the arrangement of the current data stream form palindrome string？
def getStream(s):
    if s is None or len(s) == 0:
        return None
    oddcount = 0
    result = [0 for n in range(len(s))]
    letters = [0 for m in range(26)]

    for i in range(len(s)):
        letters[ord(s[i]) - ord('a')] += 1
        if letters[ord(s[i]) - ord('a')] % 2 == 1:
            oddcount += 1
        else:
            oddcount -= 1
        result[i] = 0 if oddcount > 1 else 1

    return result
