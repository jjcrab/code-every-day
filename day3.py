# Shortest Word

def shortest_word(s):
    word = s.split(' ')
    slenw = min(word, key=len)
    return len(slenw)


# print(shortest_word("I don't think that word means what you think it means"))
# should return: 1


# # Sum of Minimums

def sum_of_minimums(list):
    sum = 0
    for li in list:
        small_num = min(li)
        sum = sum+small_num
    return sum


my_list = [
    [1, 2, 3, 4, 5],  # minimum value of row is 1
    [5, 6, 7, 8, 9],  # minimum value of row is 5
    [20, 21, 34, 56, 100]  # minimum value of row is 20
]

# print(sum_of_minimums(my_list))
#     # should return 26

# # Split Strings


def split_strings(s):
    split = []
    if len(s) % 2 != 0:
        s = s+'_'

    for i in range(0, len(s), 2):
        split.append(f"{s[i]}{s[i+1]}")
    return split


print(split_strings('abc'))
# should return ['ab', 'c_']

print(split_strings('abcdef'))
# # should return ['ab', 'cd', 'ef']
