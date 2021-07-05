import pygame
import pygame.freetype
import sys 
from Assets.Code import gameloop, screen, instructionmenu

def close_window(running, mouse, case):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            case = 3
            pygame.mixer.music.stop()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 220 <= mouse[0] <= 220+200 and 260 <= mouse[1] <= 260+50: #start game
                running = False
                case = 6 
                pygame.mixer.music.stop()
            if 220 <= mouse[0] <= 220+200 and 410 <= mouse[1] <= 410+50: #open lvl selector
                running = False
                case = 7
            if 540 <= mouse[0] <= 540+200 and 410 <= mouse[1] <= 410+50: #open instructions
                running = False
                case = 2
            if 860 <= mouse[0] <= 860+200 and 260 <= mouse[1] <= 260+50: #open settings
                running = False
                case = 4
            if 860 <= mouse[0] <= 860+200 and 410 <= mouse[1] <= 410+50: #close game
                running = False
                case = 3
                pygame.mixer.music.stop()
            if 540 <= mouse[0] <= 540+200 and 260 <= mouse[1] <= 260+50: 
                 running = False
                 case = 5
    return running, case

#main menu
def main_menu(vol):
    case = 0
    screenm = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("No Escape")
    running = True
    #load font
    GAME_FONT_head = pygame.freetype.Font("./Assets/Font/font.ttf", 100) 
    GAME_FONT_creato = pygame.freetype.Font("./Assets/Font/font.ttf", 25)
    GAME_FONT_menu = pygame.freetype.Font("./Assets/Font/font.ttf", 35)
    #set colors
    color = (0,0,0) 
    color_light = (170,170,170) 
    color_dark = (100,100,100)
    #set text
    text_surface, rect = GAME_FONT_head.render("No Escape", (0,0,0))
    text_button_quit, rect = GAME_FONT_menu.render("Quit", color)
    text_creator, rect = GAME_FONT_creato.render("Made by Gylian Kasch, Marc Pister, Pablo Herrmann and Ramon Werner", (0,0,0))
    text_button_start, rect = GAME_FONT_menu.render("Start", color)
    text_button_help, rect = GAME_FONT_menu.render("Help", color)
    text_button_setting, rect = GAME_FONT_menu.render("Settings", color)
    text_button_lvl, rect = GAME_FONT_menu.render("Levels", color)
    text_highscore, rect = GAME_FONT_menu.render("Highscore", color)
    # load music
    music = pygame.mixer.music.load("./Assets/music/music.ogg")
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play()

    bg = pygame.image.load("./Assets/map_sprites/bgmain.png")

    while running:

        mouse = pygame.mouse.get_pos() 

        running, case = close_window(running, mouse, case)

        screenm.fill((0, 0, 0))
        
        screenm.blit(bg, (0, 0))

        #detect mouse over button start
        if 220 <= mouse[0] <= 220+200 and 260 <= mouse[1] <= 260+50: 
            pygame.draw.rect(screenm,color_light,[220,260,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[220,260,200,50])
        #detect mouse over button lvl
        if 220 <= mouse[0] <= 220+200 and 410 <= mouse[1] <= 410+50: 
            pygame.draw.rect(screenm,color_light,[220,410,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[220,410,200,50])
            #detect mouse over hs
        if 540 <= mouse[0] <= 540+200 and 260 <= mouse[1] <= 260+50: 
            pygame.draw.rect(screenm,color_light,[540,260,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,260,200,50])
        #detect mouse over button help
        if 540 <= mouse[0] <= 540+200 and 410 <= mouse[1] <= 410+50: 
            pygame.draw.rect(screenm,color_light,[540,410,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,410,200,50])
        #detect mouse over button settings
        if 860 <= mouse[0] <= 860+200 and 260 <= mouse[1] <= 260+50: 
            pygame.draw.rect(screenm,color_light,[860,260,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[860,260,200,50])
        #detect mouse over button quit
        if 860 <= mouse[0] <= 860+200 and 410 <= mouse[1] <= 410+50: 
            pygame.draw.rect(screenm,color_light,[860,410,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[860,410,200,50]) 
        

        #draw text
        screenm.blit(text_surface, (400, 50))

        screenm.blit(text_button_start, (270, 270))
        screenm.blit(text_button_lvl, (260, 420))

        screenm.blit(text_highscore, (550, 270))
        screenm.blit(text_button_help, (600, 420))

        screenm.blit(text_button_setting, (880, 270))
        screenm.blit(text_button_quit , (920, 420))

        screenm.blit(text_creator, (10, 690))

        #adjustment lines
        # pygame.draw.line(screen, (0, 255, 255), (540, 0), (540, 720))
        # pygame.draw.line(screen, (0, 0, 255), (565, 0), (565, 720))
        # pygame.draw.line(screen, (255, 255, 255), (590, 0), (590, 720))
        # pygame.draw.line(screen, (0, 0, 255), (640, 0), (640, 720))
        # pygame.draw.line(screen, (255, 255, 255), (690, 0), (690, 720))
        # pygame.draw.line(screen, (0, 0, 255), (715, 0), (715, 720))
        # pygame.draw.line(screen, (0, 255, 255), (740, 0), (740, 720))
        # pygame.draw.line(screen, (0, 0, 255), (0, 160), (1280, 160))
        # pygame.draw.line(screen, (0, 0, 255), (0, 260), (1280, 260))
        # pygame.draw.line(screen, (0, 0, 255), (0, 360), (1280, 360))
        # pygame.draw.line(screen, (0, 0, 255), (0, 460), (1280, 460))
        # pygame.draw.line(screen, (0, 0, 255), (0, 560), (1280, 560))
        # pygame.draw.line(screen, (0, 0, 255), (0, 660), (1280, 660))
        # pygame.draw.line(screen, (0, 0, 255), (0, 180), (1280, 180))
        # pygame.draw.line(screen, (0, 0, 255), (0, 540), (1280, 540))

        pygame.display.flip()
        pygame.display.update()
    # if (case == 1):
    #     window = screen.create_window(1280, 720)
    #     gameloop.game_loop(window)
    # elif (case == 2):
    #     instructionmenu.instruction()
    # else:
    # pygame.quit()
    #pygame.mixer.music.stop()
    return case, vol


    