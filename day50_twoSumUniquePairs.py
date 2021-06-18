
# Two Sum - Unique pairs
'''
Description
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Example
Example 1:

Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47
Example 2:

Input: nums = [1,1], target = 2 
Output: 1
Explanation:
1 + 1 = 2
'''


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()

        last_pair = ()
        count = 0
        # result = []
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != last_pair:
                    count += 1
                last_pair = (nums[left], nums[right])
                # result.append([nums[left],nums[right]])
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return count
