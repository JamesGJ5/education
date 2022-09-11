# Exercise 17.1:

# See Time2.py for solution.


# Exercise 17.2:

class Kangaroo:
    """Represents a kangaroo with a pouch that can hold any object, including a kangaroo."""

    def __init__(self, contents=None):
        """Creates a kangaroo whose name can be input."""
        # If contents=[] above, we would have a problem, because when default values are mutable, contents = [] is
        # created only once. Therefore, different objects of the class called with contents=None would have
        # self.contents (if 'self.content = contents' was the statement used below) refer to the same empty list.
        # Therefore, if you put something in one kangaroo's pouch, another kangaroo would find that in its pouch too.
        # See http://thinkpython2.com/code/BadKangaroo.py for this issue, and
        # http://thinkpython2.com/code/GoodKangaroo.py where this issue is solved. Code with the issue is also far
        # below, greyed out.
        self.name = input("\nWhat is this kangaroo's name? \n")
        if contents == None:
            self.pouch_contents = []
        else:
            self.pouch_contents = contents

    def put_in_pouch(self, object):
        """Put an object in this kangaroo's pouch."""
        self.pouch_contents.append(object)

    def __str__(self):
        """Returns the contents of this kangaroo's pouch in string form. If any of the contents are kangaroos, it
        returns the contents of their pouches too."""
        statement = f"\nThe following objects are in {self.name}'s pouch:"
        substatements = '\n'
        for object in self.pouch_contents:
            if isinstance(object, Kangaroo):
                statement += '\n' + object.name
                substatements += str(object)
            else:
                statement += '\n' + str(object)
        return statement + substatements

if __name__ == '__main__':
    bigKangaroo = Kangaroo()
    mediumKangaroo1 = Kangaroo()
    mediumKangaroo2 = Kangaroo()
    smallKangaroo1 = Kangaroo()
    smallKangaroo2 = Kangaroo()
    smallKangaroo3 = Kangaroo()

    bigKangaroo.put_in_pouch(mediumKangaroo1)
    bigKangaroo.put_in_pouch(mediumKangaroo2)
    bigKangaroo.put_in_pouch("A string")
    mediumKangaroo1.put_in_pouch(smallKangaroo1)
    mediumKangaroo1.put_in_pouch(smallKangaroo2)
    mediumKangaroo2.put_in_pouch(smallKangaroo3)

    print(bigKangaroo)

# class Kangaroo:
#     """A Kangaroo is a marsupial."""
#
#     def __init__(self, name, contents=[]):
#         """Initialize the pouch contents.
#         name: string
#         contents: initial pouch contents.
#         """
#         self.name = name
#         self.pouch_contents = contents
#
#     def __str__(self):
#         """Return a string representaion of this Kangaroo.
#         """
#         t = [self.name + ' has pouch contents:']
#         for obj in self.pouch_contents:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)
#
#     def put_in_pouch(self, item):
#         """Adds a new item to the pouch contents.
#         item: object to be added
#         """
#         self.pouch_contents.append(item)
#
#
# kanga = Kangaroo('Kanga')
# roo = Kangaroo('Roo')
# kanga.put_in_pouch('wallet')
# kanga.put_in_pouch('car keys')
# kanga.put_in_pouch(roo)
#
# print(roo)