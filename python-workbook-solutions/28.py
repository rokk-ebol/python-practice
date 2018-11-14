#wind chill

def wind_chill_index():

    air_temperature = float(input('Enter temperature in Celsius: '))
    wind_speed = float(input('Enter speed of wind in kmph: '))

    if air_temperature <= 10.0 and wind_chill_index <= 4.8:
        print('The wind chill index is only considered valid for temperatures less than or equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per hour.')

        wind_chill_index()

    wind_chill = 13.12 + \
                0.6215 * air_temperature + \
                11.37 * wind_speed**0.16 + \
                0.3965 * air_temperature * wind_speed**0.16

    print(f'wind chill index is: {round(wind_chill)}')

wind_chill_index()
