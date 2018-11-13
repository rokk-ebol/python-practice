def calc():

    types = ['diesel','gasoline','дизель','бензин','дизельний','бензиновий']

    age = int(input('Введіть вік авто:'))
    cc = int(input('Введіть об\'єм двигуна (у куб см): '))
    engine = input('Вкажіть тип двигуна - diesel / gasoline: ')
    price = None

    if engine == 'diesel' or 'дизель' or 'дизельний':
        tax = 75
    elif engine == 'gasoline' or 'бензиновий' or 'бензин':
        tax = 50
    else:
        print('неправильно вказали тип двигуна: впишіть diesel, дизель дизельний або gasoline, бензиновий, бензин')
        calc()
    price = tax * (cc / 1000) * age
    
    print(f'Ціна акцизу: {int(price)}EUR.')
    print('Для виходу тисніть CTRL + C')

    calc()

calc()