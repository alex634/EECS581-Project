'''
Author: Harry W
Date: Sep 27, 2024
Last Modified: Sep 27, 2024
Purpose: this program assumes a 10x10 grid which we can use an index from 0 to 99 inclusive
from there based on the index the row and col can be calculated and checked for ship collisions
'''
import random


def int_to_coord(value):
    """The function converts an integer value to a string for the column int for row"""
    # the ones position is the column
    col = "ABCDEFGHIJ"[value % 10]
    # the tens position is the row
    row = int(value/10)
    return row, col

def place_ships(placed_ships, value, ship_size, rotate):
    "The function add a ship to a list and marks that location as taken so that there won't be two ship on top of each other."""
    # adds the ship as if it's vertical
    if rotate:
        # row
        for i in range(ship_size):
            # increment though the ship and appends the taken index to
            # given list
            placed_ships.append(value + (i * 10))
    # adds the ship as if it's horizontal
    else:
        # column
        for i in range(ship_size):
            # increment though the ship and appends the taken index to
            # given list
            placed_ships.append(value + i)

def gen_ship(num_ship):
    """The function generates ship locations and their rotations. It is passed in the amount of ships to generate. Returns a list of tuples in the form (col, row, rotate) for each ship."""
    # save the valid ship head coords and rotation as a tuple
    ship_coord = []
    placed_ships = [-1]
    while num_ship > 0:
        # check if the ship does not collide with one another
        valid_ship = True
        while valid_ship:
            temp_placed_ships = []
            # ship are assumed to generate downwards
            # but we can check if the rotations are valid
            # if the rotations are valid then add it to the list

            # generate a random rotation
            rotate = random.randint(0, 1)

            if rotate:
            # generate a ship from 0 to 99 but of the ship size is 5 it decrease
            # by 40 so that the tail of the ship does not hit the game boarder
                ship_index = random.randint(0, (100 - ( 10 * (num_ship - 1))) - 1)
            else:
                ship_index = random.randint(0, 99)
                if ship_index%10 in [9,8,7,6,5]:
                    ship_index = -1
            
            # adds the ship index to be marked at taken
            place_ships(temp_placed_ships, ship_index, num_ship, rotate)
            # check to see of the ship's index has been taken
            if not bool(set(temp_placed_ships) & set(placed_ships)):
                # if not been taken update the list of taken positions
                placed_ships += temp_placed_ships
                # stop the loop
                valid_ship = False

        # convert the ship index to coord
        row, col = int_to_coord(ship_index)

        # add the ship heads to the list
        ship_coord.append((col, row, rotate))
        # decrement the number of ships
        num_ship -= 1
    # returns a list of ship heads tuple
    return ship_coord

# debugging and make sure the ships does not collide
if __name__ == "__main__":
    ship_coord = gen_ship(5)
    print(ship_coord)
