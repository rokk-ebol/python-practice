# 22 AREA OF A TRIANGLE AGAIN

from math import sqrt

s1 = float(input("enter s1 side of a triangle:> "))
s2 = float(input("enter s2 side of a triangle:> "))
s3 = float(input("enter s3 side of a triangle:> "))

s = (s1 + s2 + s3) / 2
area = sqrt(s * ((s - s1) * (s - s2) * (s - s3)))

print(f'triangle square is {area}')