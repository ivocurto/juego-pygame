import pygame
from projectile import Projectile
from config.images import TRAP

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, direction = "left"):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.image = pygame.image.load(TRAP)
        if self.direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.count = 0
        self.cooldown = 50
        self.sound_death = pygame.mixer.Sound("assets\Sounds\explosion.wav")
        self.sound_death.set_volume(0.4)

    def update(self, screen, player, projectiles):
        #Dibujar la trampa
        screen.blit(self.image, self.rect)
        Trap.shot(self, player, projectiles)

    def get_hurt(self, traps, projectiles, level):
        for trap in traps:
            if pygame.sprite.spritecollide(trap, projectiles, True):
                level.score = 15 + level.score
                trap.sound_death.play()
                traps.remove(trap)

    def shot(self, player, projectiles):
        if player.rect.bottom <= self.rect.bottom and player.rect.top >= self.rect.top:
            self.count += 1
            if self.direction == "left" and self.count >= self.cooldown:
                projectile = Projectile(self.rect.left - 15, self.rect.top + 42, -1, 10)
                projectiles.add(projectile)
            elif self.direction == "right" and self.count >= self.cooldown:
                projectile = Projectile(self.rect.right, self.rect.top + 42, 1, 10)
                projectiles.add(projectile)
        if player.rect.colliderect(self.rect):
            player.game_over = True
            self.kill()
            self.sound_death.play()
