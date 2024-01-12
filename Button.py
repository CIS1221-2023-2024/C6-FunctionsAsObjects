import pygame
pygame.init()

class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 50)
        text = font.render(self.text, True, (255, 255, 255))
        screen.blit(text, (self.x, self.y))

class Button:
    def __init__(self, game, colour, outline, x, y, width, height, text):
        self.game = game
        self.colour, self.outline = colour, outline
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Consolas", 20)
        text_surface = font.render(self.text, True, ( 0, 0 , 0))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

    def is_over(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
