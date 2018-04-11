from random import randint

def roll_dice():
    print(randint(1, 6))

def init_game():
    roll_dice()
    cmd = input("Do you want to play another game? (Y/n) \n")
    if not cmd or cmd.lower() == 'y':
        init_game()


init_game()