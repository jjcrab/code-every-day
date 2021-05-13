while True:
    try:
        secret_num = int(input("Enter a secret number "))
        if secret_num == 7:
            break
        if secret_num != 7:
            print("not the right number")
    except ValueError:
        print("unknow error")

print("you got it")


# secret = 7

# while True:
#     guess = int(input("Enter a secret number "))

#     if guess == secret:
#         print("you got it")
#         break
#     else:
#         print("not the right number")


# while True:
#     try:
#         numbers = int(input("Enter a number "))
#         break
#     except ValueError:
#         print("not a number")
#     except:
#         print("unknow")
# print("thanks")
