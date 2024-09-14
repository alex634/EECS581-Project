'''
Authors: Alexandra, Sophia, Eli, Jose, and Riley
Date: 09/08/2024
Last modified: 09/14/2024
Purpose: Class for a map
'''
from Ship import Ships  #imports the ships file
from tabulate import tabulate

class Map:              #map class
    def __init__(self):
        self.map = [[" " for i in range(10)] for j in range(10)]
        self.ships = [] #empty list for the ships
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #rows list with the given number position from 1-10
        self.col = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] #columns list with the given letter position from A-J


    def placeShip(self, length, row, col, direction): #function to place the ships
        direction = direction.lower()  #makes the direction name into lowercase when they put in left, right, up or down
        if direction not in ['left', 'right', 'up', 'down']: #if the user doesn't put any of these directions
            return False #returns it to false

        if row < 0 or row >= len(self.map) or col < 0 or col >= len(self.map[0]): #if the row and column is less than 0 or greater
            return False
        if direction == 'right': #if the user puts in the direction of right
            end = col + length
            if end > len(self.map[0]):
                return False
            section = [self.map[row][ncol] for ncol in range(col, end)]

        elif direction == 'left':
            end = col - length
            if end < -1:
                return False
            section = [self.map[row][ncol] for ncol in range(end + 1, col + 1)]

        elif direction == 'down':
            end = row + length
            if end > len(self.map):
                return False
            section = [self.map[nrow][col] for nrow in range(row, end)]

        elif direction == 'up':
            end = row - length
            if end < -1:
                return False
            section = [self.map[nrow][col] for nrow in range(end + 1, row + 1)]

        possible = all(element == " " for element in section)
        if possible:
            ship = Ships(length)
            if direction == 'right':
                for new_col in range(col, end):
                    ship.updatelocation(row, new_col)
                    self.map[row][new_col] = length


            elif direction == 'left':
                for new_col in range(end + 1, col + 1):
                    ship.updatelocation(row, new_col)
                    self.map[row][new_col] = length

            elif direction == 'down':
                for new_row in range(row, end):
                    ship.updatelocation(new_row, col)
                    self.map[new_row][col] = length

            elif direction == 'up':
                for new_row in range(end + 1, row + 1):
                    ship.updatelocation(new_row, col)
                    self.map[new_row][col] = length
            self.ships.append(ship)

            return True

        return False

    def updatePlayerMap(self,row,col, opponent):
        if self.map[row][col] == "X" or self.map[row][col] == 'O':
            return 0
        if isinstance(self.map[row][col], int):
            self.map[row][col] = 'X'
            for ship in self.ships:
                if [row, col] in ship.locations:
                    ship.hit()
        else:
            self.map[row][col] = 'O'
        return 1

    def updateOpponentMap(self, row, col, opponent):
        if self.map[row][col] == "X" or self.map[row][col] == 'O' or self.map[row][col] == 1 or self.map[row][col] == 2 or self.map[row][col] == 3 or self.map[row][col] == 4 or self.map[row][col] == 5:
            return 0
        if opponent.playerMap.map[row][col] == "X":
            self.map[row][col] = "X"
            print("><><><>< SHIP HAS BEEN HIT!!! ><><><><")

            for ship in opponent.playerMap.ships:
                if [row, col] in ship.locations:
                    if ship.sunk:
                        print("YOU HAVE SUNK A SHIP!")
                        for [srow, scol] in ship.locations:
                            self.map[srow][scol] = ship.length
                        return 2
            return 1
        else:
            self.map[row][col] = 'O'
            print("SHOT HAS MISSED!!! :(")
            return 1


    def display(self):
        header = [""] + self.col
        table_data = []
        for i, row in enumerate(self.map):
            table_data.append([self.rows[i]] + row)
        table = tabulate(table_data, headers=header, tablefmt="grid")
        print(table)
