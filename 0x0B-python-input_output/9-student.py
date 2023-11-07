#!/usr/bin/python3
"""Module define the clas "Student" """


class Student:
    """ Student Class"""
    def __init__(self, first_name, last_name, age):
        """Constructor of student obj"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary repr of a Student obj"""
        return self.__dict__
