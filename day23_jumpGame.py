# https: // www.lintcode.com/problem/116 /?_from = ladder & fromId = 184
# https: // leetcode.com/problems/jump-game/solution/

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# The array A contains 𝑛 integers 𝑎1, 𝑎2, …, 𝑎𝑛(1≤𝑎𝑖≤5000)(1≤n≤5000)

def canJump(A):
    max_step_index = 0
    for i, v in enumerate(A):

        if i <= max_step_index:
            max_step_index = max(max_step_index, i+v)
            if max_step_index >= len(A) - 1:
                return True
        else:
            return False


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))

Time: O(N)
Space: O(1)
