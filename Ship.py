'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/13/2024
Purpose: Class for the ships
'''

class Ships:
    def __init__(self,length):          # creates the objects for the ships with the length
        self.hits = 0                   # hits will be set to 0 for the number of ships has been hit
        self.length = length            # creates the length of the size of ship
        self.sunk = False               # sets the sunk to false to check 
        self.locations = []             # empty list for location
    
    def hit(self):                   # hit function if the user hits the ship
        """Each ship has an internal hit counter. This increments that counter. Once the hit count is the same as the length of the ship, the sunk variable within the ship object is set."""
        self.hits += 1                  # hits counter
        if self.hits == self.length:    # if the hits number is the same as the length of the ship
            self.sunk = True            # ship will be sunk
    
    def updatelocation(self, row, col): # function updates the location of the ships with the row and column
        """Ship locations are stored as an array of points. Each point is a list containing a row and a column. updatelocation() is called when the ship is being placed. Each "location" the ship is over must be added by calling this function."""
        list = [row, col]               # list variable to put the row and column in a list
        self.locations.append(list)     # it will then add the list to the the location's empty list
