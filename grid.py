import pygame
import random
from Button import *

pygame.init() 

#Creating width and height for screen/background
BACKGROUND_WIDTH = 1000
BACKGROUND_HEIGHT = 600
LEVEL_SIZE = 4    
TILE_SIZE = 90

#Line responsible for creating the screen 
background = pygame.display.set_mode((BACKGROUND_WIDTH, BACKGROUND_HEIGHT))

#Initilising some variables 


# Tile class
class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text, tile_id):
        pygame.sprite.Sprite.__init__(self, game.all_sprites)
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.x, self.y = x, y
        self.text = text
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE + game.start_x, y * TILE_SIZE + game.start_y))
        self.id = tile_id
        self.shuffle = 0
        self.start_shuffle = True

        if self.text !=  "empty":
            self.image.fill((255, 255, 255))  # White color for non-empty tiles
            self.font = pygame.font.SysFont("Consolas", 50)
            font_surface = self.font.render(str(self.text), True, (0, 0, 0))  # Display tile's value
            font_size = self.font.size(str(self.text))
            draw_x = (TILE_SIZE - font_size[0]) // 2
            draw_y = (TILE_SIZE - font_size[1]) // 2
            self.image.blit(font_surface, (draw_x, draw_y))
        else:
            self.image.fill((0, 0, 0))  # Black color for empty tile


    def left(self):
     if self.x > 0:
        return True
     return False

    def right(self):
     if self.x < LEVEL_SIZE - 1:
        return True
     return False

    def up(self):
     if self.y > 0:
        return True
     return False

    def down(self):
     if self.y < LEVEL_SIZE - 1:
        return True
     return False



# Game class
class Game:
    def __init__(self):
        self.background = pygame.display.set_mode((BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        self.all_sprites = pygame.sprite.Group()
        self.start_x = (BACKGROUND_WIDTH - LEVEL_SIZE * TILE_SIZE) // 2
        self.start_y = (BACKGROUND_HEIGHT - LEVEL_SIZE * TILE_SIZE) // 1.2
        self.tiles_grid = self.create_game()
        self.button_list = []
        self.button_list.append(Button(self, (255, 255, 255), (0, 0, 0), BACKGROUND_WIDTH - 220, 20, 150, 50, "Shuffle"))
        self.button_list.append(Button(self, (255, 255, 255), (0, 0, 0), BACKGROUND_WIDTH - 220, 90, 150, 50, "Reset"))
        self.shuffle_time = 0
        self.start_shuffle = False
        self.previous_choice = ""
        self.shuffle_requested = False
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
                Tile(self, x, y, tile_text, tile)  # Create Tile instances for each grid element
       

    
   # Inside Game class in grid.py
    def shuffle_tiles(self):
      print("Shuffling Tiles")  # Debug print
      for _ in range(100):  # Adjust the number for more or less shuffling
        empty_tile_position = self.get_empty_tile_position()
      if empty_tile_position:
            empty_x, empty_y = empty_tile_position
            possible_moves = []

            if self.tiles_grid[empty_y][empty_x].left():
                possible_moves.append((-1, 0))  # Move left
            if self.tiles_grid[empty_y][empty_x].right():
                possible_moves.append((1, 0))   # Move right
            if self.tiles_grid[empty_y][empty_x].up():
                possible_moves.append((0, -1))  # Move up
            if self.tiles_grid[empty_y][empty_x].down():
                possible_moves.append((0, 1))   # Move down

            if possible_moves:
                move_x, move_y = random.choice(possible_moves)
                target_x, target_y = empty_x + move_x, empty_y + move_y
                self.tiles_grid[empty_y][empty_x], self.tiles_grid[target_y][target_x] = \
                    self.tiles_grid[target_y][target_x], self.tiles_grid[empty_y][empty_x]
                self.update_tile_positions()
                print(f"Shuffling move: {move_x}, {move_y}")  # Debug print
            else:
               print("No moves available")  # Debug print when no moves are possible

            self.shuffle_requested = False


            
           

                
def draw_tiles(self):
                  for y, row in enumerate(self.tiles_grid):
                   for x, tile in enumerate(row):
                    tile_text = str(tile) if tile != 0 else "empty"
                    Tile(self, x, y, tile_text, tile) 

        
        
def update(self):
           self.all_sprites.update()
           if self.start_shuffle:
              self.shuffle_tiles()
              self.draw_tiles()
              if self.shuffle_requested:
                 self.shuffle_tiles()

def check_button_click(self, mouse_pos):
         print("Checking button click")  # Debug print
         for button in self.button_list:
          if button.is_over(*mouse_pos):
            print("Button Click Detected")  # Debug print
            button.check_action()
            return
    # ... (other code)

def draw(self):
    self.background.fill((255, 255, 255))  # White background
    self.all_sprites.draw(self.background)
    for button in self.button_list:
            button.draw(self.background)
    pygame.display.flip()




# Making the actual grid 
def draw_grid(self):
     for row in range(LEVEL_SIZE + 1):
        pygame.draw.line(self.background, (150, 150, 150), 
                         (self.start_x, self.start_y + row * TILE_SIZE), 
                         (self.start_x + LEVEL_SIZE * TILE_SIZE, self.start_y + row * TILE_SIZE))
        
     for col in range(LEVEL_SIZE + 1):
        pygame.draw.line(self.background, (150, 150, 150), 
                         (self.start_x + col * TILE_SIZE, self.start_y), 
                         (self.start_x + col * TILE_SIZE, self.start_y + LEVEL_SIZE * TILE_SIZE))
 

def update_tile_positions(self):
         for row_index, row in enumerate(self.tiles_grid):
          for col_index, tile_id in enumerate(row):
            for tile_sprite in self.all_sprites:
                if tile_sprite.id == tile_id:
                    tile_sprite.rect.topleft = (col_index * TILE_SIZE + self.start_x, row_index * TILE_SIZE + self.start_y)
                    break


def get_empty_tile_position(self):
        for y, row in enumerate(self.tiles_grid):
            for x, tile_value in enumerate(row):
                if tile_value == 0:
                    return x, y
        return None

# TileClickHandler class
class TileClickHandler:
    def __init__(self, game):
        self.game = game

    def get_blank_position(self):
        for i, row in enumerate(self.game.tiles_grid):
            if 0 in row:
                return (row.index(0), i)  # Column, Row of the blank tile



    def switch_tiles(self, pos1, pos2):
        print(f"Switching tiles: {pos1} and {pos2}")
        self.game.tiles_grid[pos1[1]][pos1[0]], self.game.tiles_grid[pos2[1]][pos2[0]] = \
            self.game.tiles_grid[pos2[1]][pos2[0]], self.game.tiles_grid[pos1[1]][pos1[0]]
        self.game.update_tile_positions()  # Update tile positions after switching




    def handle_click(self, mouse_pos):
        grid_x, grid_y = (mouse_pos[0] - self.game.start_x) // TILE_SIZE, (mouse_pos[1] - self.game.start_y) // TILE_SIZE
        grid_x, grid_y = int(grid_x), int(grid_y)
        print(f"Clicked on tile at grid position: ({grid_x}, {grid_y})")

        if 0 <= grid_x < LEVEL_SIZE and 0 <= grid_y < LEVEL_SIZE:
            blank_x, blank_y = self.get_blank_position()
            if (abs(blank_x - grid_x) == 1 and blank_y == grid_y) or (abs(blank_y - grid_y) == 1 and blank_x == grid_x):
                self.switch_tiles((grid_x, grid_y), (blank_x, blank_y))


