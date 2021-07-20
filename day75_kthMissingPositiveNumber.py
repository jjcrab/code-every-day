'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
'''


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # the number of integers are missing before arr[i] equal to arr[i] - i - 1
        # use binary search to find the first arr[i] (number of integers are missing before arr[i]) > k

        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            # If number of positive integers which are missing before arr[mid] is less than k -->
            # continue to search on the right.
            if arr[mid] - mid - 1 < k:
                start = mid + 1
            # Otherwise, go left.
            else:
                end = mid - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return start + k
