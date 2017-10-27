#!/usr/bin/python3

"""Create a Node object for use in a singly linked list. """


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

    def __str__(self):
        return str(self.__data)


"""Use Node objects to build a singly linked list. """


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        head = self.__head
        if not head:
            self.__head = Node(value)
            return
        if head.data > value:
            self.__head = Node(value, head)
            return
        while head.next_node:
            if head.next_node.data >= value:
                head.next_node = Node(value, head.next_node)
                return
            head = head.next_node
        head.next_node = Node(value)

    def __str__(self):
        nodes = []
        head = self.__head
        while head:
            nodes.append(str(head))
            head = head.next_node
        return '\n'.join(nodes)
