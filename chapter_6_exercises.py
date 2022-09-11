# Exercise 6.2:

def ack(m, n):
    """Evaluates the Ackerman function given non-negative integers m and n."""
    if not isinstance(m, int) or not isinstance(n, int) or m < 0 or n < 0:
        print("m and n must be non-negative integers.")
    elif m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

# Exercise 6.4:

def is_power(a, b):
    """Takes the number a and returns True if it a power of b."""
    if a == b:
        return True
    elif a < b:
        return
    else:
        return is_power(a/b, b)

def gcd(a, b):
    """Takes two numbers a and b and returns their greatest common divisor."""
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)