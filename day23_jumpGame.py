# https: // leetcode.com/problems/jump-game/solution/

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# The array A contains š integers š1, š2, ā¦, šš(1ā¤ššā¤5000)(1ā¤nā¤5000)

def canJump(A):
    # max_step_index = 0
    # for i, v in enumerate(A):

    #     if i <= max_step_index:
    #         max_step_index = max(max_step_index, i+v)
    #         if max_step_index >= len(A) - 1:
    #             return True
    #     else:
    #         return False

    last_position = len(A) - 1
    for i in range(len(A)-2, -1, -1):
        if i + A[i] >= last_position:
            last_position = i

    return last_position == 0


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))

# Time: O(N)
# Space: O(1)
