from random import randint

def plant():
    crop = randint(0, 99999) # Number Id
    
    land = open('dump/land.txt', 'a')
    land.write(f'\n{crop}')
    land.close()

    return crop