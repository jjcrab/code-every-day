# https: // leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 
'''


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         # binary search

#         first, last = -1, -1

#         if not nums:
#             return [-1, -1]

#         # find the last
#         start, end = 0, len(nums) - 1
#         while start + 1 < end:
#             mid = (start + end) // 2
#             if nums[mid] < target:
#                 start = mid
#             elif nums[mid] == target:
#                 start = mid
#             else:
#                 end = mid
#         if nums[end] == target:
#             last = end
#         elif nums[start] == target:
#             last = start
#         else:
#             last = -1

#         # find the first
#         start, end = 0, len(nums) - 1
#         while start + 1 < end:
#             mid = (start + end) // 2
#             if nums[mid] < target:
#                 start = mid
#             elif nums[mid] == target:
#                 end = mid
#             else:
#                 end = mid

#         if nums[start] == target:
#             first = start
#         elif nums[end] == target:
#             first = end
#         else:
#             first = -1

#         return [first, last]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search

        if not nums:
            return [-1, -1]

        lower_bound = self.findBound(nums, 0, len(nums) - 1, target, True)
        upper_bound = self.findBound(nums, 0, len(nums) - 1, target, False)

        return [lower_bound, upper_bound]

    def findBound(self, nums, start, end, target, flag):
        first, last = -1, -1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif not flag and nums[mid] == target:
                start = mid
            elif flag and nums[mid] == target:
                end = mid
            else:
                end = mid

        if not flag:
            if nums[end] == target:
                last = end
            elif nums[start] == target:
                last = start
            else:
                last = -1
            return last

        if flag:
            if nums[start] == target:
                first = start
            elif nums[end] == target:
                first = end
            else:
                first = -1
            return first
