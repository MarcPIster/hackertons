import pygame
import pygame.freetype

def close_window(running, mouse, case):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            case = 3
            pygame.mixer.music.stop()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1030 <= mouse[0] <= 1030+200 and 620 <= mouse[1] <= 620+50: #back to main
                running = False
                case = 0
    return running, case

def highscore_menu(score):
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
    text_surface, rect = GAME_FONT_head.render("Highscore", (0,0,0))
    text_button_quit, rect = GAME_FONT_menu.render("Back", color)

    bg = pygame.image.load("./Assets/map_sprites/bgmain.png")

    while running:
        mouse = pygame.mouse.get_pos() 

        running, case = close_window(running, mouse, case)

        screenm.fill((0, 0, 0))
        
        screenm.blit(bg, (0, 0))

        if 1030 <= mouse[0] <= 1030+200 and 620 <= mouse[1] <= 620+50: 
            pygame.draw.rect(screenm,color_light,[1030,620,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[1030,620,200,50]) 

        screenm.blit(text_surface, (400, 50))

        screenm.blit(text_button_quit , (1090, 630))

        pygame.display.flip()
        pygame.display.update()

    return case