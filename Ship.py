'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/09/2024
Purpose: 
'''
class Ships:
    def __init__(self,length):
        self.hits = 0
        self.length = length
        self.sunk = False
        self.locations = []
    def hit(self):
        self.hits += 1
        if self.hits == self.length:
            self.sunk = True
