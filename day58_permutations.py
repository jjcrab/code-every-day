# https: // leetcode.com/problems/permutations/

'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    # def permute(self, nums):
    #     # use dfs
    #     # edge case:
    #     result = []
    #     if not nums:
    #         return [[]]
    #     self.dfs(nums, set(), [], result)
    #     return result

    # def dfs(self, nums, visited, permutation, result):
    #     # end case
    #     if len(permutation) == len(nums):
    #         result.append(list(permutation))
    #         return

    #     for num in nums:
    #         if num in visited:
    #             continue
    #         permutation.append(num)
    #         visited.add(num)
    #         self.dfs(nums, visited, permutation, result)
    #         visited.remove(num)
    #         permutation.pop()


# another way
    def permute(self, nums):
        # use dfs
        # edge case:
        result = []
        # if not nums:
        #     return [[]]
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, permutation, result):
        # end case
        if not nums:
            result.append(permutation)
            return

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], permutation + [nums[i]], result)
