#  Find Peak Element

'''
Description
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] & & A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] & & A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
Example
Example 1:

Input:

A = [1, 2, 1, 3, 4, 5, 7, 6]
Output:

1
Explanation:

Returns the index of any peak element. 6 is also correct.
Example 2:

Input:

A = [1, 2, 3, 4, 1]
Output:

3
Explanation:

return the index of peek.

Challenge
Time complexity O(logN)O(logN)
'''


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # peak = 1
        # while peak < len(A) - 1:
        #     left, right = peak - 1, peak + 1
        #     if A[left] < A[peak] and A[peak] > A[right]:
        #         return peak
        #     else:
        #         peak += 1

        # O(logN) Binary search
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid

        return start if A[start] > A[end] else end


# https://leetcode.com/problems/find-peak-element/solution/
