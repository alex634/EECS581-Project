import random
import time

def build_game_plate():
    game_plate = []
    for _ in range(10):
        temp = []
        for _ in range(10):
            temp.append(0)
        game_plate.append(temp)
    return game_plate

def print_game_plate(game_plate):
    print("   A  B  C  D  E  F  G  H  I  J")
    for i in range(10):
        print(i, end=" ")
        print(game_plate[i])

def add_point(game_plate, value, coord):
    x = ord(coord[0]) - 65
    y = int(coord[1])

    try:
        if game_plate[y][x] == 0:
            game_plate[y][x] = value
        else:
            raise Exception()
    except:
        raise Exception()

    return game_plate

def add_ship_1(game_plate, coord, rotate = 0):
    return add_point(game_plate, 1, coord)

def add_ship_2(game_plate, coord, rotate = 0):
    x = ord(coord[0])
    y = int(coord[1])


    if rotate:
        coord1 = chr(x) + str(y + 1)
    else:
        coord1 = chr(x + 1) + str(y)

    game_plate = add_point(game_plate, 2, coord)
    game_plate = add_point(game_plate, 2, coord1)
    return game_plate

def add_ship_3(game_plate, coord, rotate = 0):
    x = ord(coord[0])
    y = int(coord[1])

    if rotate:
        coord1 = chr(x) + str(y + 1)
        coord2 = chr(x) + str(y + 2)
    else:
        coord1 = chr(x + 1) + str(y)
        coord2 = chr(x + 2) + str(y)

    game_plate = add_point(game_plate, 3, coord)
    game_plate = add_point(game_plate, 3, coord1)
    game_plate = add_point(game_plate, 3, coord2)
    return game_plate

def add_ship_4(game_plate, coord, rotate = 0):
    x = ord(coord[0])
    y = int(coord[1])

    if rotate:
        coord1 = chr(x) + str(y + 1)
        coord2 = chr(x) + str(y + 2)
        coord3 = chr(x) + str(y + 3)
    else:
        coord1 = chr(x + 1) + str(y)
        coord2 = chr(x + 2) + str(y)
        coord3 = chr(x + 3) + str(y)

    game_plate = add_point(game_plate, 4, coord)
    game_plate = add_point(game_plate, 4, coord1)
    game_plate = add_point(game_plate, 4, coord2)
    game_plate = add_point(game_plate, 4, coord3)
    return game_plate

def add_ship_5(game_plate, coord, rotate = 0):
    x = ord(coord[0])
    y = int(coord[1])


    if rotate:
        coord1 = chr(x) + str(y + 1)
        coord2 = chr(x) + str(y + 2)
        coord3 = chr(x) + str(y + 3)
        coord4 = chr(x) + str(y + 4)
    else:
        coord1 = chr(x + 1) + str(y)
        coord2 = chr(x + 2) + str(y)
        coord3 = chr(x + 3) + str(y)
        coord4 = chr(x + 4) + str(y)

    game_plate = add_point(game_plate, 5, coord)
    game_plate = add_point(game_plate, 5, coord1)
    game_plate = add_point(game_plate, 5, coord2)
    game_plate = add_point(game_plate, 5, coord3)
    game_plate = add_point(game_plate, 5, coord4)
    return game_plate


def gen_move():
    return "ABCDEFGHIJ"[random.randint(0, 9)] + str(random.randint(0, 9))

def gen_ship(game_plate, ship):

    ship_coord = []
    while ship > 0:
        rotate = random.randint(0, 1)
        coord = gen_move()

        try:
            if ship == 1:
                game_plate = add_ship_1(game_plate, coord, rotate)
            elif ship == 2:
                game_plate = add_ship_2(game_plate, coord, rotate)
            elif ship == 3:
                game_plate = add_ship_3(game_plate, coord, rotate)
            elif ship == 4:
                game_plate = add_ship_4(game_plate, coord, rotate)
            elif ship == 5:
                game_plate = add_ship_5(game_plate, coord, rotate)
            ship_coord.append((coord[0], coord[1], rotate))
            ship = ship - 1
        except:
            raise Exception()

    return game_plate, ship_coord

def give_ship(ship):

    is_bad = True
    while is_bad:
        try:
            plate = build_game_plate()
            game_plate, ship_coord = gen_ship(plate, ship)
            is_bad = False
        except:
            #time.sleep(0.1)
            is_bad = True

    return game_plate, ship_coord

game_plate, ship_coord = give_ship(4)
print_game_plate(game_plate)
print(ship_coord)
