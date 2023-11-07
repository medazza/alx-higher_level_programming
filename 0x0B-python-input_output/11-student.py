#!/usr/bin/python3
"""Module define the clas "Student" """


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Constructor the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary repres of a Student obj
        with specified attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = dict()
        for attr in attrs:
            try:
                new_dict[attr] = self.__dict__[attr]
            except:
                pass
        return new_dict

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
