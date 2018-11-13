# 11 FUEL EFFICIENCY

liter = float(input('Input your fuel consumption on 100 km in liters: '))
gallon = liter * 3.78
kilometer = 1
mile = kilometer * 1.6

mpg = gallon / mile

print(f'Your MPG efficiency in USA would be {mpg:.2f}')
