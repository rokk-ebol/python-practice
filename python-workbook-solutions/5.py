# 5 BOTTLE DEPOSITS

from decimal import Decimal

LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

less = int(input("how many bottles with liter or less do you have?: "))
more = int(input("how many bottles with more than one liter do you have?: "))

result = less * LESS_DEPOSIT + more * MORE_DEPOSIT

print("you have just earned %.2f dollars" % result)