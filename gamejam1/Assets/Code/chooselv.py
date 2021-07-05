import pygame
import pygame.freetype

def close_window(running, mouse, case, lvl):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            case = 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 540 <= mouse[0] <= 540+200 and 260 <= mouse[1] <= 260+50: #select level one 
                lvl = 0
            elif 540 <= mouse[0] <= 540+200 and 360 <= mouse[1] <= 360+50: #select level two
                lvl = 1
            elif 540 <= mouse[0] <= 540+200 and 460 <= mouse[1] <= 460+50: #select level three
                lvl = 2
            elif 540 <= mouse[0] <= 540+200 and 600 <= mouse[1] <= 600+50: #go back to mainmenu
                running = False
                case = 0
    return running, case, lvl

def choose_lvl(lvl):
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
    text_surface, rect = GAME_FONT_head.render("Choose level", (0,0,0))
    text_button_quit, rect = GAME_FONT_menu.render("Back", color)
    text_lvl1, rect = GAME_FONT_menu.render("Level 1", color)
    text_lvl2, rect = GAME_FONT_menu.render("Level 2", color)
    text_lvl3, rect = GAME_FONT_menu.render("Level 3", color)
    text_check, rect = GAME_FONT_menu.render("X", color)
    bg = pygame.image.load("./Assets/map_sprites/bgmain.png")

    while running:
        mouse = pygame.mouse.get_pos() 

        running, case, lvl = close_window(running, mouse, case, lvl)

        screenm.fill((0, 0, 0))
        screenm.blit(bg, (0, 0))
        #detect mouse over button lvl1
        if 540 <= mouse[0] <= 540+200 and 260 <= mouse[1] <= 260+50: 
            pygame.draw.rect(screenm,color_light,[540,260,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,260,200,50])
        #detect mouse over button lvl2
        if 540 <= mouse[0] <= 540+200 and 360 <= mouse[1] <= 360+50: 
            pygame.draw.rect(screenm,color_light,[540,360,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,360,200,50])
        #detect mouse over button lv3
        if 540 <= mouse[0] <= 540+200 and 460 <= mouse[1] <= 460+50: 
            pygame.draw.rect(screenm,color_light,[540,460,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,460,200,50])
        #detect mouse over button back
        if 540 <= mouse[0] <= 540+200 and 600 <= mouse[1] <= 600+50: 
            pygame.draw.rect(screenm,color_light,[540,600,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,600,200,50])

        screenm.blit(text_surface, (350, 100))
        screenm.blit(text_lvl1, (560, 270))
        screenm.blit(text_lvl2, (570, 370))
        screenm.blit(text_lvl3, (560, 470))
        screenm.blit(text_button_quit , (600, 610))

        if lvl == 0:
            pygame.draw.rect(screenm,color_light,[750,260,50,50])
            screenm.blit(text_check, (766, 273))
            pygame.draw.rect(screenm,color_light,[480,260,50,50])
            screenm.blit(text_check, (497, 273))
        elif lvl == 1:
            pygame.draw.rect(screenm,color_light,[750,360,50,50])
            screenm.blit(text_check, (766, 373))
            pygame.draw.rect(screenm,color_light,[480,360,50,50])
            screenm.blit(text_check, (497, 373))
        elif lvl == 2:
            pygame.draw.rect(screenm,color_light,[750,460,50,50])
            screenm.blit(text_check, (766, 473))
            pygame.draw.rect(screenm,color_light,[480,460,50,50])
            screenm.blit(text_check, (497, 473))

        pygame.display.flip()
        pygame.display.update()
    return case, lvl