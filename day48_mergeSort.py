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
        temp = [0 for _ in range(len(A))]
        self.merge_helper(0, len(A) - 1, A, temp)

    def merge_helper(self, start, end, A, temp):
        # end case
        if start >= end:
            return

        mid = (start + end)//2
        self.merge_helper(start, mid, A, temp)
        self.merge_helper(mid + 1, end, A, temp)
        self.merge(start, mid, end, A, temp)

    def merge(self, start, mid, end, A, temp):
        # merge two sides, left side start from start, right side start from mid + 1
        left, right = start, mid + 1
        # record the index of element
        index = start
        # compare left side each element to right side each element (both are from thier most left position since already sorted)

        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right]
                right += 1
            index += 1
        # after comparing, if left side still have elements not put in temp list, put them into temp list
        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1
        # after comparing, if right side still have elements not put in temp list, put them into temp list
        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1

        # copy temp list to original list
        for index in range(start, end + 1):
            A[index] = temp[index]
