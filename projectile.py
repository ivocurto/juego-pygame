import pygame
from config.images import GREEN_PROJECTILE, PINK_PROJECTILE 

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, vel, color = "pink"):
        pygame.sprite.Sprite.__init__(self)
        if color == "pink":
            self.image = pygame.image.load(PINK_PROJECTILE)
        elif color == "green":
            self.image = pygame.image.load(GREEN_PROJECTILE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction
        self.sound = pygame.mixer.Sound("assets/Sounds/laserShoot.wav")
        self.sound.set_volume(0.4)
        if direction == 1:
            self.velocity = vel
        elif direction == -1:
            self.velocity = -vel

    def update(self, screen):
        #Dibujar al proyectil
        screen.blit(self.image, self.rect)

        #Actualizar las coordenadas del proyectil
        self.rect.x += self.velocity
