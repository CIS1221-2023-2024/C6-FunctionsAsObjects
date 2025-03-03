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
 
    def __init__(self):
        self.background = pygame.display.set_mode((BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.create_game()
        self.start_x = (BACKGROUND_WIDTH - LEVEL_SIZE * TILE_SIZE) // 2
        self.start_y = (BACKGROUND_HEIGHT - LEVEL_SIZE * TILE_SIZE) // 1.2
        self.draw_tiles()
        self.button_list = []
        shuffle_button_action = lambda: self.shuffle_tiles()
        self.shuffle_button = Button(self, (255, 255, 255), (0, 0, 0), BACKGROUND_WIDTH - 220, 20, 150, 50, "Shuffle", shuffle_button_action)
        self.button_list.append(self.shuffle_button)
        self.tiles_grid = self.create_game()
        self.solved_grid = self.completed_grid()
        self.game_won = False

     
    def draw_tiles(self):
         for y, row in enumerate(self.tiles_grid):
          for x, tile in enumerate(row):
            tile_text = str(tile) if tile != 0 else "empty"
            Tile(self, x, y, tile_text, tile) 

    def draw(self):
        self.background.fill((255, 255, 255))  # White background
        self.all_sprites.draw(self.background)
        self.draw_grid()
        for button in self.button_list:
            button.draw(self.background)

        if self.game_won:  # Check if the game is won
            self.show_winning_message()
        pygame.display.flip()

    def show_winning_message(self):
        font = pygame.font.SysFont("Arial", 60)
        win_text = font.render("Congrats! You have won the game!", True, (0, 0, 0))  # black text colour
        text_rect = win_text.get_rect(center=(BACKGROUND_WIDTH//2, BACKGROUND_HEIGHT//4))
        self.background.blit(win_text, text_rect)

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

     (self.start_x + LEVEL_SIZE * TILE_SIZE, self.start_y + row * TILE_SIZE)
        
     for col in range(LEVEL_SIZE + 1):
      pygame.draw.line( self.background, (150, 150, 150), 
                       (self.start_x + col * TILE_SIZE, self.start_y), 
                       (self.start_x + col * TILE_SIZE, self.start_y + LEVEL_SIZE * TILE_SIZE))
 



    def update_tile_positions(self):
         for row_index, row in enumerate(self.tiles_grid):
          for col_index, tile_id in enumerate(row):
            for tile_sprite in self.all_sprites:
                if tile_sprite.id == tile_id:
                    tile_sprite.rect.topleft = (col_index * TILE_SIZE + self.start_x, row_index * TILE_SIZE + self.start_y)
     
                    break

    def shuffle_tiles(self):
        self.game_won = False
        # Flatten the grid to a list, shuffle it, then rebuild the grid
        flat_list = [tile for row in self.tiles_grid for tile in row if tile != 0]
        random.shuffle(flat_list)

        # Rebuild the grid
        tile_counter = 0
        for i in range(LEVEL_SIZE):
            for j in range(LEVEL_SIZE):
                if self.tiles_grid[i][j] != 0:  # Avoid the empty tile
                    self.tiles_grid[i][j] = flat_list[tile_counter]
                    tile_counter += 1

        # Update tile positions
        self.update_tile_positions()      

    def completed_grid(self):
        solved = []
        number = 1
        for y in range(LEVEL_SIZE):
            row = []
            for x in range(LEVEL_SIZE):
                if number < LEVEL_SIZE * LEVEL_SIZE:
                    row.append(number)
                else:
                    row.append(0)
                number += 1
            solved.append(row)
        return solved

    def on_win(self):
        self.game_won = True

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
        self.checking_win_condition()
    
    def checking_win_condition(self):
        if self.game.tiles_grid == self.game.solved_grid:
            self.game.on_win()

    def handle_click(self, mouse_pos):
        # Check if a button was clicked
        for button in self.game.button_list:
            if button.is_over(mouse_pos[0], mouse_pos[1]):
                button.click()
                return  # No need to check the rest once we found our button

        # Handle tile click logic as before
        grid_x, grid_y = (mouse_pos[0] - self.game.start_x) // TILE_SIZE, (mouse_pos[1] - self.game.start_y) // TILE_SIZE
        grid_x, grid_y = int(grid_x), int(grid_y)
        if 0 <= grid_x < LEVEL_SIZE and 0 <= grid_y < LEVEL_SIZE:
           empty_x, empty_y = self.get_blank_position()
        # Check if the clicked tile is adjacent to the empty tile
           if (abs(grid_x - empty_x) == 1 and grid_y == empty_y) or (abs(grid_y - empty_y) == 1 and grid_x == empty_x):
            self.switch_tiles((grid_x, grid_y), (empty_x, empty_y))
