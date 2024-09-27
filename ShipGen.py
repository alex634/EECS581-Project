import random

def int_to_coord(value):
    col = "ABCDEFGHIJ"[value % 10]
    row = int(value/10)

    return row, col

def place_ships(placed_ships, value, ship_size, rotate):
    
    if rotate:
        # row
        for i in range(ship_size):
            placed_ships.append(value + (i * 10))
    else:
        # column
        for i in range(ship_size):
            placed_ships.append(value + i)

def gen_ship(num_ship):
    ship_coord = []
    placed_ships = []
    while num_ship > 0:
        valid_ship = True
        while valid_ship:
            temp_placed_ships = []
            # ship are asuumed to generate downwards
            ship_index = random.randint(0, (100 - ( 10 * (num_ship - 1))) - 1)
            rotate = random.randint(0, 1)
            place_ships(temp_placed_ships, ship_index, num_ship, rotate)
            if not bool(set(temp_placed_ships) & set(placed_ships)):
                placed_ships += temp_placed_ships
                valid_ship = False

        row, col = int_to_coord(ship_index)

        ship_coord.append((col, row, rotate))
        num_ship -= 1
    return ship_coord

if __name__ == "__main__":
    ship_coord = gen_ship(5)
    print(ship_coord)
