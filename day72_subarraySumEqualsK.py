# https://leetcode.com/problems/subarray-sum-equals-k/


'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''

# can't pass
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
# count = 0
# for i in range(len(nums)):
#     total = 0
#     for j in range(i, len(nums)):
#         total += nums[j]
#         if total == k:
#             count += 1
# return count


# better way to do it -> hashmap
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        cur, res = 0, 0
        for v in nums:
            cur += v
            res += dic.get(cur - k, 0)
            dic[cur] = dic.get(cur, 0) + 1
        return res
