# dog years
def dog_age_calc():

    age = int(input('enter your dog\'s age: '))

    dog_years = None

    if age <= 2:
        dog_years = age * 10.5
        print(f'Yor dog is {dog_years} dog years old')
    elif age > 2:
        dog_years = 21 + (age - 2) * 4
        print(f'Yor dog is {dog_years} dog years old')
    elif age <= 0:
        print('should be more than 0')
        dog_age_calc()
    else:
        print('error')
        dog_age_calc()

dog_age_calc()