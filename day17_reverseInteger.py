# https: // leetcode.com/problems/reverse-integer/

def reverse(x):
    # if x > 0:
    #     strlist = list(str(x))
    #     if strlist[len(strlist)-1] == 0:
    #         strlist.pop()
    #     strlist.reverse()
    #     result = int("".join(strlist))
    #     if result >= 2**31:
    #         return 0
    #     else:
    #         return result
    # elif x == 0:
    #     return 0
    # else:
    #     strlist = list(str(-x))
    #     if strlist[len(strlist)-1] == 0:
    #         strlist.pop()
    #     strlist.reverse()
    #     result = -int("".join(strlist))
    #     if result <= -2**31:
    #         return 0
    #     else:
    #         return result

    # if x < -2**31 or x > 2**31-1:
    #     return 0
    # else:
    #     if x == 0:
    #         return 0
    #     elif x > 0:
    #         return int(str(x)[::-1])
    #     else:
    #         return -int(str(-x)[::-1])

    neg = False
    if x < -2**31 or x > 2**31-1:
        return 0
    else:
        if x < 0:
            neg = True
        x = abs(x)
        ans = int(str(x)[::-1])
        if neg:
            return -ans
        else:
            return ans


print(reverse(-230))


# Math
# 145
# while n > 0:
#     rem = 145 % 10 - - -> [5, 4, 1]
#     n = n // 10 - - -> 145//10 = 14

#     n = 14
#     14 % 10 = 4
#     14 // 10 = 1.4 = 1

#     1 % 10 = 1
#     1 // 10 = 0
#     ''.join(list)

#     [5, 4, 1] = 541
#     n = 0
#     for num in list:
#         n = n*10 + num

#         0
#         0*10 + 5 = 5

#         5
#         5*10 + 4 = 54

#         54
#         54*10 + 1 = 541

#         541
