#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def __lt__(self, sq):
        return self.area() < sq.area()

    def __le__(self, sq):
        return self.area() <= sq.area()

    def __eq__(self, sq):
        return self.area() == sq.area()

    def __ne__(self, sq):
        return self.area() != sq.area()

    def __gt__(self, sq):
        return self.area() > sq.area()

    def __ge__(self, sq):
        return self.area() >= sq.area()
