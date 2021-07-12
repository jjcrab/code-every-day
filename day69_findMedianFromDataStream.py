'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
'''


import heapq


class MedianFinder:

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.nums = []

    # def addNum(self, num: int) -> None:
    #     self.nums.append(num)

    # def findMedian(self) -> float:
    #     if not self.nums:
    #         return []
    #     self.nums.sort()
    #     median_index = len(self.nums) // 2
    #     if len(self.nums) % 2 == 0:
    #         return (self.nums[median_index] + self.nums[median_index - 1]) / 2
    #     return self.nums[median_index]

    # optimize solution with two heaps


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # max heap for smaller numbers
        self.max_heap = []
        # min heap for larger numbers
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # balance the length of two heaps, min_heap(larger number) take the extra one if not even
        # before insert the num to one of the heap, need to add it to the other heap first and add the pop value to the final heap
        # length of max_heap can only either one element less than min_heap or equal

        if len(self.max_heap) < len(self.min_heap):
            # need to add one element to max_heap, find the right element to add (not simply num)
            heapq.heappush(self.max_heap, -
                           heapq.heappushpop(self.min_heap, num))
        else:
            # if equal then put it to min_heap, but first compare in max_heap
            heapq.heappush(self.min_heap, -
                           heapq.heappushpop(self.max_heap, -num))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return float(self.min_heap[0])
