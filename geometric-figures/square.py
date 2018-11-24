# drawing a square with python

import turtle
import time

def square():

    pointer = turtle.Pen()

    for line in range(1,5):
        pointer.forward(200)
        time.sleep(0.25)
        pointer.left(90)

square()