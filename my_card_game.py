# Rename this file to the name of your game and delete this comment
# Names: Jon, Corey, Lucas, Matheos, Rhonn
# Date: 7/27

# Import statements
from card import Card

import sys
import time
from time import sleep
for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
    sys.stdout.flush()
    sleep(0.01)

# Program your game here!
class Player()
    def __init__(name):
        name = name
    def play_card():
        # place the code hear

# After that gets created make indivisual Players

player1 = Player.name("Corey")
# Rename this function to the name of your game and delete this comment
def my_card_game():
    deck = Card.new_deck()
    # print(deck)

# Code that runs when script is called from terminal
# ex: python my_card_game.py
if __name__ == "__main__":
    my_card_game()

import time

# bar = [
#     " [=     ]",
#     " [ =    ]",
#     " [  =   ]",
#     " [   =  ]",
#     " [    = ]",
#     " [     =]",
#     " [    = ]",
#     " [   =  ]",
#     " [  =   ]",
#     " [ =    ]",
# ]
# i = 0

# while True:
#     print(bar[i % len(bar)], end="\r")
#     time.sleep(.2)
#     i += 1