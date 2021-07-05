import pygame
import pygame.freetype
from Assets.Code import settingsmenu

def close_window(running, mouse, case, pause, close, vol, old_vol, mute):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pause = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 540 <= mouse[0] <= 540+200 and 235 <= mouse[1] <= 235+50: #resume game
                running = False
                case = 6
                pause = False
                close = True
            elif 540 <= mouse[0] <= 540+200 and 335 <= mouse[1] <= 335+50: #restart game 
                running = False
                case = 6
                pause = False
                close = False
            elif 540 <= mouse[0] <= 540+200 and 435 <= mouse[1] <= 435+50: #go to mainmenu
                running = False
                case = 0
                pause = False
                close = False
            elif 540 <= mouse[0] <= 540+200 and 535 <= mouse[1] <= 535+50:
                case, vol, mute, old_vol = settingsmenu.settings_menu(vol, mute, old_vol)
                pygame.mixer.music.set_volume(vol)
            elif 540 <= mouse[0] <= 540+200 and 635 <= mouse[1] <= 635+50: #close game
                running = False
                case = 3
                pause = False
                close = False
    return running, case, pause, close, vol, old_vol, mute

def pause_menu(vol, old_vol, mute):
    close = False
    pause = True
    case = 1
    i = 0
    screenm = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("No Escape")
    running = True
    GAME_FONT_head = pygame.freetype.Font("./Assets/Font/font.ttf", 100)
    GAME_FONT_menu = pygame.freetype.Font("./Assets/Font/font.ttf", 35)
    color = (0,0,0)
    color_light = (170,170,170) 
    color_dark = (100,100,100)
    text_surface, rect = GAME_FONT_head.render("Pause", (0,0,0))
    text_continue, rect = GAME_FONT_menu.render("Continue", color)
    text_restart, rect = GAME_FONT_menu.render("Restart", color)
    text_main, rect = GAME_FONT_menu.render("Mainmenu", color)
    text_settings, rect = GAME_FONT_menu.render("Setings", color)
    text_exit, rect = GAME_FONT_menu.render("Exit", color)
    bg = pygame.image.load("./Assets/map_sprites/bgmain.png")
    camp_fire = pygame.image.load("./Assets/map_sprites/campfire.png")
    camp_fire = pygame.transform.scale(camp_fire, (150,150))
    bonfire = pygame.image.load("./Assets/bonfire_sprites/bonfire7.png")
    bonfire = pygame.transform.scale(bonfire, (200, 200))
    fp = []
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire1.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire2.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire3.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire4.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire5.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire6.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire7.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire8.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire9.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire10.png"))
    fp.append(pygame.image.load("./Assets/bonfire_sprites/bonfire11.png"))

    music = pygame.mixer.music.load("./Assets/music/bonfire.ogg")
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play()
    
    clock = pygame.time.Clock()

    while running:
        clock.tick(10)
        
        mouse = pygame.mouse.get_pos() 

        running, case, pause, close, vol, old_vol, mute = close_window(running, mouse, case, pause, close, vol, old_vol, mute)

        screenm.fill((0, 0, 0))
        screenm.blit(bg, (0, 0))


        #screenm.blit(camp_fire, (50, 570))
        #screenm.blit(bonfire, (170, 520))

        #detect mouse over button continue
        if 540 <= mouse[0] <= 540+200 and 235 <= mouse[1] <= 235+50: 
            pygame.draw.rect(screenm,color_light,[540,235,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,235,200,50])
        #detect mouse over button restart
        if 540 <= mouse[0] <= 540+200 and 335 <= mouse[1] <= 335+50: 
            pygame.draw.rect(screenm,color_light,[540,335,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,335,200,50])
        #detect mouse over button main
        if 540 <= mouse[0] <= 540+200 and 435 <= mouse[1] <= 435+50: 
            pygame.draw.rect(screenm,color_light,[540,435,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,435,200,50])
        #detect mouse over settings
        if 540 <= mouse[0] <= 540+200 and 535 <= mouse[1] <= 535+50: 
            pygame.draw.rect(screenm,color_light,[540,535,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,535,200,50])
        #detect mouse over button exit
        if 540 <= mouse[0] <= 540+200 and 635 <= mouse[1] <= 635+50: 
            pygame.draw.rect(screenm,color_light,[540,635,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,635,200,50])

        screenm.blit(fp[i], (100, 480))
        i += 1
        if i == 10:
            i = 0

        screenm.blit(text_surface, (500, 100))
        screenm.blit(text_continue, (560, 245))
        screenm.blit(text_restart, (570, 345))
        screenm.blit(text_main, (560, 445))
        screenm.blit(text_settings, (560, 545))
        screenm.blit(text_exit, (600, 645))

        # pygame.draw.line(screenm, (0, 255, 255), (540, 0), (540, 720))
        # pygame.draw.line(screenm, (0, 0, 255), (565, 0), (565, 720))
        # pygame.draw.line(screenm, (255, 255, 255), (590, 0), (590, 720))
        # pygame.draw.line(screenm, (0, 0, 255), (640, 0), (640, 720))
        # pygame.draw.line(screenm, (255, 255, 255), (690, 0), (690, 720))
        # pygame.draw.line(screenm, (0, 0, 255), (715, 0), (715, 720))
        # pygame.draw.line(screenm, (0, 255, 255), (740, 0), (740, 720))

        # pygame.draw.line(screenm, (0, 0, 255), (0, 310), (1280, 310))
        # pygame.draw.line(screenm, (0, 0, 255), (0, 335), (1280, 335))

        # pygame.draw.line(screenm, (0, 0, 255), (0, 160), (1280, 160))
        # pygame.draw.line(screenm, (0, 0, 255), (0, 260), (1280, 260))
        # pygame.draw.line(screenm, (0, 0, 255), (0, 360), (1280, 360))
        # pygame.draw.line(screenm, (0, 0, 255), (0, 460), (1280, 460))
        # pygame.draw.line(screenm, (0, 0, 255), (0, 560), (1280, 560))
        # pygame.draw.line(screenm, (0, 0, 255), (0, 660), (1280, 660))
        # pygame.draw.line(screenm, (0, 0, 255), (0, 180), (1280, 180))
        # pygame.draw.line(screenm, (0, 0, 255), (0, 540), (1280, 540))

        pygame.display.flip()
        pygame.display.update()
    pygame.mixer.music.stop()
    return case, pause, close, vol, old_vol, mute
