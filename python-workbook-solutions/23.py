#23 AREA OF A REGULAR POLYGON

from math import pi,tan

lenght = float(input("length of each side:> "))
number_of_sides = float(input("number of sides:> "))

area = (number_of_sides * lenght**2) / (4 * tan(pi/number_of_sides))

print(area)