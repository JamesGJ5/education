# Exercise 3.1:

    # # Takes a string s and prints the string with enough leading spaces for the last string character to be in column 70
    # def right_justify(s):
    #     spaces = 70 - len(s)
    #     result = ' ' * spaces + s
    #     print(result)

# Exercise 3.2:

    # # Takes a function object and a value and calls the function twice, passing the value as an argument
    # def do_twice(f,v):
    #     f(v)
    #     f(v)
    #
    # # Prints the string "spam"
    # def print_spam():
    #     print("spam")
    #
    # # Takes a value and prints the value twice
    # def print_twice(v):
    #     print(v)
    #     print(v)
    #
    # # Takes a function object and a value and calls the function four times with aid of do_twice(f,v), passing the value as
    # # an argument
    # def do_four(f,v):
    #     do_twice(f,v)
    #     do_twice(f,v)

# Exercise 3.3:

    # # Prints the required number of verticals for a given row
    # def print_verticals(string):
    #     print(string, end="|\n")
    #     print(string, end="|\n")
    #     print(string, end="|\n")
    #     print(string, end="|\n")
    #
    # # Prints a grid of a given number of rows and columns
    # def grid(rows, columns):
    #     horizontal = "+----"
    #     vertical = "|    "
    #     for i in range(rows):
    #         print(horizontal*columns, end="+\n")
    #         print_verticals(vertical*columns)
    #     print(horizontal * columns, end="+")
    #
    # grid(1, 1)