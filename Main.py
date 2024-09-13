
'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose: 
'''
import os
from Player import Player


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
    clear()                           
    placeShipTurn(p2, numShips)
    clear()

    # main game loop
    while p1.opponentSunk > 0 or p2.opponentSunk > 0:
        turn(p1,p2)
        if p1.opponentSunk == 0:
            print("Player 1 Wins!!!")
            exit()
        clear()
        turn(p2,p1)
        if p2.opponentSunk == 0:
            print("Player 2 Wins!!!")
            exit()
        clear()
    

# function that handles placing ships on the board
def placeShipTurn(player, numShips):
    player.displayEmpty() 
    length = numShips
    while length > 0:
        print('Place a 1x' + str(length) + ' ship')
        if length == 1:
            col = get_column()
            row = get_row()
            direction = "up"
            player.addToFleet(length, row, col, direction)
        else:
            col = get_column()
            row = get_row()
            direction = get_direction()
            player.addToFleet(length, row,col,direction)
        length -= 1

# function gets the column coordinate
def get_column():
    while True:
        col = input("Enter starting column (EX: B): ").upper()
        if col in "ABCDEFGHIJ":  
            return ord(col) - ord('A')  
        else:
            print("Invalid column. Please enter a letter between A and J.")

# function gets the row coordinate
def get_row():
    while True:
        row = input("Enter starting row (EX: 1): ")
        if row.isdigit() and 1 <= int(row) <= 10:  
            return int(row) - 1  
        else:
            print("Invalid row. Please enter a number between 1 and 10.")

# function gets the direction where the ship will be placed
def get_direction():
    while True:
        direction = input("Enter a direction to place your ship (left, right, up, down): ").lower()
        if direction in ["left", "right", "up", "down"]: 
            return direction
        else:
            print("Invalid direction. Please enter 'left', 'right', 'up', or 'down'.")

# function that handles a player's turn
def turn(player, opponent):
    player.displayMaps()
    col = get_column()
    row = get_row()

    player.updateOpponent(row, col, opponent)
    player.updatePlayer(row, col, opponent)




# function that clears the terminal and prompt the next turn
def clear():
    input("Player hit ENTER key.")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Give computer to next player.")
    input("Next player hit ENTER key.")
    os.system('cls' if os.name == 'nt' else 'clear')


main()
