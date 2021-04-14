# https://www.codewars.com/kata/54ba84be607a92aa900000f1
def is_isogram(string):
    return len(set(string.lower())) == len(string)


# https://www.codewars.com/kata/57f609022f4d534f05000024/train/javascript
# def stray(arr):
#     for i in range(len(arr)):
#         if arr[i] == arr[i+1]:
#             s = arr[i]
#             break
#     arrs = set(arr)
#     arrs.remove(s)
#     return list(arrs)[0]
    # arrs = list(set(arr))
    # if arrs[0] == s:
    #     return arrs[1]
    # else:
    #     return arrs[0]


# def stray(arr):
#     return min(arr, key=arr.count)


def stray(arr):
    for i in set(arr):
        if arr.count(i) == 1:
            return i
