'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose: 
'''
import os
from Player import Player
from Map import Map

def main():
    # both players are created
    p1 = Player()                                       
    p2 = Player()

    # loop asks how many ships there will be in play
    numShips = 0
    while True:                                         
        i = input("Enter number of ships (1-5) for game: ")
        if i.isdigit() == True:
            i = int(i)
            if i >= 1 and i <= 5:
                numShips = i
                break
        else:
            print("Invalid Input")
    
    # both players will take turns to place their ships
    placeShipTurn(p1, numShips)                            
    placeShipTurn(p2, numShips)

    # main game loop
    while p1.fleetNum > 0 or p2.fleetNum > 0:
        turn(p1,p2)
        clear()
        turn(p2,p1)
        clear()
    
    if p1.fleetNum == 0:
        print("Player 2 Wins!!!")
    elif p2.fleetNum == 0:
        print("Player 1 Wins!!!")

# function that handles placing ships on the board
def placeShipTurn(player, numShips): 
    length = numShips
    while numShips >= 0:
        start = input("Enter starting position (EX: B2): ")
        direction = input("Enter a direction to place your ship (left, right, up, down): ")
        player.addToFleet(length, direction, start)
        length -= 1

# function that handles a player's turn
def turn(player, opponent):
    player.displayMaps()
    coord = input("Enter coordinate for your attack (EX: J7): ")

    row = coord[0].upper()
    col = int(coord[1])


    player.updateOpponent(row, col, opponent)
    player.updatePlayer(row, col, opponent)




# function that clears the terminal and prompt the next turn
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Give computer to next player.")
    input("Next player hit ENTER key.")

    os.system('cls' if os.name == 'nt' else 'clear')






main()
