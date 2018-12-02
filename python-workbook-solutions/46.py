#season from month and day

def season_from_month_and_day():

    month = input('Enter month: ').capitalize()
    day = int(input('Enter day: '))

    months = ['January', 'February', 'March', 'Arpril', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # input validation
    if day > 31 or day < 1 or month not in months:
        print('incorrect month or day')
        season_from_month_and_day()
        
    # logic 
    if month == 'March' and day <= 20:
        print('winter')
    elif month == 'March' or month == 'April' or month == 'May' or day <= 21 and month == 'June': 
        print('spring')
    elif month == 'June' or month == 'July' or month == 'August' or day <= 22 and month == 'September':
        print('summer')
    elif month == 'September' or month == 'October' or month == 'November' or day <= 21 and month == 'December':
        print('fall')
    elif month == 'December' or month == 'January' or month == 'February' or day <= 20 and month == 'March':
        print('winter')


season_from_month_and_day()