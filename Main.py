'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/14/2024
Purpose: Main file
'''
import os
from Player import Player


def main():
    print("Welcome to the Battleship Game!")
    print("\nObjective: Sink all of your opponent's ships before they sink yours.")
    print("Each player will place their ships on their own board.")
    print("You will take turns to guess the location of your opponent's ships.")
    print("When a ship is hit, it will be marked on the board.")
    print("The first player to sink all of the opponent's ships wins!")
    print("\nLet's get started! Good luck and have fun!")

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
    print("\nPlayer 1, it's time to place your ships.")
    placeShipTurn(p1, numShips)
    clear()
    print("\nPlayer 2, it's time to place your ships.")
    placeShipTurn(p2, numShips)
    clear()

    # main game loop
    while p1.opponentSunk > 0 or p2.opponentSunk > 0:
        print("Player 1's Turn")
        turn(p1,p2)

        # if statements that check if either player has won
        if p1.opponentSunk == 0:
            print("Player 1 Wins!!!")
            exit()
        clear()
        print("Player 2's Turn")
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
        while True:
            print('Place a 1x' + str(length) + ' ship')
            if length == 1:
                col = get_column()
                row = get_row()
                direction = "up"
                added = player.addToFleet(length, row, col, direction)
                if added == False:
                    print("Please input a valid space! Remember you can't place on top of other ships or off the map")
                else:
                    break
            else:
                col = get_column()
                row = get_row()
                direction = get_direction()
                added = player.addToFleet(length, row,col,direction)
                if added == False:
                    print("Please input a valid space! Remember you can't place on top of other ships or off the map\n")
                else:
                    break
        length -= 1

# function that gets the column coordinate
def get_column():
    while True:
        col = input("Enter starting column (EX: B): ").upper()
        if col == "":
            print("Invalid column. Please enter a letter between A and J.")
        elif col in "ABCDEFGHIJ":
            return ord(col) - ord('A')
        else:
            print("Invalid column. Please enter a letter between A and J.")

# function that gets the row coordinates
def get_row():
    while True:
        row = input("Enter starting row (EX: 1): ")
        if row.isdigit() and 1 <= int(row) <= 10:
            return int(row) - 1
        else:
            print("Invalid row. Please enter a number between 1 and 10.")

# function that gets the direction for the ship
def get_direction():
    while True:
        direction = input("Enter a direction to place your ship (left, right, up, down): ").lower()
        if direction in ["left", "right", "up", "down"]:
            return direction
        else:
            print("Invalid direction. Please enter 'left', 'right', 'up', or 'down'.")
# function that handles a player's turn
def turn(player, opponent):
    while True:
        player.displayMaps()
        col = get_column()
        row = get_row()

        opponent_res = opponent.updatePlayer(row, col, opponent)
        player_res = player.updateOpponent(row, col, opponent)
        if opponent_res == 0:
            input("You've already targeted this spot. hit ENTER to try again.")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            break




# function that clears the terminal and prompt the next turn
def clear():
    input("Press ENTER to continue to the next player's turn.")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Give computer to next player.")
    input("Next player hit ENTER key.")

    os.system('cls' if os.name == 'nt' else 'clear')


main()
