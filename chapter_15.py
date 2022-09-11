# 15.1 PROGRAMMED-DEFINED TYPES:

# A programmer-defined type is also called a class.
# This creates a class called Point:
class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y

    def __str__(self):

        return "(%g, %g)" % (self.x, self.y)

    def __radd__(self, other):

        return self.__add__(other)

    def __add__(self, other):

        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def add_point(self, other):

        return Point(self.x + other.x, self.y + other.y)

    def add_tuple(self, other):

        return Point(self.x + other[0], self.y + other[1])

# # Defining the class Point above creates a class object; to create a Point, call
# #   Point as if it were a function:
# blank = Point()
# print(type(blank))
#
# # Creating a new object as above is called instantiation, as the object being is an
# #   instance of the class.


# 15.2 ATTRIBUTES:

# # Assign values to an instance via dot notation:
# blank.x = 3.0
# blank.y = 4.0
# # Above we are assigning values to named elements of an object, these elements
# #   being called attributes.
#
# x = blank.x
# # The expression blank.x means, “Go to the object blank refers to and get the value
# #   of x.” In the example, we assign that value to a variable named x. There is no
# #   conflict between the variable x and the attribute x above.

def print_point(p):
    """Takes a Point object and prints the Object in string
    format.

    p: Point object with attributes x and y
    """

    print('(%g, %g)' % (p.x, p.y))


def makepoint(x, y):
    """Returns a Point object with attributes x and y.

    x: num
    y: num
    """

    point = Point()

    point.x = x
    point.y = y

    return point

point1 = makepoint(3, 4)
point2 = makepoint(2, 5)

import math

def distance_between_points(p1, p2):
    """Takes two Points as arguments and returns the distance between
    them in the same units in which they are given.

    p1: Point
    p2: Point
    """

    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)


# 15.5 OBJECTS ARE MUTABLE:

class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 1.0
box.corner.y = 2.0

def move_rectangle(rect, dx, dy):
    """Takes a Rectangle object and changes its location by dx in the positive x
    direction and dy in the negative y direction.

    rect: Rectangle
    dx: num
    dy: num
    """

    rect.corner.x += dx
    rect.corner.y += dy


# 15.6 COPYING:

p1 = Point()
p1.x = 123.0
p1.y = 213.0

# The copy module contains a function called copy that can duplicate any object,
#   oft used to prevent aliasing. p1 is p2 should return False.
import copy
p2 = copy.copy(p1)
# print(p1 is p2)

# The statement p1 == p2 returns False because for instances, the default behaviour
#   of the == operator is the same as that of the is operator - it checks
#   object identity rather than object equivalence in the case of instances. This
#   is because for programmer-defined types, Python doesn't know what should be
#   considered equivalent... yet.
# print(p1 == p2)

# Attempting to use copy.copy to duplicate a Rectangle copies the Rectangle object
#   but not the embedded Point object, which instead becomes aliased - the result
#   thus becomes called a shallow copy.

# To solve the above, the copy module provides a method named deepcopy, to perform
#   what is called a deep copy.

def move_rectangle2(rect, dx, dy):
    """Takes a Rectangle object, copies it and changes the copy's location
    by dx in the positive x direction and dy in the negative y direction.

    rect: Rectangle
    dx: num
    dy: num
    """

    rect2 = copy.deepcopy(rect)

    rect2.corner.x += dx
    rect2.corner.y += dy

    return rect2


# 15.7 DEBUGGING:

# You can use isinstance() to check whether an object (passed as the first argument)
#   is an instance of a class (passed as the second argument).

# If you are not sure whether an object (argument1) has a particular attribute (argument 2,
#   the attribute name in string format), you can use the built-in function hasattr:
# print(hasattr(p2, "x"))
# print(hasattr(p2, "z"))

# Alternatively tot he above, a try statement can be used to see if an object has
#   the necessary attributes.

if __name__ == "__main__":

    p1 = Point(1, 3)
    p2 = Point(25, 33)
    print(p2 + p1)
    print(p2 + (0, 2))