# https: // leetcode.com/problems/trapping-rain-water/
'''
Description
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Trapping Rain Water

Example
Example 1:

Input: [0,1,0]
Output: 0
Example 2:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Challenge
O(n) time and O(1) memory

O(n) time and O(n) memory is also acceptable.
'''


class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        # # calculate each position water

        # # edge case:
        # if not heights:
        #     return 0

        # # left to right, find max_left of each index
        # max_left = []
        # temp = 0
        # for i in heights:
        #     temp = max(temp, i)
        #     max_left.append(temp)

        # # right to left, find max_right of each index
        # max_right = []
        # temp = 0
        # for i in reversed(heights):
        #     temp = max(temp, i)
        #     max_right.append(temp)
        # max_right.reverse()

        # # add up each position's water: min(max_left, max_right) - itself
        # water = 0
        # for i in range(len(heights)):
        #     water += min(max_left[i], max_right[i]) - heights[i]

        # return water

        # use two pointers
        # edge case:
        if not heights:
            return 0

        water = 0

        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]

        #  has to be  <=, because the prvious one of opposite diection/the next of the same direction hasn't calculate yet
        while left <= right:
            # left_max < right_max
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                water += left_max - heights[left]
                left += 1
        # left_max >= right_max
            else:
                right_max = max(right_max, heights[right])
                water += right_max - heights[right]
                right -= 1
        return water
