import pygame
from Assets.Code import map
from Assets.Code import respawn
from Assets.Code import pausemenu


# player load and animate function
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.current_sprite = 0
        self.sprites_alive = []
        self.sprites_death = []
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Player/player1.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Player/player2.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Player/player3.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Player/player4.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Player/player5.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Player/player6.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Player/player7.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Player/player8.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d1.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d2.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d3.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d4.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d5.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d6.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d7.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d8.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d9.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Player/player_d10.png"))
        self.image = self.sprites_alive[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.ani_pos = 0
        self.is_animated = False

    def animated(self, ind_anm):
        self.is_animated = True
        self.ani_pos = ind_anm

    def update(self, ani_pos):
        if self.is_animated == True:
            self.current_sprite = self.ani_pos
            self.image = self.sprites_alive[self.current_sprite]
            self.image = pygame.transform.scale(self.image, (20, 20))

# blob load and animate function
class Blob(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.current_sprite = 0
        self.sprites_alive = []
        self.sprites_death = []
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Blob/blob1.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Blob/blob2.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Blob/blob3.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Blob/blob4.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Blob/blob5.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Blob/blob6.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Blob/blob_d1.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Blob/blob_d2.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Blob/blob_d3.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Blob/blob_d4.png"))
        self.image = self.sprites_alive[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.ani_pos = 0
        self.is_animated = False

    def animated(self, ind_anm):
        self.is_animated = True
        self.ani_pos = ind_anm

    def update(self, ani_pos):
        if self.is_animated == True:
            self.current_sprite = self.ani_pos
            self.image = self.sprites_alive[self.current_sprite]

# ghost load and animate function
class Ghost(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.current_sprite = 0
        self.sprites_alive = []
        self.sprites_death = []
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost1.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost2.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost3.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost4.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost5.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost6.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost7.png"))
        self.sprites_alive.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost8.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost_d1.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost_d2.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost_d3.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost_d4.png"))
        self.sprites_death.append(pygame.image.load("./Assets/character_sprites/Ghost/ghost_d5.png"))
        self.image = self.sprites_alive[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.ani_pos = 0
        self.is_animated = False

    def animated(self, ind_anm):
        self.is_animated = True
        self.ani_pos = ind_anm

    def update(self, ani_pos):
        if self.is_animated == True:
            self.current_sprite = self.ani_pos
            self.image = self.sprites_alive[self.current_sprite]

def animated_player(player, pressed):
    key_pressed = []
    up_check = 0
    down_check = 0
    a_check = 0
    d_check = 0

    for i in pressed:
        if pressed[i] == True:
            if i == 97 or i == 1073741904:
                a_check = 1
            elif i == 119 or i == 1073741906:
                up_check = 1
            elif i == 115 or i == 1073741905:
                down_check = 1
            elif i == 100 or i == 1073741903:
                d_check = 1
            key_pressed.append(i)
    if len(key_pressed) == 2:
        if a_check == 1:
            if up_check == 1:
                player.animated(5)
            elif down_check == 1:
                player.animated(7)
        elif up_check == 1:
            if d_check == 1:
                player.animated(3)
        elif d_check == 1:
            if down_check == 1:
                player.animated(1)
    elif len(key_pressed) == 1:
        if a_check == 1:
            player.animated(6)
        elif up_check == 1:
            player.animated(4)
        elif d_check == 1:
            player.animated(2)
        elif down_check == 1:
            player.animated(0)

# Key Usage for the movement (dictionary)
# K_w = 119
# K_s = 115
# K_a = 97
# K_d = 100
# pos[0] = x-axis || pos[1] = y-axis
# dont get out of bonderies
# MOVEMENT WASD AND ARROWS

def movement(pos, pressed, wall_list, player_copy, pause, player, speed):
    check = 0
    if (pressed.get(97) or pressed.get(1073741904)) and pos[0] >= 0.0:
        pygame.Rect.move_ip(player_copy, -speed, 0)
        check = 0
        for elem in wall_list:
            if (pygame.Rect.colliderect(player_copy, elem) == True):
                check = 1
                break

        if (check == 0):
            pos[0] -= speed

    if (pressed.get(119) or pressed.get(1073741906)) and pos[1] >= 0.0:
        pygame.Rect.move_ip(player_copy, 0, (-1*speed))
        check = 0
        for elem in wall_list:
            if (pygame.Rect.colliderect(player_copy, elem) == True):
                check = 1
                break

        if (check == 0):
            pos[1] -= speed

    if (pressed.get(115) or pressed.get(1073741905)) and pos[1] <= 700.0:
        pygame.Rect.move_ip(player_copy, 0, speed)
        check = 0
        for elem in wall_list:
            if (pygame.Rect.colliderect(player_copy, elem) == True):
                check = 1
                break

        if (check == 0):
            pos[1] += speed

    if (pressed.get(100) or pressed.get(1073741903)) and pos[0] <= 1260.0:
        pygame.Rect.move_ip(player_copy, speed, 0)
        check = 0
        for elem in wall_list:
            if (pygame.Rect.colliderect(player_copy, elem) == True):
                check = 1
                break

        if (check == 0):
            pos[0] += speed

    animated_player(player, pressed)
    if (pressed.get(112)): #if p pressed open pause menu
        pause = True
    return pause

def detect_collision_with_shade(player, hitbox_shade, collect):
    for box in hitbox_shade:
        if box[1] != -1:
            if (pygame.Rect.colliderect(player.rect, box[0]) == True):
                if box[2] == 1:
                    #pygame.mixer.init()
                    shade_sound = pygame.mixer.Sound("./Assets/music/key_sound.wav")
                    pygame.mixer.Sound.play(shade_sound)
                    collect.pop()
                box[1] = -1
                break

# handle all event like key pressing or quitting
def event_handler(running, pressed, case):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            case = 3
        if event.type == pygame.KEYDOWN:
            pressed[event.key] = True
        if event.type == pygame.KEYUP:
            pressed[event.key] = False
    return running, case

def check_escape(escape, player_copy, running, case, collected):
    for elem in escape:
        if (pygame.Rect.colliderect(player_copy, elem) == True and len(collected) == 0):
            running = False
            case = 1
    return running, case

def check_speed(powerups, player_copy, speed):
    count = 0
    if powerups[0] == 0:
        return speed
    for elem in powerups:
        if elem[1] == 1:
            if pygame.Rect.contains(elem[0], player_copy) == True:
                #pygame.mixer.init()
                speed_up = pygame.mixer.Sound("./Assets/music/powerup.wav")
                pygame.mixer.Sound.play(speed_up)
                speed += 2.0
                powerups[count][1] = 0
                return speed
        count += 1
    return speed

def check_pressure_plate(pressure_plates, player_copy, teleporter):
    if pressure_plates[0] == 0:
        return
    count = 0
    for elem in pressure_plates:
        if elem[1] == 0:
            if pygame.Rect.contains(elem[0], player_copy) == True:
                #pygame.mixer.init()
                plate = pygame.mixer.Sound("./Assets/music/platetest.wav")
                pygame.mixer.Sound.play(plate)
                pressure_plates[count][1] = 1
                for elem in teleporter:
                    elem[2] = 1
        count +=1


#teleport the player
def check_teleporter(teleporter, player_copy, pos, teleport_cd, time):
    if teleporter[0] == 0:
        return
    #pygame.mixer.init()
    if teleport_cd == 0:
        if (pygame.Rect.contains(teleporter[0][0], player_copy) == True):
            if teleporter[0][1] == 'o':
                if teleporter[0][2] == 1:
                    entering_por = pygame.mixer.Sound("./Assets/music/portal_entering.wav")
                    pygame.mixer.Sound.play(entering_por)
                    pos[0] = teleporter[1][0][0]
                    pos[1] = teleporter[1][0][1]
                    teleport_cd = time
                    return teleport_cd
        if (pygame.Rect.contains(teleporter[1][0], player_copy) == True):
            if teleporter[1][1] == 'O':
                if teleporter[1][2] == 1:
                    entering_por = pygame.mixer.Sound("./Assets/music/portal_entering.wav")
                    pygame.mixer.Sound.play(entering_por)
                    pos[0] = teleporter[0][0][0]
                    pos[1] = teleporter[0][0][1]
                    teleport_cd = time
                    return teleport_cd
    if (teleport_cd - 3 < time):
        return teleport_cd

    if pygame.Rect.contains(teleporter[0][0], player_copy) == True:
        if teleporter[0][1] == 'o':
            entering_por = pygame.mixer.Sound("./Assets/music/portal_entering.wav")
            pygame.mixer.Sound.play(entering_por)
            pos[0] = teleporter[1][0][0]
            pos[1] = teleporter[1][0][1]
            teleport_cd = time
            return teleport_cd
    if (pygame.Rect.contains(teleporter[1][0], player_copy) == True):
        if teleporter[1][1] == 'O':
            entering_por = pygame.mixer.Sound("./Assets/music/portal_entering.wav")
            pygame.mixer.Sound.play(entering_por)
            pos[0] = teleporter[0][0][0]
            pos[1] = teleporter[0][0][1]
            teleport_cd = time
            return teleport_cd
    return teleport_cd

# render key top right
def key_collected_blit(collected, key, alpha_key, screen):
    pos_x = 1100

    for i in range(3 - len(collected)):
        screen.blit(key, (pos_x, 0))
        pos_x += 40
    for i in range(len(collected)):
        screen.blit(alpha_key, (pos_x, 0))
        pos_x += 40

# sets all premovement to false
def default_settings_movement(pressed):
    for i in pressed:
        if pressed[i] == True:
            pressed[i] = False

# game loop
def game_loop(screen, case, vol, map_nbr, old_vol, mute):
    running = True
    pause = False
    score = 0
    # pos and initialization of player 
    if map_nbr == 0:
        pos = [620, 280, 20, 20]
    if map_nbr == 1:
        pos = [1100, 100, 20, 20]
    if map_nbr == 2:
        pos = [80, 550, 20, 20]
    start_pos = [pos[0], pos[1]]
    speed = 2.0

    # player and group sprites initialization
    moving_sprites = pygame.sprite.Group()
    player = Player(pos[0], pos[1])
    moving_sprites.add(player)
    player_copy = pygame.Rect.copy(player.rect)

    # dictionary for pressed key
    pressed = {}

    # map sprites
    # map numbers: 0 = level3.txt  1 = map2    2 = level1
    sprites = map.load_sprites_for_map()
    maps = map.load_maps()
    hitbox_rec = map.create_map_hitbox(maps, map_nbr)
    teleporter = map.create_teleport_recs(maps, map_nbr)
    powerups = map.load_powerups(maps, map_nbr)
    presurre_plates = map.create_pressure_plate(maps, map_nbr)
    teleport_cd = 0

    # declare amount of keys and declare collected state of keys
    collected_key = []
    image_key = pygame.image.load("./Assets/map_sprites/key_1.png")
    oversized_image_key = pygame.transform.scale(image_key, (64, 64))
    alpha_image_key = oversized_image_key.copy()
    alpha_image_key.set_alpha(100)
    alpha_image_key.fill((255, 255, 255), None, pygame.BLEND_RGB_MULT)

    # way_shade arr and surface
    hitbox_shade = map.create_hit_box_shade(maps, map_nbr, collected_key)
    check_map = map.check_map_way(maps, map_nbr)
    escape = map.create_escape_rects(maps, map_nbr)
    shade_img = pygame.image.load("Assets/map_sprites/black.png")
    shade_surface = pygame.Surface((32, 32))

    # timer activated
    clock = pygame.time.Clock()
    time = 60
    timer_status = 0
    timer_font = pygame.freetype.Font("./Assets/Font/font.ttf", 30)

    soundtrack = pygame.mixer.music.load("./Assets/music/soundtrack.ogg")
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play()

    while running:
        # set and render timer ++ check if time is up, then he goes to the respawn/pause menu
        if round(time, 1) <= 0.0:
            pos[0] = start_pos[0]
            pos[1] = start_pos[1]
            time = 60
            score += 1
        if time == 60 and timer_status != 0 and pause == False:
            pygame.mixer.music.stop()
            running = respawn.respawn_function(screen)
            default_settings_movement(pressed)
            clock.tick(30)
            teleport_cd = 0
            pygame.mixer.music.play()
        timer_status = 1
        time = time - clock.tick(30) / 1000
        timer_print = timer_font.render(str(round(time, 1)), (0, 0, 0))
        if pause == True:
            time_p = time
            case, pause, running, vol, old_vol, mute = pausemenu.pause_menu(vol, old_vol, mute)
            default_settings_movement(pressed)
            time = time_p
            clock.tick(30)
            pygame.mixer.music.rewind()
        # eventhandler and movement detection
        running, case = event_handler(running, pressed, case)
        player_copy = pygame.Rect.copy(player.rect)
        pause = movement(pos, pressed, hitbox_rec, player_copy, pause, player, speed)
        detect_collision_with_shade(player, hitbox_shade, collected_key)

        player.rect.topleft = (pos[0], pos[1])
        screen.fill((0, 0, 0))
        # last number = map   ----> 0 = map1, 1 = map2
        map.tiles(maps, sprites, screen, map_nbr, powerups, presurre_plates, collected_key)
        map.load_shade_way(maps, shade_surface, screen, map_nbr, hitbox_shade, shade_img, collected_key)
        running, case = check_escape(escape, player_copy, running, case, collected_key)
        teleport_cd = check_teleporter(teleporter, player_copy, pos, teleport_cd, time)
        check_pressure_plate(presurre_plates, player_copy, teleporter)
        speed = check_speed(powerups, player_copy, speed)
        screen.blit(timer_print[0], (0, 0))
        key_collected_blit(collected_key, oversized_image_key, alpha_image_key, screen)
        moving_sprites.draw(screen)
        moving_sprites.update(player.ani_pos)
        pygame.display.update()
    pygame.mixer.music.stop()
    return case, vol, map_nbr, old_vol, mute