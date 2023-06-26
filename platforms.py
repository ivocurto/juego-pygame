import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen, platform_list):
        for platform in platform_list:
            screen.blit(platform.image, platform.rect)
