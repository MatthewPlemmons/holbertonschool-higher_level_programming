#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be an number')
        if value < 0:
            raise ValueError('size must be >= 0')
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
