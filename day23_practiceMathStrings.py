# A-Z 65-90
# a-z 97-122

print("A =", ord("A"))
print(type(ord("A")))
print(f'65 = {chr(65)}')


# Enter a string to hide in uppercase: HIDE
# Secret Message: 35647890
# Original Message: HIDE

# hide = input('Enter a string ').upper()
# print(hide)
# secret = ""
# original = ""
# for letter in hide:
#     secret += str(ord(letter))

# print(secret)

# for i in range(0, len(secret)-1, 2):
#     original += chr(int(secret[i]+secret[i+1]))

# print(f'hide message: {original}')


# A-Z 65-90
# a-z 97-122     substract 23 so biggest will be 99
hide = input('Enter a string ')
print(hide)
secret = ""
realunicode = ""
original = ""
for letter in hide:
    secret += str(ord(letter)-23)
    realunicode += str(ord(letter))

print(secret, realunicode)

for i in range(0, len(secret)-1, 2):
    original += chr(int(secret[i]+secret[i+1])+23)

print(f'hide message: {original}')
