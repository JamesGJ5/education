import math

def compare(x, y):
    """Returns 1 if x > y, 0 if x = y and -1 if x < y."""
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def hypotenuse(leg_one, leg_two):
    """Takes a right triangle with two legs (shorter sides) of given lengths and computes the length of the
    hypotenuse."""
    return math.sqrt(leg_one**2 + leg_two**2)

def is_between(x, y, z):
    """Returns True if x <= y <= z and False otherwise."""
    return x <= y <= z

def factorial(n):
    """Computes the factorial of n. This function definition contains scaffolding that clarifies what the flow of
        execution is doing and when."""
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result