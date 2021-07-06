'''
Description
Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

Example
Example 1:
	Input:  [3, 2, 1, 4, 5]
	Output: [1, 2, 3, 4, 5]
	
	Explanation: 
	return the sorted array.

Example 2:
	Input:  [1, 1, 2, 1, 1]
	Output: [1, 1, 1, 1, 2]
	
	Explanation: 
	return the sorted array.
'''


class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers(self, A):
        # use heap sort
        self.heapify(A)
        n = len(A)
        for i in range(len(A) - 1):
            A[0], A[n - i - 1] = A[n - i - 1], A[0]
            self.siftdown(A, 0, n - i - 1)

    def heapify(self, A):
        for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i, len(A))

    def siftdown(self, A, k, n):
        # if left child of k exists, if not exists then end the while loop
        while k * 2 + 1 < n:
            # left child
            son = k * 2 + 1
            if k * 2 + 2 < n and A[son] < A[k * 2 + 2]:
                # pick the bigger child
                son = k * 2 + 2
            if A[son] <= A[k]:
                break

            A[son], A[k] = A[k], A[son]
            k = son
