# https://www.codewars.com/kata/59859f435f5d18ede7000050/solutions/python
def word_to_bin(word):
    # arr = []
    # for letter in word:
    #     arr.append(f'{int(bin(ord(letter))[2:]):08}')
    # return arr
    return [f"{ord(c):08b}" for c in word]
