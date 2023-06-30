import pygame
from config.images import KEY
class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(KEY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, screen):
        #Dibujar la llave
        screen.blit(self.image, self.rect)
