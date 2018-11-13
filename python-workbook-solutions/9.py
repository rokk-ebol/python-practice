# 9 COMPOUND INTEREST

savings_growth = 0.04
deposit = float(input("How many funds do you plan to deposit?: "))

year_one = deposit + deposit * savings_growth
year_two = year_one + year_one * savings_growth
year_three = year_two + year_two * savings_growth

print(f"Your first year summary is {year_one:.2f}$")
print(f"Your second year summary is {year_two:.2f}$")
print(f"Your third year summary is {year_three:.2f}$")
