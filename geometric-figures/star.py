# Kinda looking cool star

import turtle
import time

def cool_star():

    pointer = turtle.Pen()

    for line in range(1,19):
        pointer.forward(200)
        time.sleep(0.1)

        if line % 2 == 0:
            pointer.left(175)
        else:
            pointer.left(225)

cool_star()