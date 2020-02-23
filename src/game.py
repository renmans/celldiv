import pygame
import yaml
from pygame.locals import *
import random
import launcher

class GameOfLife:
    def __init__(self, width, height, cell_size, speed, cell_color):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cell_color = cell_color
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.speed = speed


    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))


    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Cellton')
        self.screen.fill(pygame.Color('white'))
        running = True
        clist = self.cell_list(True)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.draw_cell_list(clist)
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize = False):
        if randomize:
            list = [[0 for x in range(self.width // self.cell_size)] for y in range(self.height // self.cell_size)]
            for i in range(self.height // self.cell_size):
                for j in range(self.width // self.cell_size):
                    list[i][j] = random.randint(0, 1)
            return list
        else:
            return [[0] * (self.width // self.cell_size)] * (self.height // self.cell_size)

    def draw_cell_list(self, list):
        a, b = 0, 0
        for x in list:
            a = 0
            for i in x:
                if i:
                    pygame.draw.rect(self.screen, pygame.Color(self.cell_color), Rect(a, b, self.cell_size, self.cell_size))
                a += self.cell_size
            b += self.cell_size

if __name__ == '__main__':
    if launcher.main():
        with open('settings.yml', 'r') as f:
            params = yaml.safe_load(f)
            game = GameOfLife(params['width'], params['height'], 
                    params['cell_size'], params['speed'], 
                    params['cell_color'])
        #game = GameOfLife(120, 100, 10, 10, 'green')
        game.run()
