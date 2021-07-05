import pygame
import random


# Get the map
# path to file from main.py
def get_map(filepath):
    f = open(filepath, "r")
    map = []
    for x in f:
        map.append(x)
    f.close()
    return map


# load all maps into array
def load_maps():
    maps = []
    maps.append(get_map("Assets/maps/level1.txt"))
    maps.append(get_map("Assets/maps/level2.txt"))
    maps.append(get_map("Assets/maps/level3.txt"))
    return maps


# shows the loaded map in terminal
def print_map_debbug(map):
    for x in map:
        print(x, end='')


# count = level
def tiles(maps, sprites, screen, count, powerups, pressure_plates, collected_key):
    pos_x = 0
    pos_y = 0
    for y in maps[count]:
        for x in y:
            if x == "X":
                screen.blit(sprites[0], (pos_x, pos_y))
            if x == "Y":
                screen.blit(sprites[2], (pos_x, pos_y))
            if x == "y":
                screen.blit(sprites[1], (pos_x, pos_y))
            if x == "I":
                screen.blit(sprites[3], (pos_x, pos_y))
            if x == "Z":
                screen.blit(sprites[14], (pos_x, pos_y))
            if x == "A":
                screen.blit(sprites[6], (pos_x, pos_y))
            if x == "B":
                screen.blit(sprites[7], (pos_x, pos_y))
            if x == "C":
                screen.blit(sprites[8], (pos_x, pos_y))
            if x == "D":
                screen.blit(sprites[9], (pos_x, pos_y))
            if x == "T":
                screen.blit(sprites[10], (pos_x, pos_y))
            if x == "W":
                screen.blit(sprites[11], (pos_x, pos_y))
            if x == "R":
                screen.blit(sprites[12], (pos_x, pos_y))
            if x == "L":
                screen.blit(sprites[13], (pos_x, pos_y))
            if x == " ":
                screen.blit(sprites[14], (pos_x, pos_y))
            if x == "P":
                if not collected_key:
                    screen.blit(sprites[29], (pos_x, pos_y))
                else:
                    screen.blit(sprites[28], (pos_x, pos_y))
            if x == "p":
                screen.blit(sprites[15], (pos_x, pos_y))
            if x == "t":
                screen.blit(sprites[18], (pos_x, pos_y))
            if x == "c":
                screen.blit(sprites[23], (pos_x, pos_y))
            if x == "r":
                screen.blit(sprites[19], (pos_x, pos_y))
            if x == "l":
                screen.blit(sprites[17], (pos_x, pos_y))
            if x == "O":
                screen.blit(sprites[24], (pos_x, pos_y))
            if x == "o":
                screen.blit(sprites[24], (pos_x, pos_y))
            if x == "n":
                for elem in pressure_plates:
                    if elem[1] == 0:
                        if (elem[0].x == pos_x and elem[0].y == pos_y):
                            screen.blit(sprites[26], (pos_x, pos_y))
                    elif elem[1] == 1:
                        if (elem[0].x == pos_x and elem[0].y == pos_y):
                            screen.blit(sprites[27], (pos_x, pos_y))
            if x == "k":
                for elem in powerups:
                    if elem[1] == 1:
                        if (elem[0].x == pos_x and elem[0].y == pos_y):
                            screen.blit(sprites[14], (pos_x, pos_y))
                            screen.blit(sprites[25], (pos_x, pos_y))
                    elif elem[1] == 0:
                        if (elem[0].x == pos_x and elem[0].y == pos_y):
                            screen.blit(sprites[14], (pos_x, pos_y))
            pos_x += 32
            if x == "\n":
                pos_y += 32
                pos_x = 0


def check_map_way(maps, count):
    way_arr = []
    check = 0

    for y in maps[count]:
        for x in y:
            if x == " ":
                way_arr.append(check)
                check += 1
            if x == "o":
                way_arr.append(check)
                check += 1
            if x == "O":
                way_arr.append(check)
                check += 1
            if x == "P":
                way_arr.append(check)
                check += 1
            if x == "p":
                way_arr.append(check)
                check += 1
            if x == "n":
                way_arr.append(check)
                check += 1

    return way_arr


