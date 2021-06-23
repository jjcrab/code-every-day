'''
You are given a string num, representing a large integer. Return the largest-valued odd integer(as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
'''
'''
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Afshin Yazdani to Everyone (11:08 PM)
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
'''




import collections
def find_largest(num):

    if int(num) % 2 != 0:
        return num

    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i + 1]

    return ""


print(find_largest("4240003"))


'''
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
'''


def find_shortest(matrix):
    queue = collections.deque([((0, 0), 0)])
    matrix[0][0] = 'D'
    while queue:
        (x, y), c = queue.popleft()

        for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            if 0 <= x+dx < len(matrix) and 0 <= y+dy < len(matrix[0]):
                if matrix[x+dx][y+dy] == 'X':
                    return c+1
                elif matrix[x+dx][y+dy] == 'O':
                    matrix[x+dx][y+dy] = 'D'
                    queue.append(((x+dx, y+dy), c+1))
    return -1


inp = [['O', 'O', 'O', 'O'],
       ['D', 'O', 'D', 'O'],
       ['O', 'O', 'X', 'O'],
       ['O', 'D', 'D', 'O']]
print(find_shortest(inp))
