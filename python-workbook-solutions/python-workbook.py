#1 MAILING ADDRESS

# print("Oleh Kurza")
# print("Kyivska oblast")
# print("Kruhlykova 14\n")

# #2 HELLO

# name = input("What is your name?: \n")
# print(name)

# #3 AREA OF A ROOM

# width = int(input("Enter the width value of a room: "))
# height = int(input("Enter the height value fo a room: "))

# square = width * height
# print(f"The square of a room is {square}.")

#4 AREA OF A FIELD

# SQT_FEET_IN_ACRE = 43560

# length = int(input("Input a length of a field in feet: "))
# width = int(input("Input a widht of a field in feet: "))

# result = length * width / SQT_FEET_IN_ACRE
# print(f"The result in acres is {result}")

#5 BOTTLE DEPOSITS
# from decimal import Decimal

# LESS_DEPOSIT = 0.10
# MORE_DEPOSIT = 0.25

# less = int(input("how many bottles with liter or less do you have?: "))
# more = int(input("how many bottles with more than one liter do you have?: "))

# # result = Decimal(less * LESS_DEPOSIT + more * MORE_DEPOSIT)
# result = less * LESS_DEPOSIT + more * MORE_DEPOSIT

# result = result

# print("you have just earned %.2f dollars" % result)

#6 TAX AND TIP

# tax_rate = 0.20
# tip = 0.18

# order = float(input('On what sum did you just order?: '))
# checkout = order + order * tax_rate + order * tip

# print('Checkout is: %.2f $' % checkout)

#7 SUM OF THE FIRST N POSITITVE INTEGERS

# n = abs(int(input("Enter a number 'n': ")))

# sum = (n * (n + 1)) / 2
# print(f'The sum is {int(sum)}')

# #8 WIDGEDTS AND GIZMOS

# widget_weight =  75 
# gizmo_weight = 112

# widget_order = int(input('How many widgets would you like to buy?: '))
# gizmo_order = int(input('How mant gizmos would you like to buy?: '))

# total_weight = widget_order * widget_weight + gizmo_order * gizmo_weight

# print(f"Your total order weight is {total_weight} gramms.")

#9 COMPOUND INTEREST

# savings_growth = 0.04
# deposit = float(input("How many funds do you plan to deposit?: "))

# year_one = deposit + deposit * savings_growth
# year_two = year_one + year_one * savings_growth
# year_three = year_two + year_two * savings_growth

# print(f"Your first year summary is {year_one:.2f}$")
# print(f"Your second year summary is {year_two:.2f}$")
# print(f"Your third year summary is {year_three:.2f}$")

# #10 ARITHMETIC
# from math import log10

# a = int(input("Enter value of an 'a' number: "))
# b = int(input("Enter value of an 'b' number: "))

# print(f'The base 10 logarithm of {a} is {log10(a)}')

# 11 FUEL EFFICIENCY

# liter = float(input('Input your fuel consumption on 100 km in liters: '))
# gallon = liter * 3.78
# kilometer = 1
# mile = kilometer * 1.6

# mpg = gallon / mile

# print(f'Your MPG efficiency in USA would be {mpg:.2f}')

# #12 DISTANCE BETWEEN TWO POINTS

# import math as m

# t1 = float(input("Enter latitude of first point in degrees:> "))
# g1 = float(input("Enter longtitude of first point in degrees:> "))

# t2 = float(input("Enter latitude of second point in degrees:> "))
# g2 = float(input("Enter longtitude second point in degrees:> "))

# #converting to radians

# t1 = t1 * 0.017453
# g1 = g1 * 0.017453

# t2 = t2 * 0.017453
# g2 = g2 * 0.017453

# distance = 6371.01 * m.acos(m.sin(t1) * m.sin(t2) + m.cos(t1) * m.cos(t2) * m.cos(g1-g2))

# print(f"The distance between points is {distance:.2f} km.")

