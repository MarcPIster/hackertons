import pygame

pygame.init()

def create_window(height, width):
    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption("No Escape")
    return screen