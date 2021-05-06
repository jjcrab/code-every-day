# https: // leetcode.com/problems/reverse-integer/

def reverse(x):
    if x > 0:
        strlist = list(str(x))
        if strlist[len(strlist)-1] == 0:
            strlist.pop()
        strlist.reverse()
        result = int("".join(strlist))
        if result >= 2**31:
            return 0
        else:
            return result
    elif x == 0:
        return 0
    else:
        strlist = list(str(-x))
        if strlist[len(strlist)-1] == 0:
            strlist.pop()
        strlist.reverse()
        result = -int("".join(strlist))
        if result <= -2**31:
            return 0
        else:
            return result


print(reverse(-1230))
