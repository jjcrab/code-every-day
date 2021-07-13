'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # use dp
        if not s:
            return True
        if not wordDict:
            return False
        # start from True so length of list dp is 1 more than length of s
        dp = [False] * (len(s) + 1)
        dp[0] = 1
        max_len = max([len(word) for word in wordDict])
        # for each letter
        for i in range(1, len(dp)):
            # from previous each True to current index
            for j in range(max(i - max_len, 0), i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]
