'''
Given two array, output their dot product

if there is no dot product, return -1.

Example
Example1

Input: A = [1,1,1] and B = [2,2,2]
Output: 6
Explanation:
1*2+1*2+1*2=6
Example2

Input: A = [3,2] and B = [2,3,3]
Output: -1
Explanation:
there is no dot product
'''


class Solution:
    """
    @param A: an array
    @param B: an array
    @return: dot product of two array
    """

    def dotProduct(self, A, B):
        # Write your code here
        if not A and not B:
            return -1
        if len(A) != len(B):
            return -1
        res = 0
        for i in range(len(A)):
            tmp = A[i] * B[i]
            res += tmp
        return res
