'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose: 
'''
from Ship import Ships
class Map:
    def __init__(self):
        #self.map = list of list
        self.ships = []
    def add_ship(self,length,start,direction):
        ship = Ships(length)
        #Check if space is free
    def updatePlayerMap(self,row,col):
        #If hit replace S with X
        #If miss add O
        pass
    def updateOpponentMap(self,row,col):
        #If hit add X
        #If miss add O
        #If sunk replace all with S
        pass
    def display(self):
        #displays the map
        pass
