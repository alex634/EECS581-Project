'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose: 
'''
from Player import Player
from Map import Map

def main():
    # both players are created
    p1 = Player()                                       
    p2 = Player()

    # loop asks how many ships there will be in play
    numShips = 0
    while True:                                         
        i = input("Enter number of ships for game: ")
        if i.isdigit() == True:
            i = int(i)
            if i >= 1 and i <= 5:
                numShips = i
                break
    
    # both players will take turns to place their ships
    placeShipTurn(p1, numShips)                            
    placeShipTurn(p2, numShips)

    turn(p1,p2)


def placeShipTurn(player, numShips): 
    length = numShips
    while numShips >= 0:
        start = input("Enter starting position (EX: B2): ")
        direction = input("Enter a direction to place your ship (left, right, up, down): ")
        player.addToFleet(length, direction, start)
        length -= 1



def turn(player1, player2):

    clear()
    return 0

def clear():
    return 0


main()
