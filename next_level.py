import pygame
from portal import Portal

class Next_level(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def win_level(self, player, level):
    if pygame.sprite.spritecollide(self, player, False):
        level += 1
    return level

def change_level(self, player, level):
    new_level = win_level(player, level)
    if level != new_level:
        match new_level:
            case 1:
                run_level1()
            case 2:
                run_level2()
            case 3:
                run_level3()
    return 