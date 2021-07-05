import pygame
import pygame.freetype

def close_window(running, mouse, case, vol, mute, old_vol):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            case = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 540 <= mouse[0] <= 540+200 and 560 <= mouse[1] <= 560+50: #go to main menu
                running = False
                case = 0
            elif 690 <= mouse[0] <= 690+50 and 310 <= mouse[1] <= 310+50: #increase volume
                if (vol < 100 and vol >= 0):
                    vol += 10
            elif 540 <= mouse[0] <= 540+50 and 310 <= mouse[1] <= 310+50: #decrease volume
                if (vol <= 100 and vol > 0):
                    vol -= 10
            elif 540 <= mouse[0] <= 540+200 and 410 <= mouse[1] <= 410+50:
                if mute == 0:
                    old_vol = vol
                    vol = 0
                    mute = 1
                else:
                    mute = 0
                    vol = old_vol
    return running, case, vol, mute, old_vol

def settings_menu(volume, mute, old_vol):
    case = 1
    screenm = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("No Escape")
    running = True
    GAME_FONT_head = pygame.freetype.Font("./Assets/Font/font.ttf", 100)
    GAME_FONT_menu = pygame.freetype.Font("./Assets/Font/font.ttf", 35)
    color = (0,0,0)
    color_light = (170,170,170) 
    color_dark = (100,100,100)
    text_surface, rect = GAME_FONT_head.render("Settings", (0,0,0))
    text_button_quit, rect = GAME_FONT_menu.render("Back", color)
    text_vol_name, rect = GAME_FONT_menu.render("volume", color)
    text_plus, rect = GAME_FONT_menu.render("+", color)
    text_minus, rect = GAME_FONT_menu.render("-", color)
    text_button_mute, rect = GAME_FONT_menu.render("Mute", color)
    vol = volume * 100
    bg = pygame.image.load("./Assets/map_sprites/bgmain.png")
    while running:
        
        mouse = pygame.mouse.get_pos() 

        running, case, vol, mute, old_vol = close_window(running, mouse, case, vol, mute, old_vol)
        
        screenm.fill((0, 0, 0))
        screenm.blit(bg, (0, 0))
        #detect mouse over button back
        if 540 <= mouse[0] <= 540+200 and 560 <= mouse[1] <= 560+50: 
            pygame.draw.rect(screenm,color_light,[540,560,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,560,200,50]) 
        #detect mouse over minus
        if 540 <= mouse[0] <= 540+50 and 310 <= mouse[1] <= 310+50: 
            pygame.draw.rect(screenm,color_light,[540,310,50,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,310,50,50])
        #detect mouse over plus
        if 690 <= mouse[0] <= 690+50 and 310 <= mouse[1] <= 310+50: 
            pygame.draw.rect(screenm,color_light,[690,310,50,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[690,310,50,50])
        # mouse over mute
        if mute == 1:
            pygame.draw.rect(screenm,(255, 0, 0),[540,410,200,50])
        elif 540 <= mouse[0] <= 540+200 and 410 <= mouse[1] <= 410+50: 
            pygame.draw.rect(screenm,color_light,[540,410,200,50]) 
        else: 
            pygame.draw.rect(screenm,color_dark,[540,410,200,50])    

        screenm.blit(text_surface, (440, 100))
        screenm.blit(text_button_quit , (600, 570))

        screenm.blit(text_vol_name, (580, 280))

        screenm.blit(text_plus, (706, 327))

        screenm.blit(text_minus, (558, 334))

        

        screenm.blit(text_button_mute, (600, 420))

        text_vol_num, rect = GAME_FONT_menu.render(str(int(vol)), color)
        screenm.blit(text_vol_num, (615, 323))

        
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
    return case, (vol / 100), mute, old_vol
