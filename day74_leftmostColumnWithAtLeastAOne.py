'''
(This problem is an interactive problem.)

A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

 

Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
'''


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # binary search for each row
        #         rows, cols = binaryMatrix.dimensions()
        #         min_left = cols
        #         for row in range(rows):
        #             start, end = 0, cols - 1
        #             while start + 1 < end:
        #                 mid = (start + end) // 2
        #                 if binaryMatrix.get(row, mid) == 0:
        #                     start = mid
        #                 else:
        #                     end = mid

        #             if binaryMatrix.get(row, start) == 1:
        #                 min_left = min(min_left, start)
        #             elif binaryMatrix.get(row, end) == 1:
        #                 min_left = min(min_left, end)

        #         return -1 if min_left == cols else min_left

        # start at top right, move only left or down
        rows, cols = binaryMatrix.dimensions()
        row, col = 0, cols - 1
        current = top_right = binaryMatrix.get(0, cols - 1)

        while 0 <= row < rows and 0 <= col < cols:
            if binaryMatrix.get(row, col) == 1:
                # move left
                col -= 1
            else:
                # move down
                row += 1

        return -1 if col == cols - 1 else col + 1
