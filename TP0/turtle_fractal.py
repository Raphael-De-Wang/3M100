#!/usr/bin/env python
import turtle

def left_triangle(length):
    for i in xrange(3):
        turtle.forward(length)
        turtle.left(120)

def fractal_side(length, fractal):
    if fractal == 0:
        turtle.forward(length)
    else:
        length3 = length / 3.
        fractal_side(length3, fractal-1)
        turtle.right(60)
        fractal_side(length3, fractal-1)
        turtle.left(120)
        fractal_side(length3, fractal-1)
        turtle.right(60)
        fractal_side(length3, fractal-1)

def fractal_triangle(length, fractal):
    for i in xrange(3):
        fractal_side(length,fractal)
        turtle.left(120)

turtle.reset()
turtle.speed('fastest')
fractal_triangle(300, 4)
left_triangle(300)
turtle.exitonclick()
