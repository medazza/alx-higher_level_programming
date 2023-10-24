#!/usr/bin/python3
""" singly-linked list Module."""


class Node:
    """Represent class singly-linked list."""

    def __init__(self, data, next_node=None):
        """Construct a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): Next node of the Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter the data of the Node obj."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Setter the data of the Node obj."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Setter the next_node of the Node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly-linked list class."""

    def __init__(self):
        """Construct a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """that inserts a new Node into the correct
        sorted position in the list (increasing order)
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Define the print() repre of a SinglyLinkedList."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
