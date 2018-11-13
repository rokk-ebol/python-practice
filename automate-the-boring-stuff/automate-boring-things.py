# def guessingGame():

#     import random

#     print('\nWelcome to game \'Guess the number\'\n')

#     from_num = int(input('From which number to guess: \n'))
#     to_num = int(input('To which num to guess: \n'))

#     if to_num <= from_num:
#         print('Incorrect value. Please enter value, which is bigger than first number.')
#         to_num = int(input('To which num to guess: '))

#     number_of_guesses = int(input('How many tries?: \n'))

#     secretNumber = random.randint(from_num, to_num)

#     print(f'Guess the number between {from_num} and {to_num}')

#     for guess in range(1,number_of_guesses+1):
#         print(f'Take a guess.\nYou have {number_of_guesses} tries.')
#         guess = int(input())
#         number_of_guesses = number_of_guesses - 1

#         if guess > secretNumber:
#             print('The number is too high')
#         elif guess < secretNumber:
#             print('The number is too low')
#         elif guess == secretNumber:
#             print(f'Congratulations, you have guessed the secret number {secretNumber}')
#         else:
#             print('You have used all of your tries. Please, try again.')

#     guessingGame()

# guessingGame()


# def magicBall():

#     import random

#     # print('\nWelcome to the magic ball!\n')
    
#     ask = input('Ask a magic ball something: ')
#     answers = ['yes', 'maybe', 'probably', 'definitely', 'no', 'definitely not', 'i don\'t know']

#     print(f'The magic ball says {answers[random.randint(0, len(answers))]}')

#     magicBall()

# magicBall()

# def collatz(number):    

#     if number % 2 == 0:
#         print(number // 2)
#         return number // 2
        
#     elif number % 2 == 1:
#         print(3 * number + 1)
#         return 3 * number + 1

# try:
#     n = int(input('number: '))
# except ValueError:
#           print("Please enter a valid INTEGER.")

# n = int(input('number: '))

# while n != 1:
#     n = collatz(int(n))

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

text = text.split(' ')

print(text)