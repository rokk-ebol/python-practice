# 4 AREA OF A FIELD

SQT_FEET_IN_ACRE = 43560

length = int(input("Input a length of a field in feet: "))
width = int(input("Input a widht of a field in feet: "))

result = length * width / SQT_FEET_IN_ACRE

print(f"The result in acres is {result}")