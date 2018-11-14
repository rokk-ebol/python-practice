#Celsius to Kelvin and Fahrenheit

def temperature_converter():

    temperature = float(input('Enter temperature in Celsius: '))

    if temperature <= -273.15:
        print('Impossible temperature')
        temperature_converter()


    kelvin = temperature + 273.15
    fahrenheit = temperature * 1.8 + 32

    print(f'Your temperature is equal to {kelvin:.2f} in kelvins or {fahrenheit:.1f} degrees fahrenheit.')

temperature_converter()