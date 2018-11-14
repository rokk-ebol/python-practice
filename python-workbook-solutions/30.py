#units of pressure

def units_of_pressure():

    pressure_in_kilopascals = int(input('Input pressure in kilopascals: '))

    atmospheres = pressure_in_kilopascals * 0.0098
    mm_mercury = pressure_in_kilopascals * 7.50061
    pounds_per_sq_inch = pressure_in_kilopascals * 0.1450

    print(f'pressure equivalents: \n\natmospheres:\t {round(atmospheres)};\nmercury:\t {round(mm_mercury)};\npounds per sq inch:\t {round(pounds_per_sq_inch)}')

units_of_pressure()