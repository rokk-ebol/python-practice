import turtle
import time


def round(r,g,b):

    line = turtle.Pen()

    line.color(r,g,b)
    line.begin_fill()
    line.circle(200)
    line.end_fill()
    
    line.color(0,0,0)
    line.circle(200)

    time.sleep(5)



round(1,0,0)
round(0,1,0)
round(0,0,1)