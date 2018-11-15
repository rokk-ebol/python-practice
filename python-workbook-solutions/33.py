# Day old bread

how_many = float(input('How many bread do you want to buy? : '))

regular_price = 3.49
discount = 0.60

result = how_many * regular_price * discount

print(f'Regular price on your order would be: {regular_price*how_many:.2f}$ ')
print(f'Discount price is  {result:.2f}$')