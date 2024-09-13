
'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose: 
'''
from Map import Map
class Player:
    def __init__(self):
        self.playerMap = Map()
        self.opponentMap = Map()
        self.fleetNum = 0
        self.opponentSunk = 0
        
    def displayMaps(self):
        #display both boards
        print('Your Board')
        self.playerMap.display()
        print('Opponents Board')
        self.opponentMap.display()
    def displayEmpty(self):
        self.playerMap.display()

    def addToFleet(self,length,row, col,direction):
        isValid = self.playerMap.placeShip(length,row,col,direction)
        self.fleetNum += 1
        self.opponentSunk += 1
        self.playerMap.display()
        return isValid

    def updateOpponent(self,row,col,opponent):
        #Update the map 
        result = self.opponentMap.updateOpponentMap(row,col,opponent)
        #self.opponentMap.display()
        if result == 2:
            self.opponentSunk -= 1
        return result
    
    def updatePlayer(self,row,col,opponent):
        #Update the map
        self.playerMap.updatePlayerMap(row,col,opponent)
    
