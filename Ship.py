'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 08/20/2024
Last modified: 08/26/2024
Purpose: 
'''
class Ships:
    def __init__(self,length):
        self.hits = 0
        self.length = length
        self.sunk = False
    def hit(self):
        self.hits += 1
        if self.hits == self.length:
            self.sunk = True
