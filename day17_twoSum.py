# https: // leetcode.com/problems/two-sum/solution/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            exp = target - v
            if exp in d:
                return [d[exp], i]
            d[v] = i

#         nums_sorted = sorted(nums)
#         if nums_sorted[0] == 0:
#             return [0,nums.index(target,1)]
#         else:
#             for i in range(len(nums)):
#                 for j in range(i+1,len(nums)):
#                     if sum([nums_sorted[i],nums_sorted[j]]) == target:
#                         if nums_sorted[i] == nums_sorted[j]:
#                             index_first = nums.index(nums_sorted[i])
#                             index_second = nums.index(nums_sorted[j],index_first+1)
#                             return [index_first,index_second]
#                         else:
#                             return [nums.index(nums_sorted[i]),nums.index(nums_sorted[j])]


n = Solution([3, 4, 3], 6)
print(n.twoSum())
