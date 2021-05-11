tall = eval(input('Enter number of layer: '))
max = tall * 2 - 1


for i in range(1, tall+1):
    print(" "*((max-(i*2-1))//2)+"#"*(i*2 - 1))
print(" "*((max-1)//2) + "#")


my_float = 2.13456
limit_float = round(my_float, 3)
print(limit_float)
print(f'testing {my_float:.3f}')
