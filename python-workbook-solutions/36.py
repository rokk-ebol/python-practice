#vowel or consolant

def vowel_or_consolant():

    vowels = ['a','e','i','o','u']

    input_letter = input('Enter one letter:')


    if input_letter in vowels:
        print('This is vowel')
    elif input_letter.isnumeric() == True:
        print('Input letter, not a number!')
        vowel_or_consolant()
    elif len(input_letter) > 1:
        print('Input no more than one letter!')
        vowel_or_consolant()
    elif input_letter == 'y':
        print('\'y\' is a vowel, but sometimes \'y\' is a consonant')
    else:
        print('This is consolant')
    
vowel_or_consolant()