def load_shade_way(maps, surface, screen, count, check_map, image, collect):
    pos_x = 0
    pos_y = 0
    check = 0

    for y in maps[count]:
        for x in y:
            if x == " ":
                if (check == check_map[check][1]):
                    screen.blit(image, (pos_x, pos_y))
                check += 1
            if x == "o":
                if (check == check_map[check][1]):
                    screen.blit(image, (pos_x, pos_y))
                check += 1
            if x == "O":
                if (check == check_map[check][1]):
                    screen.blit(image, (pos_x, pos_y))
                check += 1
            if x == "P":
                if (check == check_map[check][1]):
                    screen.blit(image, (pos_x, pos_y))
                check += 1
            if x == "p":
                if (check == check_map[check][1]):
                    screen.blit(image, (pos_x, pos_y))
                check += 1
            if x == "k":
                if (check == check_map[check][1]):
                    screen.blit(image, (pos_x, pos_y))
                check += 1
            if x == "n":
                if (check == check_map[check][1]):
                    screen.blit(image, (pos_x, pos_y))
                check += 1
            pos_x += 32
            if x == "\n":
                pos_y += 32
                pos_x = 0


def create_hit_box_shade(maps, levlnbr, collect):
    pos_x = 0.0
    pos_y = 0.0
    wall_list = []
    check = 0
    rand_key_sum = []
    sum_spaces = 0
    number_space = 0

    for y in maps[levlnbr]:
        for x in y:
            if x == " ":
                sum_spaces += 1

    while len(rand_key_sum) != 3:
        no_pos = 0
        temp = random.randint(1, sum_spaces)
        for i in rand_key_sum:
            if i == temp:
                no_pos = 1
        if no_pos == 0:
            rand_key_sum.append(temp)


    for y in maps[levlnbr]:
        for x in y:
            if x == " ":
                if number_space in rand_key_sum:
                    wall_list.append([pygame.Rect((pos_x, pos_y, 32.0, 32.0)), check, 1])
                    collect.append("0")
                else:
                    wall_list.append([pygame.Rect((pos_x, pos_y, 32.0, 32.0)), check, 0])
                check += 1
                number_space += 1
            if x == "o":
                wall_list.append([pygame.Rect((pos_x, pos_y, 32.0, 32.0)), check, 0])
                check += 1
            if x == "O":
                wall_list.append([pygame.Rect((pos_x, pos_y, 32.0, 32.0)), check, 0])
                check += 1
            if x == "P":
                wall_list.append([pygame.Rect((pos_x, pos_y, 32.0, 32.0)), check, 0])
                check += 1
            if x == "p":
                wall_list.append([pygame.Rect((pos_x, pos_y, 32.0, 32.0)), check, 0])
                check += 1
            if x == "k":
                wall_list.append([pygame.Rect((pos_x, pos_y, 32.0, 32.0)), check, 0])
                check += 1
            if x == "n":
                wall_list.append([pygame.Rect((pos_x, pos_y, 32.0, 32.0)), check, 0])
                check += 1
            pos_x += 32
            if x == "\n":
                pos_x = 0
                pos_y += 32
    return wall_list


