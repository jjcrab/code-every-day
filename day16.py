# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/
# Given a sequence of integers, return the sum of all the integers that have an even index, multiplied by the integer at the last index.
# Indices in sequence start from 0.
# If the sequence is empty, you should return 0.

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
