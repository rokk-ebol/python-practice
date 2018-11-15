# name that triangle

def name_that_triangle():

    side_a = int(input('Enter size a: '))
    side_b = int(input('Enter size b: '))
    side_c = int(input('Enter size c: '))

    sides = [side_a, side_b, side_c]

    if len(set(sides)) == 1:
        print('equilateral')
    elif len(set(sides)) == 2:
        print('isosceles')
    elif len(set(sides)) == 3:
        print('scalene')
    else:
        print('something is wrong.')
        name_that_triangle()


name_that_triangle()