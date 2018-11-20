# freq to note

def freq_to_note():

    C4 = 261.63
    D4 = 293.66
    # E4 = 329.63
    # F4 = 349.24
    # G4 = 392.00
    # A4 = 440.00
    # B4 = 493.88  

    step = 1.00

    freq = float(input('Enter frequency: '))

    if freq >= C4 - step and freq <= C4 + step:
        print('C4 note')
    elif freq >= D4 - step and freq <= D4 + step:
        print('D4 note')
    else:
        print('Not a known note yet')

    '''
    overall logic is working so i proceed to a next task
    '''

freq_to_note()