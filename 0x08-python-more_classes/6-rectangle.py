#!/usr/bin/python3


"""For creating and manipulating Rectangle objects"""

class Rectangle:

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width value, positive integers only"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height value, positive integers only"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of the Rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return self.height * 2 + self.__width * 2

    def __str__(self):
        """Will print a graphical representation of the Rectangle"""

        s = ""
        if self.__height == 0 or self.__width == 0:
            return s
        for x in range(self.__height):
            s += self.__width * "#" + "\n"
        return s[:-1]

    def __repr__(self):
        """String representation of the Rectangle object"""

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
