'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Editor: Harry, Timo, Isaac, and Hamza
Date: 09/08/2024
Last modified: 09/27/2024
Purpose: Main file
'''
import os                                                          #imports the os to interact with the os system
from Player import Player                                          #imports the player file
from Sound import Sound
import ShipGen
import time
import random

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
    coordinate_history = [] # Coordiinates that have been marked as hots stored for mediumAITurns to check.

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
            Sound.play_Error()
    
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
            Sound.play_Error()

    if ai == 0:
                                                                    # both players will take turns to place their ships                                                              
        print("\nPlayer 1, it's time to place your ships.")
        Sound.play_Turn()
        placeShipTurn(p1, numShips)                                     #places the ships in the placeShipTurn function for player 1
        clear()                                                         #clear terminal screen
        print("\nPlayer 2, it's time to place your ships.") 
        Sound.play_Turn()
        placeShipTurn(p2, numShips)                                     #places the ships in the placeShipTurn function for player 1
        clear()                                                         #clear terminal green
    else:
        print("\nPlayer 1, it's time to place your ships.")
        Sound.play_Turn()
        placeShipTurn(p1, numShips)
        clear(ai = 1)
        print("\nPlayer AI, is placing their ships...")
        Sound.play_Turn()
        placeAIShipTurn(p2, numShips)
        #clear()
        
    
    chosen = False                                                                # main game loop
    while p1.opponentSunk > 0 or p2.opponentSunk > 0:               #while player 1 and 2 have ships
        if ai == 0: # Human vs. Human
            # Player 1 turn
            print("Player 1's Turn") 
            Sound.play_Turn()
            turn(p1,p2)                                                 #calls the turn function for player 1
            # if statements that check if either player has won
            if p1.opponentSunk == 0:                                    #if player 1's opponent has zero ships
                print("Player 1 Wins!!!")
                Sound.play_Win()
                exit()                                                  #exits the game
            clear()                                                     #clears the terminal
            
            # Player 2 turn
            print("Player 2's Turn")
            Sound.play_Turn()
            turn(p2,p1)
            if p2.opponentSunk == 0:                                    #if player 2's opponent has zero ships
                print("Player 2 Wins!!!")
                Sound.play_Win()
                exit()                                                  #exits the game
            clear()                                                     #clears the terminal
        else: # AI vs. Human
            while (chosen == False):
                mode = input("Which dificultyl level? [E (easy), M (Medium, or H (Hard)]: ")
                if mode == "E" or mode == "e":  # Player one chooses easy.
                    mode = 0
                    print("Game mode set to Easy")
                    chosen = True
                    break
                elif mode == "M" or mode == "m": # Player one chooses meduim.
                    mode = 1
                    print("Game mode set to Medium")
                    chosen = True
                    break
                elif mode == "H" or mode == "h": # Player one chooses hard.
                    mode = 2
                    print("Game mode set to Hard") 
                    chosen = True
                    break
                else: # Player one chooses bad input.
                    print("Invalid Input")
                    Sound.play_Error()

            # Player 1 Turn
            print("Player 1's Turn") 
            Sound.play_Turn()
            turn(p1,p2)                                                 #calls the turn function for player 1                                                       # if statements that check if either player has won
            if p1.opponentSunk == 0:                                    #if player 1's opponent has zero ships
                print("Player 1 Wins!!!")
                Sound.play_Win()
                exit()                                                  #exits the game
            clear()   

            # AI (Easy) Turn
            if mode == 0:  # Easy mode
                print("AI (Easy) Turn")
                Sound.play_Turn()
                easyAITurn(p2, p1)  # AI fires randomly at Player 1
                if p2.opponentSunk == 0:  # Check if AI has won
                    print("AI Wins!!!")
                    Sound.play_Win()
                    exit()
                clear()
            
            if mode == 1:  # Medium mode
                print("AI (Medium) Turn")
                Sound.play_Turn()

                mediumAITurn(p2, p1, coordinate_history)  # AI fires with medium difficulty strategy
                if p2.opponentSunk == 0:  # Check if AI has won
                    print("AI Wins!!!")
                    Sound.play_Win()
                    exit()
                
                clear()

            # AI (Hard) Turn
            if mode == 2:  # Hard mode
                print("AI (Hard) Turn")
                Sound.play_Turn()
                hardAITurn(p2, p1)  # AI fires at Player 1's ships
                if p2.opponentSunk == 0:  # Check if AI has won
                    print("AI Wins!!!")
                    Sound.play_Win()
                    exit()
                clear()


def easyAITurn(player, opponent, coordinate_history=None):
    while True:
        row = random.randint(0, 9)  # Generate a random row between 0 and 9
        col = random.randint(0, 9)  # Generate a random column between 0 and 9

        opponent_res = opponent.updatePlayer(row, col, opponent)  # Fire at the opponent's board
        player_res = player.updateOpponent(row, col, opponent)    # Update AI's view of the opponent's board

        if player_res == 0 or opponent_res == 0:  # If already targeted, retry
            continue
        else:
            break  # Exit the loop when a valid shot is fired



def mediumAITurn(player, opponent, coordinate_history):
    # A set to track already fired coordinates, prevents firing on the same position again
    fired_coordinates = set()

    if coordinate_history:  # If there is already a history of coordinates to check
        row, col = coordinate_history[0]  # Get the first coordinate from the list

        while coordinate_history:  # Loop through until the history is empty or a valid shot is fired
            if (row, col) in fired_coordinates:  # Skip if already fired at this position
                coordinate_history.pop(0)
                if coordinate_history:
                    row, col = coordinate_history[0]  # Get the next coordinate
                else:
                    break
                continue

            opponent_res = opponent.updatePlayer(row, col, opponent)  # Fire at the opponent's board
            player_res = player.updateOpponent(row, col, opponent)    # Update AI's view of the opponent's board

            fired_coordinates.add((row, col))  # Track this coordinate as fired

            if player_res == 0 or opponent_res == 0:  # If the spot has already been targeted
                coordinate_history.pop(0)  # Remove the invalid coordinate
                if coordinate_history:
                    row, col = coordinate_history[0]  # Get the next coordinate
                else:
                    break
            else:
                if opponent_res == 3:  # Add surrounding coordinates if the hit is successful
                    potential_targets = [
                        (row - 1, col),  # Up
                        (row, col + 1),  # Right
                        (row + 1, col),  # Down
                        (row, col - 1)   # Left
                    ]

                    for target_row, target_col in potential_targets:
                        if 0 <= target_row < 10 and 0 <= target_col < 10 and (target_row, target_col) not in fired_coordinates:
                            coordinate_history.insert(0, (target_row, target_col))  # Add valid target coordinates to the list

                break  # Exit the loop when a valid shot is fired

    else:  # If no history, fire randomly
        while True:
            row = random.randint(0, 9)  # Randomly choose a row
            col = random.randint(0, 9)  # Randomly choose a column

            if (row, col) in fired_coordinates:  # If this coordinate has already been fired at, skip
                continue

            opponent_res = opponent.updatePlayer(row, col, opponent)  # Fire at the opponent's board
            player_res = player.updateOpponent(row, col, opponent)    # Update AI's view of the opponent's board

            fired_coordinates.add((row, col))  # Track this coordinate as fired

            if player_res == 0 or opponent_res == 0:  # If the shot was invalid (already hit or missed)
                continue
            else:
                if opponent_res == 3:  # If a ship is hit but not sunk
                    potential_targets = [
                        (row - 1, col),  # Up
                        (row, col + 1),  # Right
                        (row + 1, col),  # Down
                        (row, col - 1)   # Left
                    ]

                    for target_row, target_col in potential_targets:
                        if 0 <= target_row < 10 and 0 <= target_col < 10 and (target_row, target_col) not in fired_coordinates:
                            coordinate_history.insert(0, (target_row, target_col))  # Add valid target coordinates to the list

                break  # Exit the loop when a valid shot is fired


def hardAITurn(player, opponent):
    # Retrieve coordinates of opponent's ships
    ship_coordinates = opponent.playerMap.get_opponent_ship_coordinates()  # Get the coordinates from opponent's Map class
    
    # Find the first available ship part that hasn't been hit yet
    available_hits = [(row, col) for row, col in ship_coordinates if not opponent.playerMap.is_hit(row, col)]
    
    if available_hits:
        # Select the first available ship part to hit
        row, col = available_hits[0]
        
        opponent_res = opponent.updatePlayer(row, col, opponent)  # AI fires at the opponent's map
        player_res = player.updateOpponent(row, col, opponent)    # AI updates its view of the opponent's map

    else:
        print("No available hits found!")  # This shouldn't happen in hard mode

def placeAIShipTurn(player, numShips):
    ship_coord = ShipGen.gen_ship(numShips)  # Generate ship coordinates
    index = 0
    while numShips > 0:
        length = numShips  # Ship length
        col = ord(ship_coord[index][0]) - ord("A")
        row = int(ship_coord[index][1])

        # Boundary check
        if ship_coord[index][2] == 0 and col + length > 10:  # Right boundary
            continue  # Skip invalid placement
        if ship_coord[index][2] == 1 and row + length > 10:  # Down boundary
            continue  # Skip invalid placement

        direction = "right" if ship_coord[index][2] == 0 else "down"
        player.addToFleet(length, row, col, direction)  # Place the ship
        os.system('cls' if os.name == 'nt' else 'clear')
        index += 1
        numShips -= 1  # Move to the next ship


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
                    Sound.play_Error()
                else:
                    break                                           #exits if successful
            else:                                                   #if ship is greater than the 1x1 ship
                col = get_column()                                  #gets the column 
                row = get_row()                                     #gets the row 
                direction = get_direction()                         #gets the direction for where the place the ship
                added = player.addToFleet(length, row,col,direction)        #adds ship to fleet
                if added == False:                                  #if it was not successful
                    print("Please input a valid space! Remember you can't place on top of other ships or off the map")
                    Sound.play_Error()
                else:
                    break
        length -= 1                                                 #decreases the length of ship for the next ship

# function that gets the column coordinate
def get_column():
    while True: 
        col = input("Enter starting column (EX: B): ").upper()      #user enters column and makes it uppercase
        if col == "": #if the inout is empty
            print("Invalid column. Please enter a letter between A and J.") #invalid message
            Sound.play_Error()
        elif col in "ABCDEFGHIJ":                                   #if the input is one of these letters
            return ord(col) - ord('A')                              #returns it to an index from 0-9
        else:                                                       #if they put a different letter other than from A-J
            print("Invalid column. Please enter a letter between A and J.") 
            Sound.play_Error()

# function that gets the row coordinates
def get_row():
    while True:
        row = input("Enter starting row (EX: 1): ")                 #user enters row number
        if row.isdigit() and 1 <= int(row) <= 10:                   #if the row number is between 1 and 10
            return int(row) - 1                                     #makes the row to an index from 0-9
        else:                                                       #if they put a different number or not
            print("Invalid row. Please enter a number between 1 and 10.")
            Sound.play_Error()

# function that gets the direction for the ship
def get_direction():
    while True:
        direction = input("Enter a direction to place your ship (left, right, up, down): ").lower() #user enters direction and makes it lowercase
        if direction in ["left", "right", "up", "down"]:                                            #if the user enters any of these directions
            return direction                                                                        #returns the direction from what the user put in 
        else:                                                                                       #invalid message
            print("Invalid direction. Please enter 'left', 'right', 'up', or 'down'.")
            Sound.play_Error()
# function that handles a player's turn
def turn(player, opponent):
    while True:
        player.displayMaps()  # Display both player's and opponent's boards
        col = get_column()  # Get column input
        row = get_row()  # Get row input

        # Check if the spot has already been targeted
        if opponent.playerMap.map[row][col] in ['X', 'O']:
            print("You've already targeted this spot. Try again.")
            Sound.play_Error()
            continue  # Retry valid coordinate input

        opponent_res = opponent.updatePlayer(row, col, opponent)  # Update opponent's board
        player_res = player.updateOpponent(row, col, opponent)  # Update player's view of opponent's board
        if player_res == 0 or opponent_res == 0:  # Check if spot has already been targeted
            print("You've already targeted this spot. Try again.")
            Sound.play_Error()
        else:
            break  # Exit loop and continue the game




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
