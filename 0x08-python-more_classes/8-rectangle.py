#!/usr/bin/python3
'''Define a class Rectangle wit width and height'''


class Rectangle:
    '''Represents a rectangle.
        Attributes:
            number_of_instances: the number of instance in Rectangle
            print_symbol (any): prints the symbol used for string
            representation'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Returns the width and height of rectangle
        raise:
            TypeError: if width and height is non-integer or < 0'''
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Get the current width of the Rectangle'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Get the current height of the rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Get the area of the rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            self.perimeter = 0
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the rectangle with the greater area
        raise:
            TypeError: if rect_1 0r rect_2 is not a Rectangle'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        '''Returns the representation of the rectangle.
            Represents the rectangle with the "#" character'''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        '''Returns the string representation of the Rectangle'''
        print_rect = "Rectangle(" + str(self.__width)
        print_rect += ", " + str(self.__height) + ")"
        return (print_rect)

    def __del__(self):
        '''Print a message at the deletion of a rectangle'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
