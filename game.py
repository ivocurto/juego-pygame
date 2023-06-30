import pygame
from config.images import BACKGROUND_IMAGE
class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_img = pygame.image.load(BACKGROUND_IMAGE)
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.exit = 0
