# https: // www.codewars.com/kata/51c89385ee245d7ddf000001/python
def solution(value):
    # return 'Vaule is '+'0' * (5-len(str(value)))+str(value)
    # return f'Value is {value:0>5}'
    return f'Value is {value:05}'


# https: // www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python
# def solution(nums):
#     if nums == 0 or nums == None:
#         return []
#     else:
#         nums.sort()
#         return nums


def solution(nums):
    if not nums:
        return []
    return sorted(nums)
