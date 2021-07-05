import pygame
import sys 
from Assets.Code import mainmenu

def close_window(running, mouse, case):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            case = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 540 <= mouse[0] <= 540+200 and 600 <= mouse[1] <= 600+50: #go back to mainmenu
                running = False
                case = 0
    return running, case

def instruction():
    case = 1
    screenm = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("No Escape")
    running = True
    GAME_FONT_head = pygame.freetype.Font("./Assets/Font/font.ttf", 100)
    GAME_FONT_menu = pygame.freetype.Font("./Assets/Font/font.ttf", 35)
    color = (0,0,0)
    color_light = (170,170,170) 
    color_dark = (100,100,100)
    #set text
    text_surface, rect = GAME_FONT_head.render("How to play", (0,0,0))
    text_button_quit, rect = GAME_FONT_menu.render("Back", color)
    text_controlls, rect = GAME_FONT_menu.render("Controlls:", color)
    text_keys, rect = GAME_FONT_menu.render("w, a, s, d    -    move character", color)
    text_instructions1, rect = GAME_FONT_menu.render("You have 1 minute to solve the maze", color)
    text_instructions2, rect = GAME_FONT_menu.render("Good luck and have fun!", color)
    text_instructions3, rect = GAME_FONT_menu.render("Discover the maze and collect power-ups", color)
    text_pause, rect = GAME_FONT_menu.render("p    -    pause game", color)
    bg = pygame.image.load("./Assets/map_sprites/bgmain.png")
    while running:
        
        mouse = pygame.mouse.get_pos() 

        running, case = close_window(running, mouse, case)

        screenm.fill((0, 0, 0))
        screenm.blit(bg, (0, 0))
         #detect mouse over button back
        if 540 <= mouse[0] <= 540+200 and 600 <= mouse[1] <= 600+50: 
            pygame.draw.rect(screenm,color_light,[540,600,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,600,200,50]) 
        #draw text
        screenm.blit(text_controlls, (200, 260))
        screenm.blit(text_keys, (350, 310))
        screenm.blit(text_pause, (540, 360))
        screenm.blit(text_surface, (350, 100))
        screenm.blit(text_button_quit , (600, 610))

        screenm.blit(text_instructions1 , (250, 410))
        screenm.blit(text_instructions3 , (230, 460))
        screenm.blit(text_instructions2 , (400, 510))

        pygame.display.flip()
        pygame.display.update()
    return case