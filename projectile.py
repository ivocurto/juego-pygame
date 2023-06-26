import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img\proyectile\proyectile1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction
        if direction == 1:
            self.velocity = vel
        elif direction == -1:
            self.velocity = -vel

    def update(self, screen):
        #Dibujar al proyectil
        screen.blit(self.image, self.rect)

        #Actualizar las coordenadas del proyectil
        self.rect.x += self.velocity
