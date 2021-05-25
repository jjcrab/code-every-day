# https: // leetcode.com/problems/fibonacci-number/
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,


# Find the Nth number in Fibonacci sequence.
# A Fibonacci sequence is defined as follow:
# The first two numbers are 0 and 1.
# The i th number is the sum of i-1 th number and i-2 th number.
# The first ten numbers in Fibonacci sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...


def fibonacci(n):
    # result_list = [0, 1]
    # # for i in range(2, n):
    # #     sum = result_list[i-2] + result_list[i-1]
    # #     result_list.append(sum)
    # # print(result_list)
    # # return result_list[n-1]

    # for i in range(2, n+1):
    #     result_list[i % 2] = result_list[0]+result_list[1]
    # return result_list[(n+1) % 2]

    if n <= 2:
        return n-1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(1))
print(fibonacci(4))
