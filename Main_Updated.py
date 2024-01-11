import pygame
from grid import *

pygame.init()

game = Game()

# Initialize the TileClickHandler
click_handler = TileClickHandler(game)

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_handler.handle_click(pygame.mouse.get_pos())

    game.draw()
    pygame.display.flip()