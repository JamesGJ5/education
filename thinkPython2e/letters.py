import turtle
import math

def polyline(t, n, length, angle):
    """Uses turtle t to draws n line segments each of a given length in px and inter-segment angle in degrees."""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Uses turtle t to draw an arc with the given radius r in px and angle arc subtends in degrees."""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    """Uses turtle t to draw a circle with the given radius r in px."""
    arc(t, r, 360)

def dot(t):
    t.pu()
    t.fd(55)
    t.lt(90)
    t.pd()
    circle(t, 5)

def draw_a(t):
    t.pu()
    arc(t, 50, 90)
    t.pd()
    circle(t, 50)
    t.lt(180)
    t.fd(50)

def draw_b(t):
    t.lt(90)
    t.fd(200)
    t.lt(180)
    t.fd(150)
    circle(t, 50)

def draw_c(t):
    t.lt(150)
    arc(t, 50, 240)

def draw_d(t):
    draw_a(t)
    t.lt(180)
    t.fd(200)

def draw_e(t):
    t.fd(100)
    t.lt(90)
    arc(t, 50, 315)

def draw_f(t):
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(100)
    t.lt(180)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)

def draw_g(t):
    draw_a(t)
    t.fd(50)
    t.lt(180)
    t.pu()
    arc(t, 50, 180)
    t.pd()
    arc(t, 50, 180)

def draw_h(t):
    t.lt(90)
    t.fd(200)
    t.lt(180)
    t.fd(150)
    t.lt(180)
    arc(t, 50, -180)
    t.fd(50)

def draw_i(t):
    t.lt(90)
    t.fd(150)
    dot(t)

def draw_j(t):
    t.lt(90)
    t.pu()
    arc(t, 50, 180)
    t.pd()
    arc(t, 50, 180)
    t.fd(100)
    dot(t)

def draw_k(t):
    t.lt(90)
    t.fd(200)
    t.lt(180)
    t.fd(100)
    t.lt(135)
    t.fd(100*math.sqrt(2))
    t.rt(135)
    draw_v(t)

def draw_l(t):
    t.rt(90)
    t.fd(150)
    arc(t, 50, 180)

def draw_m(t):
    t.rt(90)
    t.fd(100)
    for i in range(2):
        t.rt(90)
        draw_u(t)

def draw_n(t):
    draw_r(t)
    t.fd(50)

def draw_o(t):
    circle(t, 50)

def draw_p(t):
    t.lt(180)
    draw_d(t)

def draw_q(t):
    draw_a(t)
    t.fd(50)
    t.lt(135)
    t.fd(50)

def draw_r(t):
    t.rt(90)
    t.fd(100)
    t.lt(180)
    t.fd(50)
    arc(t, 50, -180)

def draw_s(t):
    t.lt(150)
    arc(t, 50, 210)
    arc(t, 50, -210)

def draw_t(t):
    draw_l(t)
    t.pu()
    t.fd(100)
    t.lt(90)
    t.pd()
    t.fd(150)

def draw_u(t):
    t.rt(90)
    t.fd(50)
    arc(t, 50, -180)
    t.fd(50)

def draw_v(t):
    t.rt(45)
    t.fd(100*math.sqrt(2))
    t.lt(90)
    t.fd(100*math.sqrt(2))

def draw_w(t):
    t.rt(60)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)

def draw_x(t):
    draw_y(t)
    t.fd(50)

def draw_y(t):
    t.lt(60)
    t.fd(100)
    t.lt(120)
    t.pu()
    t.fd(50)
    t.pd()
    t.lt(120)
    t.fd(50)

def draw_z(t):
    t.fd(50)
    t.rt(120)
    t.fd(100)
    t.lt(120)
    t.fd(50)

bob = 2
john = bob + 1
bob = 3