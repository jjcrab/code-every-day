'''
Description
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
Example
Example 1:

Input: "-4(2(3)(1))(6(5))"
Output: {-4,2,6,3,1,5}
Explanation:
The output is look like this:
      -4
     /  \
    2    6
   / \   / 
  3   1 5   
Example 2:

Input: "1(-1)"
Output: {1,-1}
Explanation:
The output is look like this:
     1
    /
  -1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        # stack and two pointers (same directions), O(N) and O(N)
        if s == '':
            return None

        i = 0
        while i < len(s) and (s[i].isdigit() or s[i] == '-'):
            i += 1

        root = TreeNode(s[:i])
        stack = [root]

        j = i
        while i < len(s):
            if s[i] == '(':
                j = i + 1
                while s[j].isdigit() or s[j] == '-':
                    j += 1
                node = TreeNode(int(s[i+1:j]))
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
                stack.append(node)

            elif s[i] == ')':
                stack.pop()
                j += 1
            i = j
        return root
