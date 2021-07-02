# https: // leetcode.com/problems/permutations-ii/solution/

'''
Description
Given a list of numbers with duplicate numbers in it. Find all unique permutations of it.

Example
Example 1:

Input:

nums = [1,1] 
Output:

[ 
  [1,1] 
] 
Explanation:

The different arrangement of [1,1] is only [1,1].

Example 2:

Input:

nums = [1,2,2] 
Output:

[ 
  [1,2,2], 
  [2,1,2], 
  [2,2,1] 
] 
Explanation:

The different arrangements of [1,2,2] are [1,2,2],[2,1,2]and [2,2,1].

Challenge
Using recursion to do it is acceptable. If you can do it without recursion, that would be great!

'''


class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # result = set()
        result = []
        nums.sort()
        self.dfs(nums, [], result)
        # return list(result)
        return result

    def dfs(self, nums, permutation, result):
        # end case
        if not nums:
            result.append(permutation)
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], permutation + [nums[i]], result)


# method 2

    def permuteUnique(self, nums):
        # use dfs
        # edge case:
        result = []
        if not nums:
            return [[]]
        nums.sort()
        print(nums)
        # visited cannot be a set because has duplicate numbers
        self.dfs(nums, {}, [], result)
        return result

    def dfs(self, nums, visited, permutation, result):
        # end case
        if len(permutation) == len(nums):
            result.append(permutation[:])
            return

        for i in range(len(nums)):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
                continue
            permutation.append(nums[i])
            visited[i] = nums[i]
            self.dfs(nums, visited, permutation, result)
            visited.pop(i)
            permutation.pop()
