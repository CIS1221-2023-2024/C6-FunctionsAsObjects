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
            button_clicked = True 
            mouse_pos = pygame.mouse.get_pos()
            for button in game.button_list:
                if button.is_over(mouse_pos[0], mouse_pos[1]):
                  button.handle_click()
                  button_clicked = False
                  break

            if not button_clicked:
             click_handler.handle_click(mouse_pos, click_handler.switch_tiles)
        
    
    game.draw(game.draw_grid)
    pygame.display.flip() 
   
pygame.quit()
    
    
    


