import pygame
from projectile import Projectile

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, direction = "left"):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.image = pygame.image.load("img/trap.png")
        if self.direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.count = 0
        self.cooldown = 100

    def update(self, screen, player, projectiles):
        #Dibujar la trampa
        screen.blit(self.image, self.rect)
        Trap.shot(self, player, projectiles)

    def get_hurt(self, projectiles, data):
        if pygame.sprite.spritecollide(self, projectiles, True):
            data["score"] = 15 + data["score"]
            self.kill()

    def shot(self, player, projectiles):
        if player.rect.bottom <= self.rect.bottom and player.rect.top >= self.rect.top:
            self.count += 1
            if self.direction == "left" and self.count >= self.cooldown:
                projectile = Projectile(self.rect.left - 15, self.rect.top + 25, -1, 10)
                projectiles.add(projectile)
            elif self.direction == "right" and self.count >= self.cooldown:
                projectile = Projectile(self.rect.right, self.rect.top + 25, 1, 10)
                projectiles.add(projectile)
