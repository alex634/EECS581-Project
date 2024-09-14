'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/14/2024
Purpose: 
'''
from Map import Map
class Player:
    def __init__(self):                      #creates a class for the player and opponent board
        self.playerMap = Map()                              #player map
        self.opponentMap = Map()                            #opponent map
        self.fleetNum = 0                                   #fleet number set to 0 for the counter
        self.opponentSunk = 0                               #opponent sunk set to 0 for counter
    
    def displayMaps(self):                                  #function to display the boards for the player and opponent board
        print("Your Board")                                 #prints your board on the screen
        self.playerMap.display()                            #display of the player map
        print("Opponents Board")                            #prints opponents board on the screen
        self.opponentMap.display()                          #display of the opponent map
    
    def displayEmpty(self):                                 #function to display the empty map once it's the player's turn 
        self.playerMap.display()                            #display player's map  
   
    def addToFleet(self,length,row,col, direction):          #function to add the ships to the fleet 
        self.playerMap.placeShip(length,row,col,direction)  #places the ships to the player map with the length of ship, row, column and direction
        self.opponentSunk += 1                              #counter for when the opponent's ship is sunk
        self.fleetNum += 1                                  #counts the fleet after adding the ship
        self.playerMap.display()                            #displays the player map of ship after adding to the fleet

    def updateOpponent(self,row,col,opponent):                       #updates the map of the opponent
        result = self.opponentMap.updateOpponentMap(row,col,opponent)#result variable that will update the opponent's row and column
        #self.opponentMap.display()                         #this will then display the map after updating the opponent's row and column
        if result == 2:                                     #if the result is 2 
            self.opponentSunk -= 1                          #decreases the opponent's sunk counter
        return result                                       #returns the result of the updated map
    
    def updatePlayer(self,row,col,opponent):                         #function to update the player's board 
        self.playerMap.updatePlayerMap(row,col,opponent)             #calls the player's map and updates the row and column
    
