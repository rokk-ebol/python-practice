#SumoftheDigitsinanInteger

def sum_of_digits_in_integer():

    number = list((input('Enter 4-digits number: ')))
    number = [int(num) for num in number]

    result = sum(num for num in number)
    print(result)

sum_of_digits_in_integer()