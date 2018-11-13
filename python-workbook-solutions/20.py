# 20 IDEAL GAS LAW

import math as m 

temperature_in_celsius = float(input("Enter temperature in celsius:> "))
temperature_in_kelvins = 273.15 + temperature_in_celsius

volume = float(input("Enter volume of a tank in liters:> "))
pressure = float(input("Enter pressure in pascals:> "))

ideal_gas_constant = 8.314

amount_of_gas =  ideal_gas_constant * temperature_in_kelvins / pressure * volume

print(f"amount of gas is {amount_of_gas:.1f}")
