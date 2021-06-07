# https: // leetcode.com/problems/zigzag-iterator/

'''
Description
Follow up Zigzag Iterator: What if you are given k 1d vectors? How well can your code be extended to such cases? The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".

Example
Example1

Input: k = 3
vecs = [
    [1,2,3],
    [4,5,6,7],
    [8,9],
]
Output: [1,4,8,2,5,9,3,6,7]
Example2

Input: k = 3
vecs = [
    [1,1,1]
    [2,2,2]
    [3,3,3]
]
Output: [1,2,3,1,2,3,1,2,3]
'''


# class ZigzagIterator2:
#     """
#     @param: vecs: a list of 1d vectors
#     """

#     def __init__(self, vecs):
#         # do intialization if necessary
#         self.vecs = vecs
#         self.row = 0
#         self.col = 0
#         # counter of not empty row
#         self.not_emptyrows = len(vecs)
#         # deal with empty list
#         for i in self.vecs:
#             if len(i) == 0:
#                 self.not_emptyrows -= 1

#     """
#     @return: An integer
#     """

#     def _next(self):
#         # when col doesn't have data, which means the current row is finished, go to next non empty data
#         while len(self.vecs[self.row]) <= self.col:
#             self.row += 1

#             if self.row == len(self.vecs):
#                 self.row = 0
#                 self.col += 1

#         # current value
#         val = self.vecs[self.row][self.col]

#         # update not empty row counter
#         if self.col == len(self.vecs[self.row])-1:
#             self.not_emptyrows -= 1

#         # prepare next value
#          # when out of row range, row is back to 0, col + 1
#         self.row += 1
#         if self.row == len(self.vecs):
#             self.row = 0
#             self.col += 1

#         # return current val
#         return val

#     """
#     @return: True if has next
#     """

#     def hasNext(self):
#         # when not empty row counter is 0 means all the rows are finished
#         return self.not_emptyrows


# Method2: queue
import collections


class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """

    def __init__(self, vecs):

        self.queue = collections.deque()
        for vec in vecs:
            # filer tempty list
            if len(vec) > 0:
                # self.queue.append([iter(vec), len(vec)])
                self.queue.append(vec)

    def _next(self):
        # vec_iter, vec_len = self.queue.popleft()
        # val = next(vec_iter)
        # vec_len -= 1

        # if vec_len > 0:
        #     self.queue.append([vec_iter, vec_len])

        # return val
        v = self.queue.popleft()
        val = v.pop(0)
        if v:
            self.queue.append(v)
        return val

    def hasNext(self):
        return len(self.queue)
