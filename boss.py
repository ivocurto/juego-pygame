import pygame, random
from projectile import Projectile

class Boss:
    def __init__(self, x, y):
        self.image = pygame.image.load("img/boss.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 2
        self.direction_counter = 0
        self.direction_cooldown = 0
        self.direction = 0
        self.distance = 50
        self.shot_cooldown = 50
        self.shot_counter = 0
        self.life = 20
        self.delay_counter =0
        self.delay = 75
        self.hurt_delay = 15
        self.hurt_delay_counter = 0
        self.hearts = 21

    def update(self, screen, player, projectiles):   
        #Dibujar al jefe
        screen.blit(self.image, self.rect)
        self.delay_counter += 1
        if self.delay_counter >= self.delay:
            self.delay_counter = 0
            self.image = pygame.image.load("img/boss.png")
        Boss.move(self)
        Boss.shot(self, player, projectiles)
        # Boss.hurt_with_contact(self, player)

    def move(self):
        
        if self.rect.y <= 175:
            self.direction = 0
        elif self.rect.y >= 400:
            self.direction = 1
        elif self.direction_counter >= self.distance:
            self.direction_counter = 0
            self.distance = random.randint(200, 400)
            self.direction = random.randint(0, 1)
            self.vel = random.randint(1, 3)

        match self.direction:
            case 0:
                self.rect.y += self.vel
                self.direction_counter += self.vel
            case 1:
                self.rect.y -= self.vel
                self.direction_counter += self.vel

    def shot(self, player, projectiles):
        self.shot_counter += 1
        if self.shot_counter >= self.shot_cooldown:
            self.shot_cooldown = random.randint(50, 100)
            self.shot_counter = 0
            if player.rect.x < 400:
                projectile = Projectile(self.rect.left - 15, self.rect.top + 25, -1, 2)
            elif player.rect.x >= 400:
                projectile = Projectile(self.rect.right, self.rect.top + 25, 1, 2)
            projectiles.add(projectile)

    def get_hurt(self, projectiles, data):
        if pygame.sprite.spritecollide(self, projectiles, True):
            self.image = pygame.image.load("img/boss_hurt.png")
            self.life -= 1
            self.hearts -= 1
            print(self.life)
            if self.life <= 0:
                data["score"] += 150
                return True

    def hurt_with_contact(self, player):
        self.hurt_delay_counter += 1
        if self.hurt_delay_counter > self.hurt_delay:
            if self.rect.colliderect(player.rect) and player.game_over is False:
                self.hurt_delay_counter = 0
                player.game_over = True