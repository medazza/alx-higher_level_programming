#!/usr/bin/python3
'''Module contains the Square class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class that subclass repre a rectangle.'''
    def __init__(self, size):
        '''Constructor of objects.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method calculate the area of square.'''
        return self.__size ** 2
