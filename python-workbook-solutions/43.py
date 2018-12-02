# Faces on money

denomination = int(input('Enter dollar denomination: '))

if denomination == 1:
    print('George Washington')
elif denomination == 2:
    print('Thomas Jefferson')
elif denomination == 5:
    print('Abraham Lincoln')
elif denomination == 10:
    print('Alexander Hamilton')
elif denomination == 50:
    print('Ulysses Grant')
elif denomination == 100:
    print('Benjamin Franklin')
else:
    print('this denomination does not exist')