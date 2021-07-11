# https: // leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

'''
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

 

Example 1:


Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:


Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
'''


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        # max area = max_height * max_width, so need to find the max_height and max_width

        horizontalCuts.sort()
        verticalCuts.sort()

        # deal with edge cuts and pick the bigger one
        max_height = max(horizontalCuts[0], h - horizontalCuts[-1])
        max_width = max(verticalCuts[0], w - verticalCuts[-1])

        # loop the rest to find the max_height and max_width
        for i in range(1, len(horizontalCuts)):
            max_height = max(
                max_height, horizontalCuts[i] - horizontalCuts[i - 1])

        for j in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[j] - verticalCuts[j - 1])

        return (max_height * max_width) % (10 ** 9 + 7)
