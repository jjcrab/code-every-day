# https: // www.lintcode.com/problem/936 /?_from = ladder & fromId = 184

def capitalizesFirst(s):
    # s_list = list(s)
    # print(s)
    # print(s_list)
    # if s_list[0] and s_list[0].isalpha():
    #     s_list[0] = s_list[0].capitalize()
    # for i in range(1, len(s_list)):
    #     if s_list[i-1].isspace():
    #         s_list[i] = s_list[i].capitalize()
    # return "".join(s_list)

    s_change = ""
    for i in range(len(s)):
        if i == 0 and s[i].isalpha() or s[i-1].isspace():
            s_change += s[i].capitalize()
        else:
            s_change += s[i]
    return s_change


print(capitalizesFirst(" i love you "))
