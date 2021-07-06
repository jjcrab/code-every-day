'''
Description
Given a collection of integers that might contain duplicate numbers, return all possible subsets.

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
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

nums = [1,2,2]
Output:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Explanation:

The distinct subsets of [1,2,2] are [], [1], [2], [1,2], [2,2], [1,2,2].

Challenge
Can you do it in both recursively and non-recursively?
'''


class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        if nums is None:
            return result
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, index, subset, result):
        result.append(subset[:])
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i > index:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, result)
            subset.pop()


# method 2 use hashmap
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        if nums is None:
            return result
        self.dfs(nums, 0, [], result, {})
        return result

    def dfs(self, nums, index, subset, result, visited):
        result.append(subset[:])
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
                continue
            subset.append(nums[i])
            visited[i] = nums[i]
            self.dfs(nums, i + 1, subset, result, visited)
            visited.pop(i)
            subset.pop()
