# string_input = input('Enter a string please: ')
# string_input = string_input.upper()
# print(string_input)
# print(string_input.lower())
# list_input = string_input.split()
# print(list_input)
# for word in list_input:
#     print(word[0], end="")

# print("\n")
# print("test")

# s = sorted(list_input)
# list_input.sort()
# print(list_input)
# print(s)


# r = list(reversed(list_input))
# reversed(list_input)
# list_input.reverse()
# print(list_input)
# print(r)


# letter_z = "Y"
# num_3 = "3"
# a_space = " "

# print(letter_z.isalnum())
# print(num_3.isalnum())
# print(letter_z.isalpha())


# encrypted and decrypted
# A-Z: 65-90
# a-z: 97-122
# original = input('message: ')
# en = []
# for letter in original:
#     if not letter.isalpha():
#         en.append(letter)
#     else:
#         en.append(str(ord(letter)-23))
# print(en)
# print("".join(en))

# de_list = []
# for num in en:
#     if not num.isdigit():
#         de_list.append(num)
#     else:
#         de_list.append(chr(int(num)+23))
# print(de_list)
# print("".join(de_list))

message = input("Enter your message: ")
key = int(input('how many characters to shift (1-26):'))
encrypted = ""
for letter in message:
    if not letter.isalpha():
        encrypted += letter
    else:
        new_num = ord(letter)+key
        if letter.isupper() and new_num > ord('Z') or letter.islower() and new_num > ord('z'):
            new_num -= 26
        encrypted += chr(new_num)
print(encrypted)
print()
decrypted = ""
for letter in encrypted:
    if not letter.isalpha():
        decrypted += letter
    else:
        ori = ord(letter) - key
        if letter.isupper() and ori < ord("A") or letter.islower() and ori < ord('a'):
            ori += 26
        decrypted += chr(ori)
print(decrypted)
