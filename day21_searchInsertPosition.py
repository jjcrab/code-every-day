# https: // leetcode.com/problems/search-insert-position/
def searchInsert(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        pivot = (left+right)//2
        mid = nums[pivot]
        if target == mid:
            return pivot
        elif target < mid:
            right = pivot - 1
        else:
            left = pivot + 1
    return left


print(searchInsert([1, 3, 5, 6], 2))
