# 12.1 TUPLES ARE IMMUTABLE:

# The below are equivalent; the comma is necessary to make a singleton
# tuple:
t1 = ('a',)
t2 = 'a',
t3 = ("a",)
t4 = "a",

# Creates an empty tuple since no argument given:
t5 = tuple()

# If the argument is a sequence, the result is a tuple whose elements are the
# elements of that sequence:
t6 = tuple("hello")

# Most list operators also work on tuples, including the slice operator.

# You cannot modify tuple elements but you can replace one tuple with another:
t7 = tuple("well") + t6

# The relational operators work, too. Python starts by comparing the first element
# from each sequence. If they are equal, it goes on to the next elements, and so
# on, until it finds elements that differ. Subsequent elements are not considered
# (even if they are really big). If Python finds that, for an element in one tuple,
# there isn't an element at the same index position in the other, Python declares
# the longer tuple as larger; but only if it reaches the point at which this
# comparison can be made (i.e. the shorter list doesn't win out for earlier
# elements).
# print((0, 1, 2, 1) < (1, 1, 2))


# 12.2 TUPLE ASSIGNMENT:

a = 5
b = 6

# This is an assignment, in which the left side is a typle of variables and the
# right is a tuple of expressions. Each value is assigned to its respective
# variable. All expressions on the right are evaluated before any assignments. This
# assignment is a fast way to swap the values of a an b. The right can be any kind
# of sequence (string, list or tuple).
a, b = b, a
# print(a)
# print(b)

# Example of the above in less bare circumstances. Split returns a list (which is
# a sequence, as required of a right hand side (see above).
addr = "jamesgracajones@gmail.com"
uname, domain = addr.split("@")
# print(uname, domain)


# 12.3 TUPLES AND RETURN VALUES

# Returning a tuple can be useful if you want a function to return, essentially,
# multiple values!

# The built-in function divmod takes two arguments and returns a tuple of two
# values, the quotient and remainder.
t8 = divmod(11, 3)
# print(t8)


# 12.4 VARIABLE-LENGTH ARGUMENT TUPLES:

# In a function defintion, a parameter name that begins with * gathers arguments
# given into a tuple.
def printall(*args):
    print(args)

# If you have a sequence of values and you want to pass it to a function as
# multiple arguments, you can use the * operator to scatter the sequence. Here, this
# is done because t9 is a tuple, which divmod can't accept as an argument.
t9 = (16, 5)
t10 = divmod(*t9)
# print(t10)

# The max and min built-in functions use variable-length argument tuples but sum
# doesn't (it accepts exactly two arguments).

def sumall(* args):
    """Takes any number of arguments and returns their sum.

    args: all of the same type"""

    # Can use index because * args collects the given arguments as a tuple, as
    # earlier stated
    sum = args[0]

    for arg in args[1:]:
        sum += arg

    return sum


# 12.5 LISTS AND TUPLES:

# The built-in function zip interleaves multiple sequences into a zip object. A
# zip object is an iterator, as it iterates through a sequence.
s = 'abc'
li1 = [0, 1, 2]
zip1 = zip(s, li1)
# for pair in zip1:
    # print(pair)

# You can't use an index to select an element from an iterator but you can use the
# zip object to make a list and then do so on that:
li2 = list(zip1)

# If the sequences are of different lengths, the reuslt of list(zip(s, li1)) has the
# length of the shorter sequence, with the rest of the longer sequence cut off.

# print(li2)
# for letter, number in li2:
#     print(letter, number)

# Below is a way to use zip, for and tuple assignment in an idiom that is useful
# for traversing mutliple sequences simultaneously.
def has_match(t1, t2):
    """Takes two sequences and returns True if there's an index i such that
    t1[i] == t2[i].

    t1: sequence
    t2: sequence
    """

    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

# The result of enumerate below is an enumerate object, which iterates a sequence
# of pairs (containing an index and an element from the given sequence).
# for index, element in enumerate("abc"):
#     print(index, element)


# 12.6 DICTIONARIES AND TUPLES:

d = {'a':0, 'b':1, 'c':2}

# Dictionaries have a method called items that returns a sequence of tuples, where
# each tuple is a key-value pair, forming a dict_items object:
t = d.items()
# print(t)
# for key, value in t:
#     print(key, value)

# Vice versa, you can also use a list of tuples to initialise a new dictionary.
# This does the reverse of t = d.items():
t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)

# More concise way to create the dictionary:
d = dict(zip("abc", range(3)))
# print(d)

# Dictionary method update takes a list of tuples and adds them to an existing
# dictionary as key-value pairs.
li = [("a1", 0), ("b1", 1), ("c1", 2)]
d.update(li)
# print(d)

last = "Graca-Jones"
first = "Stephen James"
number = "07453565811"

# The expression in square brackets below is a tuple being assigned to dictionary
# called directory as a key, with value given by number.
directory = {}
directory[last, first] = number


# 12.7 SEQUENCES OF SEQUENCES:

# As well as lists of tuples, nearly all the examples in this chapter thus far
# also work with lists of lists, tuples of tuples, and tuples of lists - i.e.,
# other sequences of sequences (strings, lists and tuples).

# String limitations in choosing sequences: immutable, and elements have to be
# characters.

# When tuples over lists:
# -->  In some contexts, like a return statement, it is syntactically simpler to
# create a tuple than a list.
# --> If you want to use a sequence as a dictionary key, you have to use an
# immutable type like a tuple or string.
# --> If you are passing a sequence as an argument to a function, using tuples
# reduces the potential for unexpected behavior due to aliasing.

# sorted function takes any sequence and returns a new list with the same elements
# in sorted order; oft used on tuples to make up for the sort function's inability
# to modify immutable types.

# reversed returns an iterator that traverses the list in reverse order, used to
# make up for reverse.


# 12.8 DEBUGGING

# Lists, dictionaries and tuples are examples of data structures.
# Compound data structures, like lists of tuples, are useful but prone to what
# shape errors (errors due to a data structure having the wrong type, size or
# structure. For example, if you are expecting a list with one integer and I give you a plain
# old integer (not in a list), it won’t work.

# The module structshape isn't built-in, but is something downloaded from Allen
# Downey's GitHub repository for Think Python 2e. It can be used to keep track of
# your data structures.
from structshape import structshape

t1 = [[1, 2], (3,), [4, 5], 6]
print(structshape(t1))


# 12.9 GLOSSARY:

# iterator: An object that can iterate through a sequence, but which does not provide list
# operators and methods