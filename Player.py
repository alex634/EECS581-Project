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
    def displayMaps(self):
        #display both boards
        self.playerMap.display()
        self.opponentMap.display()
    def addShip(self,length,direction,start):
        self.playerMap.add_ship(length,direction,start)
        self.playerMap.display()
    def updateOpponent(self,row,col):
        #Update the map 
        self.opponentMap.updateOpponentMap(row,col)
        self.opponentMap.display()
    def updatePlayer(self,row,col):
        #Update the map
        self.playerMap.updatePlayerMap(row,col)
