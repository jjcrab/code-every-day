# https: // leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def isValid(s):
    # t = {'(': ')', '{': '}', '[': ']'}
    t = {")": "(", "}": "{", "]": "["}
    if len(s) % 2 != 0:
        return False
    else:
        stack = []
        for p in s:
            if p not in t:
                stack.append(p)
            else:
                if not stack or stack.pop() != t[p]:
                    return False
        return not stack

        # for i in range(0, len(s)-1, 2):
        #     if s[i] not in t:
        #         # print('here', i)
        #         return False

        #     if t[s[i]] != s[i+1]:
        #         mid = len(s)//2
        #         half = s[:mid]
        #         val = ""
        #         for p in half:
        #             if p not in t:
        #                 return False
        #             val += t[p]
        #         if val == s[:mid-1:-1]:
        #             return True
        #         else:
        #             # print('there')
        #             return False
        # return True
print(isValid('()'))
