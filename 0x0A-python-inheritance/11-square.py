#!/usr/bin/python3
'''Module: for Square class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass repr a rectangle.'''
    def __init__(self, size):
        '''Constructor of objects.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method calculates area of square.'''
        return (self.__size * self.__size)

    def __str__(self):
        '''Returns string repres of this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
