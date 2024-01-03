import pygame
pygame.init()
from grid import *


class Tile:
    def __init__(self, background, col, row,image, size):

        self.background = background  # here its refering to the tiles background
        self.col = col
        self.row = row
        self.image = image
        self.size = size
        self.x = row * size
        self.y = col * size 
    
    def draw(self):
        self.background.blit(self.image, (self.x, self.y))


#initialize the tile w properties position, label, etc.
pass

def create_game(background):

    grid = []
    number = 1
    for x in range(LEVEL_SIZE):
        grid.append([])
        for y in range(LEVEL_SIZE):
            grid[x].append(number)
            number += 1
        grid[-1][-1] =  0 
    print(grid)
    return grid

def new(background):
    background.all_spirites = pygame.spirite.Group()
    background.tiles_grid = create_game(background)
    background.tiles_grid_completed = create_game(background)

   

def draw_tiles(background):

#Initilising list as empty 
    background.tiles = []
    for row, x in enumerate(background.tiles_grid):
        background.tiles.append([])
        for col, tile_number in enumerate(x):
            if tile_number != 0:
                tile = Tile(background, col, row, str(tile_number))
                
            else:
                tile= Tile(background, col, row, "empty")
            background.tiles[row].append(tile)

