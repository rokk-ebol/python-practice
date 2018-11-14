# Body mass index calculation

def bmi_calc():

    question = input('Do you use metric system?: Y/N> ')
    metric_system = None

    if question == 'Y' or question == 'y' or question == 'yes': 
        metric_system = True

        height = float(input('Enter your height in meters: '))
        weight = float(input('Enter your weight in kilograms: '))

    elif question == 'N' or question == 'n' or question == 'no':
        metric_system = False

        height = float(input('Enter your height in feets: '))
        weight = float(input('Enter your weight in pounds: '))

        #converting to inches
        height = height * 12 

    else:
        print('incorrect answer')
        bmi_calc()

    bmi = None

    if metric_system == True:
        bmi = weight / (height ** 2)
    elif metric_system == False:
        bmi = (weight / (height ** 2)) * 703

    print(f'Your body mass index is {bmi:.2f}')

bmi_calc()