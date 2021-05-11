# https: // leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    max_sum = nums[0]
    max_final = nums[0]
    for n in nums[1:]:
        max_sum = max(n, max_sum+n)
        max_final = max(max_sum, max_final)
    return max_final


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
