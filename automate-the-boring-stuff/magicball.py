def magicBall():

    import random
    
    ask = input('Ask a magic ball something: ')
    answers = ['yes', 'maybe', 'probably', 'definitely', 'no', 'definitely not', 'i don\'t know']

    print(f'The magic ball says {answers[random.randint(0, len(answers))]}')

    magicBall()

magicBall()