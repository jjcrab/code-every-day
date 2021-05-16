'''Description
Implement a Rectangle class which include the following attributes and methods:

Two public attributes width and height.
A constructor which expects two parameters width and height of type int.
A method getArea which would calculate the size of the rectangle and return.
'''


# class Rectangle:

#     '''
#      * Define a constructor which expects two parameters width and height here.
#     '''
#     # write your code here

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def getArea(self):
#         return self.width * self.height

#     '''
#      * Define a public method `getArea` which can calculate the area of the
#      * rectangle and return.
#     '''
#     # write your code here


# r = Rectangle(3, 4)
# print(r.getArea())


'''
Implement a class School, including the following attributes and methods:

A private attribute name of type string.
A setter method setName which expect a parameter name of type string.
A getter method getName which expect no parameter and return the name of the school.
'''


class School:
    '''
     * Declare a setter method `setName` which expect a parameter *name*.
    '''
    # write your code here

    def __init__(self):
        self.__name = ""

    def setName(self, name):
        self.__name = name

    '''
     * Declare a getter method `getName` which expect no parameter and return
     * the name of this school
    '''
    # write your code here

    def getName(self):
        return self.__name


# s = School('ucd')
s = School()
s.setName('abc')
print(s.getName())
