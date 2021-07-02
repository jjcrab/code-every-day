'''
Description
Given a set with distinct integers, return all possible subsets.

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Example
Example 1:

Input:

nums = [0] 
Output:

[ 
  [], 
  [0] 
] 
Explanation:

The subsets of [0] are only [] and [0].

Example 2:

Input:

nums = [1,2,3] 
Output:

[ 
  [3], 
  [1], 
  [2], 
  [1,2,3], 
  [1,3], 
  [2,3], 
  [1,2], 
  [] 
] 
Explanation:

The subsets of [1,2,3] are [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].

Challenge
Can you do it in both recursively and non-recursively?
'''


class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        if nums is None:
            return nums
        nums.sort()
        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, index, subset, result):
        # if index == len(nums):
        #     return

        result.append(list(subset))

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, result)
            subset.pop()
