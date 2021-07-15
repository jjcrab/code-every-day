# https://leetcode.com/problems/sort-colors/

'''
Description
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

You are not suppose to use the library's sort function for this problem.
You should do it in-place (sort numbers in the original array).
You are not allowed to use counting sort to solve this problem.

Example
Example 1

Input : [1, 0, 1, 2]
Output : [0, 1, 1, 2]
Explanation : sort it in-place
Challenge
Could you come up with an one-pass algorithm using only O(1) space?
'''


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """

    def sortColors(self, nums):
        # counting sort
        color = {0: 0, 1: 0, 2: 0}
        for num in nums:
            color[num] += 1

        index = 0
        for i in range(len(color)):
            for j in range(color[i]):
                nums[index] = i
                index += 1
        return nums

    #     # quick sort
    #     second_start = self.quickSort(nums, 0, len(nums) - 1, 1)
    #     self.quickSort(nums, second_start, len(nums) - 1, 2)
    #     return nums

    # def quickSort(self, nums, start, end, pivot):

    #     left, right = start, end

    #     while left <= right:
    #         while left <= right and nums[left] < pivot:
    #             left += 1
    #         while left <= right and nums[right] >= pivot:
    #             right -= 1
    #         if left <= right:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1

    #     return left


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """

    def sortColors(self, nums):
        # three pointers
        left, cur, right = 0, 0, len(nums) - 1
        while cur <= right:
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
                continue
            else:
                nums[right], nums[cur] = nums[cur], nums[right]
                right -= 1

        return nums
