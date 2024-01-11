import pygame 

#Initilizing pygame extenstion
pygame.init() 

#Creating width and height for screen/background
BACKGROUND_WIDTH = 1000
BACKGROUND_HEIGHT = 600

#Line responsible for creating the screen 
background = pygame.display.set_mode((BACKGROUND_WIDTH, BACKGROUND_HEIGHT))

#Initilising some variables 
LEVEL_SIZE = 4    
TILE_SIZE = 90


# Making the actual grid 
def draw_grid(background):

  # calculating position to centre grid at the bottom 
  start_x = (BACKGROUND_WIDTH - LEVEL_SIZE * TILE_SIZE) // 2
  start_y = (BACKGROUND_HEIGHT - LEVEL_SIZE * TILE_SIZE) // 1.2



  for row in range(LEVEL_SIZE + 1):
        pygame.draw.line(background, (150, 150, 150), 
                         (start_x, start_y + row * TILE_SIZE), 
                         (start_x + LEVEL_SIZE * TILE_SIZE, start_y + row * TILE_SIZE))
  for col in range(LEVEL_SIZE + 1):
        pygame.draw.line(background, (150, 150, 150), 
                         (start_x + col * TILE_SIZE, start_y), 
                         (start_x + col * TILE_SIZE, start_y + LEVEL_SIZE * TILE_SIZE))



run = True
while run:  
  

  #lines 17 - 19 act as an event handler 
  for event in pygame.event.get():  
     if event.type == pygame.QUIT:
        run = False
  
  # Clear the screen and draw the grid
  draw_grid(background)
  pygame.display.update()      
        
pygame.quit()