# 19 FREE FALL

import math as m 

h = float(input("input height from what we drop an object:> "))

init_speed = 0
acceleration = 9.8

final_speed = m.sqrt(init_speed + 2*acceleration*h)

print(f"the final speed is {final_speed:.2f} m/s")
