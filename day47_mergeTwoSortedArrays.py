# https: // www.lintcode.com/problem/6/
'''
Merge two given sorted ascending integer array A and B into a new sorted integer array.

Example
Example 1:

Input:

A = [1]
B = [1]
Output:

[1,1]
Explanation:

return array merged.

Example 2:

Input:

A = [1,2,3,4]
B = [2,4,5,6]
Output:

[1,2,2,3,4,4,5,6]
Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
'''


class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):

        # array = A + B
        # return sorted(array)

        # two pointers
        # if not A and not B:
        #     return []
        # if not A:
        #     return B
        # if not B:
        #     return A
        result = []
        a, b = 0, 0
        lA, lB = len(A), len(B)
        while a < lA and b < lB:
            if A[a] <= B[b]:
                result.append(A[a])
                a += 1
            else:
                result.append(B[b])
                b += 1
        # if a == lA:
        #     result += B[b:]
        # if b == lB:
        #     result += A[a:]
        while a < lA:
            result.append(A[a])
            a += 1
        while b < lB:
            result.append(B[b])
            b += 1
        return result
