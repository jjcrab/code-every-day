# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/

# def even_last(numbers):
#     result = 0
#     if not numbers:
#         return 0
#     for x, v in enumerate(numbers):
#         if x % 2 == 0:
#             result += v
#     return result*numbers[-1]


def even_last(numbers):
    return sum(numbers[::2]) * numbers[-1] if numbers else 0
