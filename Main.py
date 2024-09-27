'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/15/2024
Purpose: Main file
'''
import os                                                          #imports the os to interact with the os system
from Player import Player                                          #imports the player file
import ShipGen
import time

#printing a welcoming message before starting the game
def main():                                                             
    print("Welcome to the Battleship Game!")                                       
    print("\nObjective: Sink all of your opponent's ships before they sink yours.")
    print("Each player will place their ships on their own board.")
    print("You will take turns to guess the location of your opponent's ships.")
    print("When a ship is hit, it will be marked on the board.")
    print("The first player to sink all of the opponent's ships wins!")
    print("\nLet's get started! Good luck and have fun!")

    p1 = Player()                                                   #player 1 created
    p2 = Player()                                                   #player 2 created


    numShips = 0                                                    #number ships set to 0 
    while True:                                                     # loop asks how many ships there will be in play
        i = input("Enter number of ships (1-5) for game: ")
        if i.isdigit() == True:                                     #checks if the number is a digit
            i = int(i)                                              #converts it to an integer
            if i >= 1 and i <= 5:                                   #if the number is from 1-5
                numShips = i                                        #sets the number of ships from the input
                break                                               #ends the loop
        else:                                                       #if they don't put a number from 1-5 it's invalid
            print("Invalid Input")

    while True:
        ai = input("Play with AI? [Y/n]: ")
        if ai == "Y" or ai == "y":
            ai = 1
            break
        elif ai == "N" or ai == "n":
            ai = 0
            break
        else:
            print("Invalid Input")

    if ai == 0:
                                                                    # both players will take turns to place their ships                                                              
        print("\nPlayer 1, it's time to place your ships.")
        placeShipTurn(p1, numShips)                                     #places the ships in the placeShipTurn function for player 1
        clear()                                                         #clear terminal screen
        print("\nPlayer 2, it's time to place your ships.") 
        placeShipTurn(p2, numShips)                                     #places the ships in the placeShipTurn function for player 1
        clear()                                                         #clear terminal green
    else:
        print("\nPlayer 1, it's time to place your ships.")
        placeShipTurn(p1, numShips)
        clear(ai = 1)
        print("\nPlayer AI, is placing their ships...")
        placeAIShipTurn(p2, numShips)
        #clear()
        
    
                                                                    # main game loop
    while p1.opponentSunk > 0 or p2.opponentSunk > 0:               #while player 1 and 2 have ships
        print("Player 1's Turn") 
        turn(p1,p2)                                                 #calls the turn function for player 1
        
                                                                    # if statements that check if either player has won
        if p1.opponentSunk == 0:                                    #if player 1's opponent has zero ships
            print("Player 1 Wins!!!")
            exit()                                                  #exits the game
        clear()                                                     #clears the terminal
        print("Player 2's Turn")
        turn(p2,p1)
        if p2.opponentSunk == 0:                                    #if player 2's opponent has zero ships
            print("Player 2 Wins!!!")
            exit()                                                  #exits the game
        clear()                                                     #clears the terminal

def placeAIShipTurn(player, numShips):
    ship_coord = ShipGen.gen_ship(numShips)
    length = numShips
    index = 0
    while length > 0:
        col = ord(ship_coord[index][0]) - ord("A")
        row = int(ship_coord[index][1])

        if ship_coord[index][2] == 0:
            direction = "right"
        elif ship_coord[index][2] == 1:
            direction = "down"
        
        player.addToFleet(length, row, col, direction)
        os.system('cls' if os.name == 'nt' else 'clear')
        index += 1
        length -= 1


# function that handles placing ships on the board
def placeShipTurn(player, numShips): 
    player.displayEmpty()                                           #displays the empty board before placing ships
    length = numShips                                               #ship length
    while length > 0:                                               #while loop for the ship placement
        while True: 
            print('Place a 1x' + str(length) + ' ship')             #tells user to place ship
            if length == 1:                                         #if the ship is 1x1
                col = get_column()                                  #gets the column 
                row = get_row()                                     #gets the row 
                direction = "up"                                    #uses the up direction
                added =player.addToFleet(length, row, col, direction) #adds the ship to fleat
                if added == False:                                  #if it was not successful
                    print("Please input a valid space! Remember you can't place on top of other ships or off the map")
                else:
                    break                                           #exits if successful
            else:                                                   #if ship is greater than the 1x1 ship
                col = get_column()                                  #gets the column 
                row = get_row()                                     #gets the row 
                direction = get_direction()                         #gets the direction for where the place the ship
                added = player.addToFleet(length, row,col,direction)        #adds ship to fleet
                if added == False:                                  #if it was not successful
                    print("Please input a valid space! Remember you can't place on top of other ships or off the map")
                else:
                    break
        length -= 1                                                 #decreases the length of ship for the next ship

# function that gets the column coordinate
def get_column():
    while True: 
        col = input("Enter starting column (EX: B): ").upper()      #user enters column and makes it uppercase
        if col == "": #if the inout is empty
            print("Invalid column. Please enter a letter between A and J.") #invalid message
        elif col in "ABCDEFGHIJ":                                   #if the input is one of these letters
            return ord(col) - ord('A')                              #returns it to an index from 0-9
        else:                                                       #if they put a different letter other than from A-J
            print("Invalid column. Please enter a letter between A and J.") 

# function that gets the row coordinates
def get_row():
    while True:
        row = input("Enter starting row (EX: 1): ")                 #user enters row number
        if row.isdigit() and 1 <= int(row) <= 10:                   #if the row number is between 1 and 10
            return int(row) - 1                                     #makes the row to an index from 0-9
        else:                                                       #if they put a different number or not
            print("Invalid row. Please enter a number between 1 and 10.")

# function that gets the direction for the ship
def get_direction():
    while True:
        direction = input("Enter a direction to place your ship (left, right, up, down): ").lower() #user enters direction and makes it lowercase
        if direction in ["left", "right", "up", "down"]:                                            #if the user enters any of these directions
            return direction                                                                        #returns the direction from what the user put in 
        else:                                                                                       #invalid message
            print("Invalid direction. Please enter 'left', 'right', 'up', or 'down'.")
# function that handles a player's turn
def turn(player, opponent):
    while True:
        player.displayMaps()    #display player's map
        col = get_column()      #gets the column from the get_column function during the game
        row = get_row()         #gets the row from the get_row function during the game

        opponent_res = opponent.updatePlayer(row, col, opponent)    #updates the player from the game
        player_res = player.updateOpponent(row, col, opponent)      #updates the opponent from the game
        if player_res == 0 or opponent_res == 0:                    #checks if the spot has been targeted
            print("You've already targeted this spot. Try again.")
        else:
            break                                                   #breaks the loop 




# function that clears the terminal and prompt the next turn
def clear(ai = 0):
    input("Press ENTER to continue to the next player's turn.")     #tells the user to press enter
    os.system('cls' if os.name == 'nt' else 'clear')                #clear the screen

    if ai:
        print("The AI is placing their ships >:3")
        print("Thinking", end = "")
        print(".", end = "", flush=True)
        time.sleep(1)
        print(".", end = "", flush=True)
        time.sleep(1)
        print(".", flush=True)
        input("I'm ready, hit the ENTER key to play >:3")
    else:
        print("Give computer to next player.")                          #tells the user to hand over the screen to next player
        input("Next player hit ENTER key.")                             #tells the next user to start

    os.system('cls' if os.name == 'nt' else 'clear')                #clear the screen

#calls main 
main()             
