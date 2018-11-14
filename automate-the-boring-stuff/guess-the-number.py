def guessingGame():

    import random

    print('\nWelcome to game \'Guess the number\'\n')

    from_num = int(input('From which number to guess: \n'))
    to_num = int(input('To which num to guess: \n'))

    if to_num <= from_num:
        print('Incorrect value. Please enter value, which is bigger than first number.')
        to_num = int(input('To which num to guess: '))

    number_of_guesses = int(input('How many tries?: \n'))

    secretNumber = random.randint(from_num, to_num)

    print(f'Guess the number between {from_num} and {to_num}')

    for guess in range(1,number_of_guesses+1):
        print(f'Take a guess.\nYou have {number_of_guesses} tries.')
        guess = int(input())
        number_of_guesses = number_of_guesses - 1

        if guess > secretNumber:
            print('The number is too high')
        elif guess < secretNumber:
            print('The number is too low')
        elif guess == secretNumber:
            print(f'Congratulations, you have guessed the secret number {secretNumber}')
        else:
            print('You have used all of your tries. Please, try again.')

    guessingGame()

guessingGame()