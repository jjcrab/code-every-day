# https: // leetcode.com/problems/integer-to-english-words/

'''
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''


class Solution:
    #     def numberToWords(self, num: int) -> str:
    #         billion = num // 1000000000
    #         million = (num - billion * 1000000000) // 1000000
    #         thousand = (num - billion * 1000000000 - million * 1000000) // 1000
    #         rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

    #         if not num:
    #             return "Zero"
    #         result = ''
    #         if billion:
    #             result = self.three(billion) + ' Billion'
    #         if million:
    #             result += ' ' if result else ''
    #             result += self.three(million) + ' Million'
    #         if thousand:
    #             result += ' ' if result else ''
    #             result += self.three(thousand) + ' Thousand'
    #         if rest:
    #             result += ' ' if result else ''
    #             result += self.three(rest)
    #         return result

    #     def one(self, num):
    #         switcher = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    #         return switcher.get(num)

    #     def two_less_20(self, num):
    #         switcher = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    #         return switcher.get(num)

    #     def ten(self, num):
    #         switcher = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
    #         return switcher.get(num)

    #     def two(self, num):
    #         if not num:
    #             return ''
    #         elif num < 10:
    #             return self.one(num)
    #         elif num < 20:
    #             return self.two_less_20(num)
    #         else:
    #             tenner = num // 10
    #             rest = num - tenner * 10
    #             return self.ten(tenner) + ' ' + self.one(rest) if rest else self.ten(tenner)

    #     def three(self, num):
    #         hundred = num // 100
    #         rest = num - hundred * 100
    #         if hundred and rest:
    #             return self.one(hundred) + ' Hundred ' + self.two(rest)
    #         elif not hundred and rest:
    #             return self.two(rest)
    #         elif hundred and not rest:
    #             return self.one(hundred) + ' Hundred'

    def numberToWords(self, num: int) -> str:
        ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]

        def helper(num):
            if not num:
                return []
            if num < 20:
                return [ones[num-1]]
            elif num < 100:
                return [tens[(num//10)-2]] + helper(num % 10)
            elif num < 1000:
                return helper((num//100)) + ["Hundred"] + helper(num % 100)
            elif num < 10**6:
                return helper((num//1000)) + ["Thousand"] + helper(num % 1000)
            elif num < 10**9:
                return helper((num//10**6)) + ["Million"] + helper(num % 10**6)
            else:
                return helper((num//10**9)) + ["Billion"] + helper(num % 10**9)

        if num == 0:
            return "Zero"
        return ' '.join(helper(num))
