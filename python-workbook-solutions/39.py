# sound levels

def sound_levels():

    sound_level_in_db = int(input('Enter sound level in DB: '))

    if sound_level_in_db == 130:
        print('Sound level of a Jackhammer')
    elif sound_level_in_db > 130:
        print('Louder than Jackhammer')
    elif sound_level_in_db < 130 and sound_level_in_db > 106:
        print('Somewhere between Gas lawnmower and Jackhammer')
    else:
        print('error')

    #this logic works, so I can add multiple elif conditions, but I am too lazy for this

sound_levels()
