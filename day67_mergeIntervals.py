https: // leetcode.com/problems/merge-intervals/submissions/

'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        print(intervals)

        x, y = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            if x == intervals[i][0] and y == intervals[i][1]:
                continue
            # include
            if y >= intervals[i][1]:
                continue
            # overlap
            if intervals[i][0] <= y < intervals[i][1]:
                y = intervals[i][1]

            # no overlap
            else:
                result.append((x, y))
                x, y = intervals[i][0], intervals[i][1]

        result.append((x, y))
        return result


# a better way to do it
# combining the situations above
# only think two situation: over lap and no over lap
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            # no overlap (and no result, put the element into result first and then modify
            if not result or result[-1][1] < i[0]:
                result.append(i)
            # overlap
            else:
                result[-1][1] = max(result[-1][1], i[1])
        return result
