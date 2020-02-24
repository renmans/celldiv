import random
import pygame
from pygame.locals import QUIT, Rect
import yaml
import launcher


class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=10,
                 cell_color='black'):
        self.width = width
        self.height = height
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.cell_size = cell_size
        self.cell_color = cell_color
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.speed = speed
        self.cells = self.cell_list()
        print(len(self.cells))  # rows
        print(len(self.cells[0]))  # columns

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def cell_list(self, randomize=False):
        if randomize:
            for i in range(self.height // self.cell_size):
                for j in range(self.width // self.cell_size):
                    self.cells[i][j] = random.randint(0, 1)
            return self.cells
        else:
            return [[0 for x in range(self.width // self.cell_size)]
                    for y in range(self.height // self.cell_size)]

    def draw_cell_list(self, list):
        column, row = 0, 0
        for cell in list:
            column = 0
            for cell_state in cell:
                if cell_state:
                    pygame.draw.rect(self.screen,
                                     pygame.Color(self.cell_color),
                                     Rect(column, row, self.cell_size,
                                          self.cell_size))
                column += self.cell_size
            row += self.cell_size

    def get_neighbours(self, cell):
        pass

    def get_next_generation(self):
        pass

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
            self.draw_cell_list(clist)
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == '__main__':
    if launcher.main():
        try:
            with open('settings.yml', 'r') as f:
                params = yaml.safe_load(f)
                game = GameOfLife(params['width'], params['height'],
                                  params['cell_size'], params['speed'],
                                  params['cell_color'])
        except FileNotFoundError:
            game = GameOfLife()
        game.run()
