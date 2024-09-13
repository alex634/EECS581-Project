Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose: 
'''
class Ships:
    def __init__(self,length): #creates the objects for the ships with the length
        self.hits = 0 #hits will be set to 0 for the number of ships has been hit
        self.length = length #creates the length of the size of ship
        self.sunk = False #sets the sunk to false to check 
        self.locations = [] #empty list for location
    def hit(self): #hit function if the user hits the ship
        self.hits += 1 #hits counter
        if self.hits == self.length: #if the hits number is the same as the length of the ship
            self.sunk = True #ship will be sunk
    def updatelocation(self, row, col): #function to update the location of the ships with the row and column
        list = [row, col] #list variable to put the row and column in a list
        self.locations.append(list) #it will then add the list to the the location's empty list

