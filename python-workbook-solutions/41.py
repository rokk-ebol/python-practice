# note to frequency

def inputing_notes():

    '''checking if note is correct'''
    note = (input('enter note: '))

    if len(note) > 2:
        print('incorrect note, try again')
        inputing_notes()
    elif note[1].isdigit() == False:
        print('incorrect note, try again')
        inputing_notes()

    octave = note[1]

    return note, octave


'''writing result into global variables'''
note, octave = inputing_notes()


def note_to_freq(note, octave):

    octave = int(octave)
    note = note[0].capitalize()

    C4 = 261.63
    D4 = 293.66
    E4 = 329.63
    F4 = 349.24
    G4 = 392.00
    A4 = 440.00
    B4 = 493.88

    print('Note frequency is being measured in herz')
    
    if note == 'C':
        freq = C4
    elif note == 'D':
        freq = D4
    elif note == 'E':
        freq = E4
    elif note == 'G':
        freq = G4
    elif note == 'F':
        freq = F4
    elif note == 'A':
        freq = A4
    elif note == 'B':
        freq = B4

    freq = freq / 2 ** (4 - octave)

    print(freq)


note_to_freq(note, octave)
    
    
    

