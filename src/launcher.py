import pygame
import pygameMenu

WINDOW_SIZE = (640, 480)

# Pygame initialization
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Cellton Launcher')
clock = pygame.time.Clock()

menu = pygameMenu.Menu(surface, window_width=WINDOW_SIZE[0],
        window_height=WINDOW_SIZE[1], font=pygameMenu.font.FONT_BEBAS,
        title='MENU')
