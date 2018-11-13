#18 VOLUME OF A CYLINDER

import math as m

r = float(input("enter cylinder radius:> "))
h = float(input("enter cylinder height:> "))

PI = m.pi

v = PI*r**2*h 

print(f"Volume of a cylinder is {v:.1f}")

