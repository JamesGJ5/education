# Exercise 19.11:

def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes
    returns: int
    """
    # Be careful, don't swap around the order of the k == 0 and n == 0 conditional statements or this thing won't work.
    # If this order isn't retained, then implementing recursion by creating two new function calls with the arguments
    # n-1, k and n-1, k-1 will not work with the base cases to create the correct result. Think of 1C1, for example.

    # k == 0 is the base case corresponding to the virtual zero on either side of a row of Pascal's triangle.
    # if k == 0:
    #     return 1

    # n == 0 is the base case corresponding to the virtual row just above the top of Pascal's triangle.
    # if n == 0:
    #     return 0

    # This recursion works because it is reminiscent of adding two horizontally adjacent numbers in Pascal's triangle
    # to find the number horizontally in between them but in the row below.
    # res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    # return res

    # Be careful, don't swap around the order of the k == 0 and n == 0 conditional statements or this thing won't work.
    # If this order isn't retained, then implementing recursion by creating two new function calls with the arguments
    # n-1, k and n-1, k-1 will not work with the base cases to create the correct result. Think of 1C1, for example.

    return 1 if k == 0 else 0 if n == 0 else (binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1))

print(binomial_coeff(5, 2))