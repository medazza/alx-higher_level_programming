#!/usr/bin/python3
"""Module that contains the Square Class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor or initialisation of instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Method should return [Square] (<id>) <x>/<y> - <size> """
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Getter of Size of this square obj."""
        return (self.width)

    @size.setter
    def size(self, value):
        """ Setter of Size of this square obj."""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """ Method private that assigns attributes """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes via no-keyword & keyword args."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Func that returns the dictionary representation of a Square """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
