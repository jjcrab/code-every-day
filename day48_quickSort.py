# Sort Integers II
'''
Description
Given an integer array, sort it in ascending order in place. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

Example
Example1:

Input: [3, 2, 1, 4, 5], 
Output: [1, 2, 3, 4, 5].
Example2:

Input: [2, 3, 1], 
Output: [1, 2, 3].
'''


class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        # quick sort
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        # end case
        if start >= end:
            return

        # pick pivot
        # key point 1: pivot is a value not index
        pivot = A[(start + end) // 2]
        left, right = start, end

        # key point 2: left <= right not left < right, because left and right \
        # can't be the same, if the same both need to move 1 more step
        while left <= right:
            # key point 3: A[left] < pivot not <= pivot, similar to A[right]
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

            # while A[left] < pivot:
            #     left += 1
            # while A[right] > pivot:
            #     right -= 1
            # if left <= right:
            #     A[left], A[right] = A[right], A[left]
            #     left += 1
            #     right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
