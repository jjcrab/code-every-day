# https://www.lintcode.com/problem/31/?_from=collection&fromId=161
'''
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length
0 <= nums.length <= 20000<=nums.length<=2000

Example
Example 1:

Input:

nums = []
k = 9
Output:

0
Explanation:

Empty array, print 0.

Example 2:

Input:

nums = [3,2,2,1]
k = 2
Output:

1
Explanation:

the real array is[1,2,2,3].So return 1.

Challenge
Can you partition the array in-place and in O(n)O(n)?
'''


# class Solution:
#     """
#     @param nums: The integer array you should partition
#     @param k: An integer
#     @return: The index after partition
#     """

#     def partitionArray(self, nums, k):
#         if not nums:
#             return 0
#         self.helper(nums, 0, len(nums) - 1)
#         print(nums)
#         for i in range(len(nums)):
#             if nums[i] >= k:
#                 return i
#         return len(nums)

#     def helper(self, nums, start, end):
#         if start >= end:
#             return

#         pivot = nums[(start + end) // 2]
#         left, right = start, end

#         while left <= right:
#             while left <= right and nums[left] < pivot:
#                 left += 1
#             while left <= right and nums[right] > pivot:
#                 right -= 1
#             if left <= right:
#                 nums[right], nums[left] = nums[left], nums[right]
#                 left += 1
#                 right -= 1
#         self.helper(nums, start, right)
#         self.helper(nums, left, end)


# quick select
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        if not nums:
            return 0

        # quick select
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left
