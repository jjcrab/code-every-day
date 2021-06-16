# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.


# Example 1:

# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
# Output: 4


class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, k, nums):

        # nums.sort(reverse = True)
        # return nums[k-1]

        # quick select
        if not nums or k < 1 or k > len(nums):
            return None
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, start, end, k):
        # end case
        if start == end:
            return nums[start]

        pivot = nums[(start + end) // 2]
        left, right = start, end

        while left <= right:
            # decending order, so nums[left] > pivot not < pivot
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self.quickSelect(nums, start, right, k)
        if start + k - 1 >= left:
            return self.quickSelect(nums, left, end, k - (left - start))
        return nums[right + 1]
