import pygame 

#Initilizing pygame extenstion
pygame.init() 

#Creating width and height for screen/background
BACKGROUND_WIDTH = 1000
BACKGROUND_HEIGHT = 600

#Line responsible for creating the screen 
background = pygame.display.set_mode((BACKGROUND_WIDTH, BACKGROUND_HEIGHT))


grid = pygame.Rect((350, 200, 300, 300 ))

run = True
while run:  
  
  pygame.draw.rect(background,(255, 255, 255), grid)

  #lines 17 - 19 act as an event handler 
  for event in pygame.event.get():  
     if event.type == pygame.QUIT:
        run = False

  pygame.display.update()      
        
pygame.quit()

