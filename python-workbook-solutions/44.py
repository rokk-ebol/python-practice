# Date to Holiday name

month = input('Enter month name: ').capitalize()
date = input('Enter date: ')

if month == 'January' and date == '1':
    print('New years day')
elif month == 'July' and date == '1':
    print('Canadas day')
elif month == 'December' and date == '25':
    print('Christmas day')
else:
    print('Either it is not a date either it is not a holiday')