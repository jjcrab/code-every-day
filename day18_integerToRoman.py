# https: // leetcode.com/problems/integer-to-roman/

def intToRoman(num):
    # dic = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    # if num in dic:
    #     return dic(num)
    # else:
    digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
              (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
              (5, "V"), (4, "IV"), (1, "I")]
    # romanlist = []
    # for v, letter in digits:
    #     if num == 0:
    #         break
    #     quo, num = divmod(num, v)
    #     romanlist.append(letter*quo)

    # return "".join(romanlist)

    romanletter = ""
    for v, letter in digits:
        romanletter = romanletter + (num//v)*letter
        num = num % v
    return romanletter


print(intToRoman(1994))
