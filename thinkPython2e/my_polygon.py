from math import *
import turtle
bob = turtle.Turtle()

# Uses a turtle, t, to draw connected steps, each of a given step_length (in px), at a given step_angle (in degrees)
    # to each other
def polyline(t, steps, step_length, step_angle):
    for i in range(steps):
        t.fd(step_length)
        t.lt(step_angle)

# Uses a turtle, t, to draw a polygon with a given number of sides, each with a given side_length in px
def polygon(t, sides, side_length):
    ext_angle = 360 / sides
    polyline(t, sides, side_length, ext_angle)

# Uses a turtle, t, to draw an approxiamte arc of a given radius (in px) and angle (in degrees)
def arc(t, radius, angle):
    circumference = 2 * pi * radius
    arc_length = circumference * angle / 360
    steps = int(arc_length / 3) + 1
    step_length = arc_length / steps
    step_angle = float(angle) / steps
    polyline(t, steps, step_length, step_angle)

# Uses a turtle, t, to draw an approximate circle of a given radius (in px)
def circle(t, radius):
    arc(t, radius, 360)

circle(bob, 50)
turtle.mainloop()