#14 HEIGHT UNITS

# height = float(input("Enter your height in feets: "))
# height_in_inches = height * 12
# height_in_centimerters = height_in_inches * 2.54
# height_in_meters = height_in_centimerters / 100

# print(f"Your height in meters would be - {height_in_meters:.2f}, in centimeters - {height_in_centimerters:.2f}, in inches - {height_in_inches:.2f}. ")

#15 DISTANCE UNITS

# basicallly the same
 
#16 AREA AND VOLUME

# import math as m

# r = float(input("enter radius:> "))

# pi = m.pi
# area = pi*r**2
# volume = (4/3)*pi*r**3

# print(f"area of round is: {area:.2f}, volume of sphere is {volume:.2f}")

# #18 VOLUME OF A CYLINDER

# import math as m

# r = float(input("enter cylinder radius:> "))
# h = float(input("enter cylinder height:> "))

# PI = m.pi

# v = PI*r**2*h 

# print(f"Volume of a cylinder is {v:.1f}")


#19 FREE FALL

# import math as m 

# h = float(input("input height from what we drop an object:> "))

# init_speed = 0
# acceleration = 9.8

# final_speed = m.sqrt(init_speed + 2*acceleration*h)

# print(f"the final speed is {final_speed:.2f} m/s")

#20 IDEAL GAS LAW

# import math as m 

# temperature_in_celsius = float(input("Enter temperature in celsius:> "))
# temperature_in_kelvins = 273.15 + temperature_in_celsius

# volume = float(input("Enter volume of a tank in liters:> "))
# pressure = float(input("Enter pressure in pascals:> "))

# ideal_gas_constant = 8.314

# amount_of_gas =  ideal_gas_constant * temperature_in_kelvins / pressure * volume

# print(f"amount of gas is {amount_of_gas:.1f}")


#21 AREA OF A TRIANGLE

# h = float(input("enter height value:> "))
# b = float(input("enter base value:> "))

# area = (b * h) / 2
# print(f"triangle area is {area:.0f}.")

#22 AREA OF A TRIANGLE AGAIN

# from math import sqrt

# s1 = float(input("enter s1 side of a triangle:> "))
# s2 = float(input("enter s2 side of a triangle:> "))
# s3 = float(input("enter s3 side of a triangle:> "))

# s = (s1 + s2 + s3) / 2

# area = sqrt(s * ((s - s1) * (s - s2) * (s - s3)))

# print(f'triangle square is {area}')

# #23 AREA OF A REGULAR POLYGON

# from math import pi,tan

# lenght = float(input("length of each side:> "))
# number_of_sides = float(input("number of sides:> "))

# area = (number_of_sides * lenght**2) / (4 * tan(pi/number_of_sides))

# print(area)

#24 UNITS OF TIME

# SECONDS_IN_YEAR = 365 * 24 * 60 * 60
# SECONDS_IN_DAY = 24 * 60 * 60
# SECONDS_IN_HOUR = 60 * 60 

# days = int(input('Enter number of days: '))
# years = int(input('Enter number of years: '))
# hours = int(input('Enter number of hours: '))
# seconds = int(input('Enter number of seconds: '))

# result = (years * SECONDS_IN_YEAR) + (days * SECONDS_IN_DAY) + (hours * SECONDS_IN_HOUR) + seconds

# print('{0:,d}'.format(result))


# 25 UNITS OF TIME AGAIN

SECONDS_IN_YEAR = 365 * 24 * 60 * 60
SECONDS_IN_DAY = 24 * 60 * 60
SECONDS_IN_HOUR = 60 * 60 

days = int(input('Enter number of days: '))
years = int(input('Enter number of years: '))
hours = int(input('Enter number of hours: '))
seconds = int(input('Enter number of seconds: '))

print((years * SECONDS_IN_YEAR) + (days * SECONDS_IN_DAY) + (hours * SECONDS_IN_HOUR) + seconds)


