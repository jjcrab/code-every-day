'''
Description
Find any position of a target number in a sorted array. Return -1 if target does not exist.

Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 1 or 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1
Challenge
O(logn) time
'''


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # binary search
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    # def findPosition(self, nums, target):
    #     # recursion
    #     return self.helper(nums, 0, len(nums) - 1, target)

    # def helper(self, nums, start, end, target):
    #     if start > end:
    #         return -1

    #     mid = (start + end) // 2
    #     if nums[mid] == target:
    #         return mid
    #     if nums[mid] < target:
    #         return self.helper(nums, mid + 1, end, target)

    #     return self.helper(nums, start, mid - 1, target)
