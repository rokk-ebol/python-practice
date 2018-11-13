# 24 UNITS OF TIME

SECONDS_IN_YEAR = 365 * 24 * 60 * 60
SECONDS_IN_DAY = 24 * 60 * 60
SECONDS_IN_HOUR = 60 * 60 

days = int(input('Enter number of days: '))
years = int(input('Enter number of years: '))
hours = int(input('Enter number of hours: '))
seconds = int(input('Enter number of seconds: '))

result = (years * SECONDS_IN_YEAR) + (days * SECONDS_IN_DAY) + (hours * SECONDS_IN_HOUR) + seconds

print('{0:,d}'.format(result))
