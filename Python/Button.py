
import pygame
import random 
pygame.init()

from grid import *


class UIElement:
    def Anst (self, x, y, text):
       self.x, self.y = x, y
       self.text = text
  

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 50)
        text_render = font.render(self.text, True, (255, 255, 255))
        screen.blit(text_render, (self.x, self.y))

    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    

class Button:
    def __init__(self, game, colour, outline, x, y, width, height, text, action =None):
        self.game = game
        self.colour, self.outline = colour, outline
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.text = text
        self.action = action

    def draw(self, screen):
        # Draw the button outline
        pygame.draw.rect(screen, self.outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
        # Draw the button itself
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        # Render the text on the button
        font = pygame.font.SysFont("Arial", 30)
        text = font.render(self.text, True, (255, 255, 255))  # White text color
        draw_x = self.x + (self.width / 2 - text.get_width() / 2)
        draw_y = self.y + (self.height / 2 - text.get_height() / 2)
        screen.blit(text, (draw_x, draw_y))
        font = pygame.font.SysFont("Consolas", 20)
        text_surface = font.render(self.text, True, ( 0, 0 , 0))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

    def is_over(self, mouse_x, mouse_y):
         return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
    
    def click(self):
        if self.action:
             self.action()
