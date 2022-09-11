import turtle
import math

def arch_spiral(tur, a, c, revolutions):
    """Uses a turtle, tur, to draw a given number of revolutions of an Archimedian spiral of the form r = a * theta + c,
    where r is the distance of a point on the spiral from the origin, theta is the angle revolved through in radians and
    a & b are constants, c being the initial distance of the spiral from the origin and a being the spacing between
    points separated by 2pi radians."""
    w = 1
    v = a * w
    tur.pu()
    tur.fd(c)
    tur.pd()
    for i in range(revolutions * 40):
        t = i / 20 * math.pi
        x = (v * t + c) * math.cos(w * t)
        y = (v * t + c) * math.sin(w * t)
        tur.goto(x, y)

bob = turtle.Turtle()
arch_spiral(bob, 1, 10, 5)
turtle.mainloop()