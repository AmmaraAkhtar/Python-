import random

def game():
    print("Welcome to the game")
    game=["snake","water","gun"]
    while True:
        print("Enter the option(snake,water,gun)and quit for exit:")
        user=input(":")

        if(user=="quit"):
            print("bye")
            break
        elif user not in game:
            print("invalide choice ,, enter again")
            continue

        else:
            computer=random.choice(game)
            if (computer==user):
                print("match is draw")
            elif((user=="snake" and computer=="water") or (user=="water" and computer=="gun")  or (user=="gun" and computer=="snake") ):
                print("user wins")
            else:
                print("user lost")
game()

