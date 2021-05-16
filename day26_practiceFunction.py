# glb_name = "jingjing"
# def change_name():
#     global glb_name
#     glb_name = "jingjing li"
# change_name()
# print(glb_name)


# def sum(equation):
#     x, add, num1, equal, num2 = equation.split()
#     num1, num2 = int(num1), int(num2)
#     x = num2-num1
#     return f'X = {x}'


# print(sum('x + 4 = 9'))


# def mult_divide(num1, num2):
#     return (num1 * num2), (num1/num2)


# mul, divide = mult_divide(5, 4)
# print(mul, divide)


# def is_prime(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True

# def get_primes(max_num):
#     primes = []
#     for i in range(1, max_num):
#         if is_prime(i):
#             primes.append(i)
#     return primes

# max_num_prime = int(input('Enter the max number: '))
# print(get_primes(max_num_prime))
# print(max(get_primes(max_num_prime)))


# def sumAll(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum


# print(sumAll(3, 4, 6))


import math


def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("please enter rectangle or circle")


def rectangle_area():
    length = float(input("enter the length:"))
    width = float(input("enter the width:"))
    area = length * width
    print(area)


def circle_area():
    radius = float(input("enter the radius:"))
    area = math.pi * (math.pow(radius, 2))
    print('{:.2f}'.format(area))
    print(f'{area:.2f}')


def main():
    shape_type = input("get area for what shape: ")
    get_area(shape_type)


main()
