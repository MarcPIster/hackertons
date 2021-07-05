import pygame
import pygame.freetype

def close_window(running, mouse, case):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            case = 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 540 <= mouse[0] <= 540+200 and 610 <= mouse[1] <= 610+50: #exit game
                running = False
                case = 3
            elif 540 <= mouse[0] <= 540+200 and 510 <= mouse[1] <= 510+50: #go to mainmenu
                running = False
                case = 0    
    return running, case

def end_screen():
    case = 1
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("No Escape")
    running = True
    GAME_FONT_head = pygame.freetype.Font("./Assets/Font/font.ttf", 100)
    GAME_FONT_menu = pygame.freetype.Font("./Assets/Font/font.ttf", 35)
    color = (0,0,0)
    color_light = (170,170,170) 
    color_dark = (100,100,100)
    text_surface, rect = GAME_FONT_head.render("Level Cleared!", (0,0,0))
    text_main, rect = GAME_FONT_menu.render("Mainmenu", color)
    text_exit, rect = GAME_FONT_menu.render("Exit", color)
    bg = pygame.image.load("./Assets/map_sprites/bgmain.png")
    tcc = pygame.image.load("./Assets/map_sprites/tcc.png")
    tco = pygame.image.load("./Assets/map_sprites/tco.png")

    while running:
        
        mouse = pygame.mouse.get_pos() 

        running, case = close_window(running, mouse, case)

        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        #detect mouse over button main
        if 540 <= mouse[0] <= 540+200 and 510 <= mouse[1] <= 510+50: 
            pygame.draw.rect(screen,color_light,[540,510,200,50]) 
        else: 
            pygame.draw.rect(screen,color_dark,[540,510,200,50])
        #detect mouse over button exit
        if 540 <= mouse[0] <= 540+200 and 610 <= mouse[1] <= 610+50: 
            pygame.draw.rect(screen,color_light,[540,610,200,50]) 
        else: 
            pygame.draw.rect(screen,color_dark,[540,610,200,50])
        #display chest
        if 513 <= mouse[0] <= 513+254 and 200 <= mouse[1] <= 200+254:
            screen.blit(tco, (513, 200))
        else:
            screen.blit(tcc, (513, 200))

        screen.blit(text_surface, (250, 100))
        screen.blit(text_main, (560, 520))
        screen.blit(text_exit, (600, 620))

        pygame.display.flip()
        pygame.display.update()
    return case