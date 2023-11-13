#!/usr/bin/python3
""" Module contains the  Rectangle Class."""
from models.base import Base


class Rectangle(Base):
    """ The Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor or Initialisation of instances."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter the Width of this rectangle obj."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the Width of this rectangle obj."""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter the Height of this rectangle obj."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the Height of this rectangle obj."""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter x of this rectangle obj."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x of this rectangle obj."""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter y of this rectangle obj."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y of this rectangle obj."""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """ Validation of all setter methods and instantiation """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Func returns the area value of the Rectangle instance. """
        return (self.width * self.height)

    def display(self):
        """ prints in stdout the Rectangle instance with the character #
            and handle x and y. """
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end="")

    def __str__(self):
        """Func that returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """ Private method that updates instance attributes via */**args."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Func that returns the dictionary representation of a Rectangle """
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
