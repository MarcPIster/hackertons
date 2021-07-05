import pygame

def respawn_function(screen):
    running = True
    state = True
    pause_surface  = pygame.Surface((1280, 720))
    pause_surface.set_alpha(3)
    pause_surface.fill((255, 255, 255))
    message_font = pygame.freetype.Font("./Assets/Font/font.ttf", 30)
    message_print = message_font.render("Press Enter to Start your Hussle", (0, 0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                state = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
        screen.blit(pause_surface, (0, 0))
        screen.blit(message_print[0], (300, 345))
        pygame.display.update()
        
    return state
