# 19.1: Conditional expressions

# Assigning one of two values to a variable:
# y = math.log(x) if x > 0 else float('nan')

# Returning one of two values value, in this instance in a function:
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n-1)

# In general, you can replace a conditional statement with a conditional expression if both
# branches contain simple expressions that are either returned or assigned to the same variable.


# 19.2: List comprehensions

# Example:
# return [s for s in t if s.isupper()]

# List comprehensions are usually faster than the equivalent loops. However, they are harder to debug because you can't
# put print statements in them, so use them in simple cases.


# 19.3: Generator expressions

# Generator expressions are similar to list comprehensions, but with parentheses instead of
# square brackets.

# IMPORTANT:
# The result is a generator object that knows how to iterate through a sequence of values. But
# unlike a list comprehension, it does not compute the values all at once; it waits to be asked.
# The built-in function 'next' gets the next value from the generator.

# Can also use a for loop to iterate over the generator object, of course. If using a for loop after using next, the
# for loops will pick up where next left off.


# 19.4: 'any' and 'all'

# 'any' takes a sequence of boolean values and returns True if any of the values are True. It is often used with
# generator expressions:
def avoids(word, forbidden):
    """“Word avoids forbidden if there are not any forbidden letters in word."""
    return not any(letter in forbidden for letter in word)

# Using any with a generator expression is efficient because it stops immediately if it finds a
# True value, so it doesn’t have to evaluate the whole sequence (see
# https://stackoverflow.com/questions/16505456/how-does-this-input-work-with-the-python-any-function for why).

# 'all' is similar to 'any' but returns True iff every element of a sequence is True.

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

def concise_uses_all(word, required):
    return all(letter in word for letter in required)


# 19.5: Sets

# A set is like a dictionary with keys but no values. If you are thinking of making a dictionary with keys whose values
# are all 'none', you might as well make a set to save memory.

# Adding elements to a set and checking membership is fast.

# You can subtract one set from another.

def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

def concise_has_duplicates(t):
    """A concise version of has_duplicates. Works because an element can only appear in a set once."""
    return len(set(t)) < len(t)

def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

def set_avoids(word, forbidden):
    """Checks if a word avoids all the characters in forbidden, by using sets rather than 'any' and a generator
    object."""
    return set(word) - set(forbidden) == set(word)


# 19.6: Counters

# A Counter is like a set, except that if an element appears more than once, the Counter
# keeps track of how many times it appears. If you are familiar with the mathematical idea
# of a multiset, a Counter is a natural way to represent a multiset. A multiset differs from a list in that in a list,
# order matters, but it doesn't in a multiset.

# Counter is imported from collections

# You can initialize a Counter with a string, list, or anything else that supports iteration.

# Unlike dictionaries, Counters don’t raise an exception if you access an element that doesn’t
# appear. Instead, they return 0 (as that element occurs 0 times).

# Counters provide methods and operators to perform set-like operations, including addition, subtraction, union (|) and
# intersection (&). And they provide an often-useful method, most_common, which returns a list of value-frequency pairs,
# sorted from most common to least.

# Intersection finds values that occur in both of the sets operated on. However, operated on two Counters, it keeps the
# the keys from each but the value (frequency) is assigned to be the lower frequency between the two Counters.


# 19.7 defaultdict

# The collections module also provides defaultdict, which is like a dictionary except that
# if you access a key that doesn’t exist, it can generate a new value on the fly.

# For example:
from collections import defaultdict
d = defaultdict(list)

# Now, if you look up a key that doesn't exist, it will put that key in the dictionary with a corresponding value of [].

# t = d['new key']
# print(t)

# # t now gets a reference to the list in the dictionary, because of the nature of a list. So, when we modify t, the
# # value of the key 'new key' changes.
# print(d)
# t.append('new value')
# print(d)

# If you are making a dictionary of lists, you can often write simpler code using defaultdict.

# The below shows where defaultdict might be advantageous. signature is necessary for this example but it is not to be
# paid attention to.

def signature(s):
    """Returns the signature of this string.
    Signature is a string that contains all of the letters in order.
    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    """For a filename in which each line is but a word, this function returns a dictionary mapping the sorted version
    of each word to a list of words in the file that are its anagrams."""
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d.setdefault(t, []).append(word)
    return d

# This solution has the drawback that it makes (and returns) a new list pretty much every time (unless t is being added
# to the dictionary for the first time, in which case nothing is returned), regardless of whether
# it is needed. For lists, that’s no big deal, but if the factory function is complicated, it might
# be.

# We can avoid this problem and simplify the code using a defaultdict:

def all_anagrams(filename):
    d = defaultdict(list)
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d[t].append(word)
    return d

# Answer to mini exercise at the end of Section 19.7:

# def has_straightflush(self):
#     """Checks whether this hand has a straight flush.
#     Better algorithm (in the sense of being more demonstrably
#     correct). Of course, doesn't work unless PokerHand is imported.
#     """
#     # partition the hand by suit and check each
#     # sub-hand for a straight
#     d = defaultdict(PokerHand)
#     for c in self.cards:
#         d[c.suit].add_card(c)
#
#     # see if any of the partitioned hands has a straight
#     for hand in d.values():
#         if len(hand.cards) < 5:
#             continue
#         hand.make_histograms()
#         if hand.has_straight():
#             return True
#     return False


# 19.8: Named tuples

# Named tuples can be used to express a class definition more concisely. For example:

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return '(%g, %g)' % (self.x, self.y)

# can be rewritten as:

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

# where Point is the name of the class to create and ['x', 'y'] is the list of attributes it has.
# Point still will provide __init__ and __str__ without these having to be explicitly defined:

p = Point(1, 5)
print(p.x, p.y)
print(p)

# Can also treat a named tuple as a tuple:
print(p[0], p[1])

# Drawback of using named tuples for this purpose is that it is good for simple purposes, but you might later want to
# modify your class heavily. In that case, could define a new class that inherits from the named tuple:

class Pointier(Point):
    # add more methods here
    pass

# or just switch to a conventional class definition.


# 19.9 Getting keyword args

# * can be used in a function definition to gather its arguments into a tuple. However, * doesn't gather keyword
# arguments.

# ** can be used to gather the keyword arguments. For example:

def printall(*args, **kwargs):
    print(args, kwargs)

printall(1, 2.0, fourth='3')

# If you have a dictionary of keywords and values, you can use the scatter operator, ** to
# call a function:
d = dict(x=1, y=2)
print(Point(**d))


# 19.10: Glossary

# List comprehension: An expression with a for loop in square brackets that yields a new
# list.

# Factory: A function, usually passed as a parameter, used to create objects.