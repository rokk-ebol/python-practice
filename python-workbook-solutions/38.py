#month name to number of days

def month_to_days():

    month = input('Enter name of the month: ')
    month = month.capitalize()

    long_months = ['January','March','May','July','August','October','December']
    short_months = ['April','June','September','November']

    if month in long_months:
        print('31 days')
    elif month in short_months:
        print('30 days')
    elif month == 'February':
        print('28 or 29 days')
    else:
        print('Enter full name of the month properly')
        month_to_days()

month_to_days()