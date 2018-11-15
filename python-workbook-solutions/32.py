#sort three integers

def sort_three():

    num_1 = int(input('Enter first number: '))
    num_2 = int(input('Enter second number: '))
    num_3 = int(input('Enter third number: '))

    lst = [num_1,num_2,num_3]

    lst = sorted(lst)

    print(lst)

sort_three()