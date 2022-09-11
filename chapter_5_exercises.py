# Exercise 5.1:

import time
import math
import turtle


def epoch_time():
    unix_epoch = time.time() # Gives number of seconds elapsed since the UNIX Epoch.
    day_seconds = 60 * 60 * 24
    days_since = unix_epoch // day_seconds

    seconds_today = unix_epoch % day_seconds
    minutes_today = seconds_today / 60
    hours_today = math.floor(minutes_today / 60) # Gives the number of complete hours elapsed today

    seconds_this_minute = math.floor(seconds_today % 60) # Gives the number of complete seconds elapsed this minute
    minutes_this_hour = math.floor(minutes_today % 60) # Gives the number of complete minutes elasped this hour

    print(str(days_since) + " days, " + str(hours_today) + " hours, " + str(minutes_this_hour) + " minutes, " +
        str(seconds_this_minute) + " seconds.")

# Exercise 5.2:

def check_fermat():
    a = int(input("Choose a value for a:\n"))
    b = int(input("Choose a value for b:\n"))
    c = int(input("Choose a value for c:\n"))
    n = int(input("Choose a value for n:\n"))
    left = a**n + b**n
    right = c**n
    if left == right:
        if n > 2:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("Both sides are equal but n isn't > 2 so Fermat hasn't been proven wrong.")
    else:
        print("Both sides are different.")

# Exercise 5.3:

def is_triangle():
    """Prompts user to enter three side lengths and determines the type of triangle they can constitute."""

    side_one = int(input("Enter the length of side one:\n"))
    side_two = int(input("Enter the length of side two:\n"))
    side_three = int(input("Enter the length of side three:\n"))

    if side_one <= 0 or side_two <= 0 or side_three <= 0:
        print("Input side lengths must be greater than or equal to zero, please.")
    elif side_one > side_two + side_three or side_two > side_one + side_three or side_three > side_one + side_two:
        print("No triangle can be made.")
    elif side_one == side_two + side_three or side_two == side_one + side_three or side_three == side_one + side_two:
        print("A degenerate triangle can be made.")
    else:
        print("A non-degenerate triangle can be made.")

# Exercise 5.4:

    """Takes two values, n and s, and increments n by -1 in each pass, and s by n in each pass, until n becomes 0, at which 
    point the value for s is printed."""

# Exercise 5.5:

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

# Exercise 5.6:

def koch(t, x):
    if x < 3:
        t.fd(x)
    else:
        koch(t, x/3)
        t.lt(60)
        koch(t, x/3)
        t.rt(120)
        koch(t, x/3)
        t.lt(60)
        koch(t, x/3)

def snowflake(t, area):
    x = area * 4 / (1.6 * math.sqrt(3))
    for i in range(3):
        koch(t, x)
        t.rt(120)

bob = turtle.Turtle()
snowflake(bob, 20)
turtle.mainloop()