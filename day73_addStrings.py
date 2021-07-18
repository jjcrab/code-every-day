# https: // leetcode.com/problems/add-strings/

'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #         num1_num = self.change_to_interger(num1)
        #         num2_num = self.change_to_interger(num2)
        #         return str(num1_num + num2_num)

        #     def change_to_interger(self, num):
        #         str_num = 0
        #         e = len(num)
        #         for i in range(e):
        #             str_num += int(num[i]) * (10 ** (e - 1 - i))

        #         return str_num

        res = ""
        carry = 0
        i_num1, i_num2 = len(num1) - 1, len(num2) - 1
        while i_num1 >= 0 or i_num2 >= 0:
            x1 = ord(num1[i_num1]) - ord('0') if i_num1 >= 0 else 0
            x2 = ord(num2[i_num2]) - ord('0') if i_num2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            res += str(value)
            carry = (x1 + x2 + carry) // 10
            i_num1 -= 1
            i_num2 -= 1

        # edge case: "1" "9"
        if carry:
            res += str(carry)
        return res[::-1]
