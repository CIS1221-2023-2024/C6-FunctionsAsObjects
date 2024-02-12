import pygame
from grid import *


pygame.init()

game = Game() 

    
# Initialize the TileClickHandler
click_handler = TileClickHandler(game)

# Main game loop
run = True
event_handlers = {
    pygame.QUIT: lambda: setattr(run, 'value', False),
    pygame.MOUSEBUTTONDOWN: lambda: click_handler.handle_click(pygame.mouse.get_pos())
}

while run:
    for event in pygame.event.get():
        handler = event_handlers.get(event.type)
        if handler:
            handler()
    
    game.draw()
    pygame.display.flip() 
    
    
    


