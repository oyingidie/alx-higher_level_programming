#!/usr/bin/python3
"""a class with private instance attributes, public class
attributes, public instance methods, and
static method; print...
"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialises a new Rectangle
        Args:
            width (int): the width of the new rectangle
            height (int): the height of the new rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """return width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2*(self.__width + self.__height))

    def __str__(self):
        """return the printable representation (#) of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return ("".join(rect))

    def __repr__(self):
        """return a string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """print a message for every deletion of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the rectangle with the greater area
        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle
        Raises:
            TypeError: if neither of rect_1 or rect_2 is a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
