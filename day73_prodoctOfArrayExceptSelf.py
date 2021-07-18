'''
Description
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

Example
Example1

Input: [1,2,3,4]
Output: [24,12,8,6]
Explanation:
2*3*4=24
1*3*4=12
1*2*4=8
1*2*3=6
Example2

Input: [2,3,8]
Output: [24,16,6]
Explanation:
3*8=24
2*8=16
2*3=6
Challenge
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

'''


class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """

    def productExceptSelf(self, nums):
        # each element in result is current index's prefix * postfix
        # can think the prefix is add 1 from front, postfix is adding 1 from the back

        prefix = 1
        postfix = 1
        result = [1] * len(nums)

        # from left to right, prefix is product of all previous elements
        for i in range(len(nums)):
            # result[i] == 1
            result[i] = prefix
            prefix *= nums[i]

        print(result)

        # from right to left, postfix is product of all behind elements
        for i in range(len(nums) - 1, -1, -1):
            # result[i] != 1
            result[i] *= postfix
            postfix *= nums[i]

        return result
