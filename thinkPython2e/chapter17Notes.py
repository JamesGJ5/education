# 17.2 Printing objects

# Subject is an object upon which a method is invoked.

class Time:
    """Represents the time of day."""

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds


time1 = Time()
time1.hour = 1
time1.minute = 2
time1.second = 10

# print(time1.time_to_int())


# 17.5, 17.6, 17.7, 17.8

class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other[0]
            y = self.y + other[1]
        return Point(x, y)

    def __radd__(self, other):
        return self.__add__(other)


point1 = Point(1, 2)
point2 = Point(5, 6)

# print(point1.x, point1.y)
# print(point1)
# print(point1 + (1, 5, 10))
# print((1, 5, 10) + point1)


# 17.8 Type-based dispatch

# A 'type-based dispatch' dispatches a task to different methods depending on the types of the arguments passed.


# 17.9 Polymorphism

# Calling the below won't work because the sum() function initialises a value of 0 for the sum at the start, I believe,
# and adds Point objects to the sum. However, __add__ in Point's class definition is not written to accept a number as
# a non-Point argument; instead, it only accepts arrays as non-point arguments.
# print(sum([point1, point2]))


# 17.10 Debugging

# It's recommended to initialise all an object's attributes in __init__, lest you get objects of the same class but with
# different types of attribute and thereby risk mistakes.
# hasattr checks if an object has a particular attribute.

# Maps attribute names to their values in the object
# print(vars(point1))

# A good function for debugging:

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

# print_attributes(point1)


# 17.11 Interface and implementation

# After you deploy a new class, you might discover a better implementation. If other parts
# of the program are using your class, it might be time-consuming and error-prone to change
# the interface. But if you designed the interface carefully, you can change the implementation without
# changing the interface, which means that other parts of the program don’t have to change.


# 17.12 Glossary

# method: A function that is defined inside a class definition and is invoked on instances of
# that class.

# positional argument: An argument that does not include a parameter name, so it is not a
# keyword argument.

# operator overloading: Changing the behavior of an operator like + so it works with a
# programmer-defined type.

# polymorphic: Pertaining to a function that can work with more than one type.