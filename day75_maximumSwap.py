'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        # 2736[2,7,3,6]
        n = [int(x) for x in str(num)]
        # {2: 0, 7: 1, 3: 2, 6: 3}
        dic = {v: k for k, v in enumerate(n)}
        for i, n1 in enumerate(n):
            for x in range(9, n1, -1):
                # from 9 to find the max in dic
                if dic.get(x, -1) > i:
                    n[i], n[dic[x]] = n[dic[x]], n[i]
                    return int(''.join(map(str, n)))
        return num
