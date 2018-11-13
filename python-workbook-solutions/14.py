# 14 HEIGHT UNITS

height = float(input("Enter your height in feets: "))
height_in_inches = height * 12
height_in_centimerters = height_in_inches * 2.54
height_in_meters = height_in_centimerters / 100

print(f"Your height in meters would be - {height_in_meters:.2f}, in centimeters - {height_in_centimerters:.2f}, in inches - {height_in_inches:.2f}. ")
