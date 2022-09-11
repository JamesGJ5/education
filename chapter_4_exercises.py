# Exercise 4.1:

"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle


def square(t, length):
    """Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

# if __name__ == '__main__':
#     bob = turtle.Turtle()
#
#     # draw a circle centered on the origin
#     radius = 100
#     bob.pu()
#     bob.fd(radius)
#     bob.lt(90)
#     bob.pd()
#     circle(bob, radius)
#
#     # wait for the user to close the window
#     turtle.mainloop()

# Exercise 4.2

def petal(t, arc_radius, intra_petal_angle):
    """Draws a petal of two arcs, subtended by intra_petal_angle and of radius arc_radius."""
    for i in range(2):
        arc(t, arc_radius, intra_petal_angle)
        t.lt(180 - intra_petal_angle)

def flower(t, petals, arc_radius, intra_petal_angle):
    """Draws a flower with petals number of petals, with arcs of radius arc_radius and with petals of two arcs subtended
    by intra_petal_angle"""
    inter_petal_angle = 360 / petals
    for i in range(petals):
        petal(t, arc_radius, intra_petal_angle)
        t.lt(inter_petal_angle)

def isosceles(t, vertex_angle, leg_length):
    """Uses a turtle, t, to draw an equilateral triangle of a given vertex_angle and given leg_length"""
    base_angle = (180 - vertex_angle) / 2
    base_length = 2 * leg_length * math.sin(vertex_angle * math.pi / 360)
    t.fd(leg_length)
    t.lt(180 - base_angle)
    t.fd(base_length)
    t.lt(180 - base_angle)
    t.fd(leg_length)

def pie(t, sections, leg_length):
    """Uses a turtle, t, to draw a regular polygon with a given number of isosceles of a given
    leg_length"""
    vertex_angle = 360 / sections
    for i in range(sections):
        isosceles(t, vertex_angle, leg_length)
        t.lt(180)

bob  = turtle.Turtle()
pie(bob, 3, 50)
turtle.mainloop()