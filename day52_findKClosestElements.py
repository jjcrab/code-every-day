# https://leetcode.com/problems/find-k-closest-elements/submissions/
'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the bound of '<= target' first position (find the insert position of target)
        # face to face two pointers
        if k == 0:
            return []
        target_position = None
        result = []
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] < x:
                start = mid
            elif arr[mid] == x:
                end = mid
            else:
                end = mid
        if arr[start] == x:
            target_position = start
        elif arr[end] == x:
            target_position = end
        else:
            if abs(x - arr[start]) <= abs(x - arr[end]):
                target_position = start
            else:
                target_position = end

        result.append(arr[target_position])

        # compare left and right (take k number), back to back two pointers
        left, right = target_position - 1, target_position + 1
        while len(result) < k and left >= 0 and right <= len(arr) - 1:
            if abs(x - arr[left]) > abs(x - arr[right]):
                result.append(arr[right])
                right += 1
            else:
                result.append(arr[left])
                left -= 1
        if left < 0:
            for i in range(k-len(result)):
                result.append(arr[right])
                right += 1

        elif right > len(arr) - 1:
            for j in range(k - len(result)):
                result.append(arr[left])
                left -= 1

        return sorted(result)
