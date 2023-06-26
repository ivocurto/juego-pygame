import pygame
class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_img = pygame.image.load('img/background.jpg')
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.exit = 0