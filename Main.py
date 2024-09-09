'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose: 
'''
from Player import Player
from Map import Map

def main():
    p1 = Player()                                       # both players are created
    p2 = Player()

    numShips = 0
    while True:                                         # loop asks how many ships there will be in play
        i = input("Enter number of ships for game: ")
        if i.isdigit() == True:
            i = int(i)
            if i >= 1 and i <= 5:
                numShips = i
                break
    
    placeShips(p1, numShips)                            # both players will place their ships
    placeShips(p2, numShips)

    return 0

def placeShips(player, numShips):
    
    return 0


def turn():
    return 0

def clear():
    return 0


main()
