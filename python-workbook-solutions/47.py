# birth date to astrological sigh

def birth_to_astro():

    month = input('Enter month: ').capitalize()
    day = int(input('Enter day: '))

    months = ['January', 'February', 'March', 'Arpril', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # input validation
    if day > 31 or day < 1 or month not in months:
        print('incorrect month or day')
        birth_to_astro()

    if month == 'December' and day > 21 or month == 'January' and day <= 20:
        print('Capricorn')
    elif month == 'January' and day > 20 or month == 'February' and day <= 19:
        print('Aquarius')
    elif month == 'February' and day > 19 or month == 'March' and day <= 20:
        print('Pisces')
    elif month == 'March' and day > 20 or month == 'April' and day <= 19:
        print('Aries')
    elif month == 'April' and day > 19 or month == 'May' and day <= 20:
        print('Taurus')
    elif month == 'May' and day > 20 or month == 'June' and day <= 20:
        print('Gemini')
    elif month == 'June' and day > 20 or month == 'July' and day <= 22:
        print('Cancer')
    elif month == 'July' and day > 22 or month == 'August' and day <= 22:
        print('Leo')
    elif month == 'August' and day > 22 or month == 'September' and day <= 22:
        print('Virgo')
    elif month == 'September' and day > 22 or month == 'October' and day <= 22:
        print('Libra')
    elif month == 'October' and day > 22 or month == 'November' and day <= 21:
        print('Scorpio')
    elif month == 'November' and day > 22 or month == 'December' and day <= 21:
        print('Sagittarius')


birth_to_astro()