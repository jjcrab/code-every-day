# https: // leetcode.com/problems/remove-element/
def removeElement(nums, val):
    # length = len(nums)
    # for i in range(len(nums)):
    #     if nums[i] == val:
    #         length -= 1
    # return length

    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


print(removeElement([3, 2, 2, 3], 3))
