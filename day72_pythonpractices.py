# print("hello " + "world")
# print("hello " "world")
# print("hello ""world")
# print("hello, world", end=" ")
# print(bool(None))

li = [1, 2, 4, 3]
# li.remove(2)
del li[1:3]
# print(li)
if 2 in li:
    # print(li)
    print(li.index(2))

# print(li.index(1))
# print(li.index(2))


# print("yay!" if 0 > 1 else "nay!")


filled_dict = {"one": 1, "two": 2, "three": 3}
# print(filled_dict.get("four"))
# print(filled_dict["four"])
# our_iterable = filled_dict.keys()
l = list(filled_dict.keys())
l = filled_dict.keys()
# print(our_iterable)
print(l)


name = "Reiko"
# print(f"She said her name is {name}.")


# for animal in ["dog", "cat", "mouse"]:
# You can use format() to interpolate formatted strings
# print("{} is a mammal".format(animal))
# print(f"{animal} is a mammal.")
