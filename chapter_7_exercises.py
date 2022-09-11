import math

# Exercise 7.1:

def mysqrt(a):
    """Takes a number, a, and estimates its square root."""
    x = a / 2
    while True:
        y = (x + a / x) / 2
        if y == x:
            return(x)
        x = y

def test_square_root():
    """Draws a table showing the estimates of the square root of a by mysqrt and math.sqrt, and compares them, for
    integers of a between 1 and 9."""
    print("a   mysqrt(a)          math.sqrt(a)       diff\n"
          "_   _________          ____________       ____")
    a = 1.0
    while a < 10:
        print(str(a), str(mysqrt(a)) + (18 - len(str(mysqrt(a)))) * " ",
              str(math.sqrt(a)), (18 - len(str(math.sqrt(a)))) * " ",
              str(abs(math.sqrt(a) - mysqrt(a))))
        a += 1

# Exercise 7.2:

def eval_loop():
    """Takes a user's input and evaluates it, unless the input is "done", at which point the last evaluated input will
    be returned."""
    result = None
    while True:
        userinput = input("> ")
        if userinput == "done":
            return result
        result = eval(userinput)

# Exercise 7.3:

def estimate_pi():
    """Estimates pi using the Ramanujan Summation, the final used term being the first term smaller than 1e-15."""
    sum = 0
    k = 0
    while True:
        term = 2 * math.sqrt(2) * math.factorial(4 * k) * (1103 + 26390 * k) / (9801 * math.factorial(k) ** 4 * 396
                                                                                    ** (4 * k))
        if abs(term) < 1e-15:
            break
        sum += term
        k += 1
    return 1 / sum