# load the sprites to build the map:
# sprites[0] == Cornerleftdown
# sprites[1] == cornerleftup
# sprites[2] == cornerrightup
# sprites[3] == cornerrightdown
# sprites[4] == way.jpg
# sprites[5] == testlock
# sprite[6] == stone1
#       [9]--> stone4
# sprite [10] = topsideboarder
# sprite [11] = botsideboarder
# sprite [12] = rightsideboarder
# sprite [13] = leftsideboarder
# sprite [14] = way
# sprite [15] = portal
# sprite [16] = portalboarderdown
# sprite [17] = portalborderleft
# sprite [18] = portalbordertop
# sprite [19] = portalborderright
# sprite [20] = portalleftdown
# sprite [21] = portalleftup
# sprite [22] = portalrightdown
# sprite [23] = portalrightup
# sprite [24] = teleporter
# sprite [25] = power_up
# sprite [26] = plate off
# sprite [27] = plate on
# sprite [28] = portal_close
# sprite [29] = portal_open
def load_sprites_for_map():
    sprites = []
    sprites.append(pygame.image.load("Assets/map_sprites/cornerleftdown.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/cornerleftup.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/cornerrightup.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/cornerrightdown.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/way.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/testblock.png"))
    sprites.append(pygame.image.load("Assets/map_sprites/stone1.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/stone2.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/stone3.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/stone4.jpg"))
    sprites.append(pygame.image.load(("Assets/map_sprites/topsideborder.jpg")))
    sprites.append(pygame.image.load(("Assets/map_sprites/botsideborder.jpg")))
    sprites.append(pygame.image.load(("Assets/map_sprites/rightsideborder.jpg")))
    sprites.append(pygame.image.load(("Assets/map_sprites/leftsideborder.jpg")))
    sprites.append(pygame.image.load("Assets/map_sprites/way.png"))
    sprites.append(pygame.image.load("Assets/map_sprites/portal.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/portalborderdown.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/portalborderleft.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/portalbordertop.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/portalborderright.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/portalleftdown.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/portalleftup.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/portalrightdown.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/portalrightup.jpg"))
    sprites.append(pygame.image.load("Assets/map_sprites/teleporter2.png"))
    sprites.append((pygame.image.load("Assets/character_sprites/Boosters/speed_up.png")))
    sprites.append(pygame.image.load("Assets/map_sprites/pressure_plate_off.png"))
    sprites.append(pygame.image.load("Assets/map_sprites/pressure_plate_on.png"))
    sprites.append(pygame.image.load("Assets/map_sprites/portal_close.png"))
    sprites.append(pygame.image.load("Assets/map_sprites/portal_open.png"))
    return sprites


# Create the wall_rect and store it into array
def create_map_hitbox(maps, levelnbr):
    pos_x = 0.0
    pos_y = 0.0
    wall_list = []
    for y in maps[levelnbr]:
        for x in y:
            if x == "X":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "Y":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "L":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "I":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "A":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "B":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "C":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "D":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "W":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "T":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "R":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "L":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            if x == "y":
                wall_list.append(pygame.Rect((pos_x, pos_y, 32.0, 32.0)))
            pos_x += 32.0
            if x == "\n":
                pos_y += 32.0
                pos_x = 0.0
    return wall_list


def create_teleport_recs(maps, level_nbr):
    teleporter = []
    pos_x = 0.0
    pos_y = 0.0
    for y in maps[level_nbr]:
        for x in y:
            if x == "O":
                teleporter.append([pygame.Rect(pos_x, pos_y, 32.0, 32.0), 'O', 0])
            if x == "o":
                teleporter.append([pygame.Rect(pos_x, pos_y, 32.0, 32.0), 'o', 0])
            pos_x += 32.0
            if x == "\n":
                pos_y += 32.0
                pos_x = 0
    if not teleporter:
        teleporter.append(0)
    return teleporter


def create_escape_rects(maps, level_nbr):
    portalzone = []
    pos_x = 0.0
    pos_y = 0.0
    for y in maps[level_nbr]:
        for x in y:
            if x == "P":
                portalzone.append(pygame.Rect(pos_x, pos_y, 32.0, 32.0))
            pos_x += 32.0
            if x == "\n":
                pos_y += 32.0
                pos_x = 0
    return portalzone

def create_pressure_plate(maps, level_nbr):
    pressure_plates = []
    pos_x = 0.0
    pos_y = 0.0
    for y in maps[level_nbr]:
        for x in y:
            if x == "n":
                pressure_plates.append([pygame.Rect(pos_x, pos_y, 32.0, 32.0), 0])
            pos_x += 32.0
            if x == "\n":
                pos_y += 32.0
                pos_x = 0
    if not pressure_plates:
        pressure_plates.append(0)
    return pressure_plates


def load_powerups(maps, level_nbr):
    power_ups = []
    pos_x = 0.0
    pos_y = 0.0
    for y in maps[level_nbr]:
        for x in y:
            if x == "k":
                power_ups.append([pygame.Rect(pos_x, pos_y, 32.0, 32.0), 1])
            pos_x += 32.0
            if x == "\n":
                pos_y += 32.0
                pos_x = 0
    if not power_ups:
        power_ups.append(0)
    return power_ups
