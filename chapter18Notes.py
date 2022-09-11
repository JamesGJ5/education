import random

# 18 Inheritance

# Inheritance is the ability to define a new class that is a modified version of an existing one.


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                        '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

        # Converting the suit and rank of the card into a 2-digit number of the same base as the number of ranks there
        # are, and then subtracting them for each card. I have yet to time-profile this but it definitely requires
        # fewer statements than the above method does.
        # return (self.suit - other.suit) * (len(Card.rank_names) - 1) + (self.rank - other.rank) < 0


# queenOfDiamonds = Card(1, 12)
# print(queenOfDiamonds)


# 18.2 Class attributes


# Variables like suit_names and rank_names, which are defined inside a class but outside
# of any method, are called class attributes because they are associated with the class object
# Card. This term distinguishes them from variables like suit and rank (which are made by self.suit and self.rank when
# the Card object is initalised), which are called instance attributes because they are associated with a particular
# instance.

# Card.rank_names will access the class attribute, while self.rank will access the instance attribute, 'self' referring
# to a particular Card object.


# 18.3 Comparing cards

queenOfDiamonds = Card(1, 12)
sixOfHearts = Card(2, 6)

# print(queenOfDiamonds < sixOfHearts)


# 18.4, 18.5, 18.6

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()


# 18.7 Inheritance

# When you define a class that inherits from another, it will inherit the other's __init__; you might have to override
# it by writing an __init__ for the child class (the class that inherits).


# 18.8 Class diagrams

# HAS-A relationship: objects of one class contain references to objects in another class. ThinkPython2e says Deck and
# Card have a HAS-A relationship, since a Deck HAS A Card (or multiple of them).

# IS-A: one class might inherit from another, so a Hand IS A type of Deck.

# DEPENDENCY: objects of one class might take objects of another class as parameters, or use objects of the other class
# as part of a computation. The book doesn't say that Deck and Card have a DEPENDENCY, probably because neither takes
# objects of the other as parameters in its __init__ method.
# TODO: check the above


# 18.9 Debugging

# You can have child classes that inherit from parent classes but override their methods. So, when a method is invoked
# upon an object in a complex script where there are many is-a relationships (i.e. a child class is a version of a
# parent class), then when you invoke a method of an object, it might be confusing which method is being invoked (i.e.
# which class it belongs to). The easiest way to debug and follow the flow of execution here is to add print statements
# to the beginning of the relevent methods, e.g. "Running {class}'s {method}". An alternative way is using the
# following function:

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

# Here’s a design suggestion: when you override a method, the interface of the new method
# should be the same as the old. It should take the same parameters, return the same type,
# and obey the same preconditions and postconditions. If you follow this rule, you will find
# that any function designed to work with an instance of a parent class, like a Deck, will also
# work with instances of child classes like a Hand and PokerHand. This is called the Liskov substitution principle.


# 18.10 Data encapsulation

# Data encapsulation is a good way of discovering class interfaces that allow us to make a sound development plan. See
# the current chapter for a good example regarding Markov analysis.

# Step by step data encapsulation development plan:

# 1. Start by writing functions that read and write global variables (when necessary).
# 2. Once you get the program working, look for associations between global variables
# and the functions that use them.
# 3. Encapsulate related variables as attributes of an object.
# 4. Transform the associated functions into methods of the new class.