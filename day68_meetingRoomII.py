# https://leetcode.com/problems/meeting-rooms-ii/submissions/
'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
'''


# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         if not intervals or not intervals[0]:
#             return 0
#         intervals.sort(key=lambda x: x[0])
#         room_intervals = []

#         for i in intervals:
#             # no overlap, no need to have another room, same room extend time
#             if not room_intervals:
#                 room_intervals.append(i)
#             # here is "<=" not "<", should confirm with interviewer
#             elif room_intervals[-1][1] <= i[0]:
#                 room_intervals[-1][1] = i[1]

#             # overlap, need to check if len(room_intervals) > 1, might not overlap other rooms
#             else:
#                 # can't initiate the flag outside of the outer for loop, because need to refresh for each i
#                 flag = False
#                 if len(room_intervals) > 1:
#                     for j in range(len(room_intervals) - 1):
#                         # here is "<=" not "<", should confirm with interviewer
#                         if room_intervals[j][1] <= i[0]:
#                             room_intervals[j][1] = i[1]
#                             flag = True
#                             break
#                 if not flag:
#                     room_intervals.append(i)

#         return len(room_intervals)


# sweep line method
# class Solution:
#     """
#     @param intervals: an array of meeting time intervals
#     @return: the minimum number of conference rooms required
#     """

#     def minMeetingRooms(self, intervals):
#         # scanning/ sweep line
#         result = 0
#         if not intervals:
#             return result

#         time = []
#         count = 0

#         for i in intervals:
#             time.append((i.start, 1))
#             time.append((i.end, -1))

#         for i in sorted(time):
#             count += i[1]
#             result = max(result, count)

#         return result


# heap method
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        heap = []
        intervals.sort(key=lambda x: x[0])

        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i][0]:
                heapq.heappop(heap)

            heapq.heappush(heap, intervals[i][1])

        return len(heap)
