import pygame 
#update
#TEST

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

# Tile class
class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text, tile_id):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.x, self.y = x, y
        self.text = text
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE + game.start_x, y * TILE_SIZE + game.start_y))
        self.id = tile_id

        if self.text != "empty":
            self.image.fill((255, 255, 255))  # White color for non-empty tiles
            self.font = pygame.font.SysFont("Consolas", 50)
            font_surface = self.font.render(self.text, True, (0, 0, 0))  # Black font color
            font_size = self.font.size(self.text)
            draw_x = (TILE_SIZE - font_size[0]) // 2
            draw_y = (TILE_SIZE - font_size[1]) // 2
            self.image.blit(font_surface, (draw_x, draw_y))
        else:
            self.image.fill((0, 0, 0))  # Black color for empty tile

# Game class
class Game:
    def __init__(self):
        self.background = pygame.display.set_mode((BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.create_game()
        self.start_x = (BACKGROUND_WIDTH - LEVEL_SIZE * TILE_SIZE) // 2
        self.start_y = (BACKGROUND_HEIGHT - LEVEL_SIZE * TILE_SIZE) // 1.2
        self.draw_tiles()

    def create_game(self):
        grid = []
        number = 1
        for y in range(LEVEL_SIZE):
            row = []
            for x in range(LEVEL_SIZE):
                if number < LEVEL_SIZE * LEVEL_SIZE:
                    row.append(number)
                else:
                    row.append(0)  # 0 represents the empty tile
                number += 1
            grid.append(row)
        return grid

    def draw_tiles(self):
         for y, row in enumerate(self.tiles_grid):
          for x, tile in enumerate(row):
            tile_text = str(tile) if tile != 0 else "empty"
            Tile(self, x, y, tile_text, tile) 

    def draw(self):
        self.background.fill((255, 255, 255))  # White background
        self.all_sprites.draw(self.background)
        self.draw_grid()
        pygame.display.flip()

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