# https: // leetcode.com/problems/fizz-buzz/
# Given an integer n, return a string array answer(1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.

def fizzBuzz(n):
    result = []
    # temp = ""
    # for i in range(1, n+1):
    #     if i % 15 == 0:
    #         temp = "FizzBuzz"
    #     elif i % 3 == 0:
    #         temp = "Fizz"
    #     elif i % 5 == 0:
    #         temp = "Buzz"
    #     else:
    #         temp = str(i)
    #     result.append(temp)
    # return result
    fizzbuzzhash = {3: "Fizz", 5: "Buzz"}
    for i in range(1, n+1):
        temp = ""
        for key in fizzbuzzhash:
            if i % key == 0:
                temp += fizzbuzzhash[key]
        if not temp:
            temp = str(i)
        result.append(temp)
    return result


print(fizzBuzz(3))
