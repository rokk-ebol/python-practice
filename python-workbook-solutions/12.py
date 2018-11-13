#12 DISTANCE BETWEEN TWO POINTS

import math as m

t1 = float(input("Enter latitude of first point in degrees:> "))
g1 = float(input("Enter longtitude of first point in degrees:> "))

t2 = float(input("Enter latitude of second point in degrees:> "))
g2 = float(input("Enter longtitude second point in degrees:> "))

#converting to radians

t1 = t1 * 0.017453
g1 = g1 * 0.017453

t2 = t2 * 0.017453
g2 = g2 * 0.017453

distance = 6371.01 * m.acos(m.sin(t1) * m.sin(t2) + m.cos(t1) * m.cos(t2) * m.cos(g1-g2))

print(f"The distance between points is {distance:.2f} km.")