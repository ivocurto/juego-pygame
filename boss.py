import pygame, random
from projectile import Projectile
from config.images import BOSS, BOSS_HURT

class Boss:
    def __init__(self, x, y):
        self.image = pygame.image.load(BOSS)
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
        self.delay = 30
        self.hearts = 21
        self.sound_hurt = pygame.mixer.Sound("assets\Sounds\hurt_boss.wav")
        self.sound_hurt.set_volume(0.4)

    def update(self, screen, player, projectiles):   
        #Dibujar al jefe
        screen.blit(self.image, self.rect)
        self.delay_counter += 1
        if self.delay_counter >= self.delay:
            self.delay_counter = 0
            self.image = pygame.image.load(BOSS)
        Boss.move(self)
        Boss.shot(self, player, projectiles)

    def move(self):
        
        if self.rect.y <= 200:
            self.direction = 0
        elif self.rect.y >= 300:
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
            self.shot_cooldown = random.randint(40, 65)
            self.shot_counter = 0
            if player.rect.x < 400:
                projectile = Projectile(self.rect.left - 16, self.rect.top + 75, -1, 4, "green")
            elif player.rect.x >= 400:
                projectile = Projectile(self.rect.right + 2, self.rect.top + 75, 1, 4, "green")
            projectiles.add(projectile)

    def get_hurt(self, projectiles, level):
        if pygame.sprite.spritecollide(self, projectiles, True):
            self.image = pygame.image.load(BOSS_HURT)
            self.sound_hurt.play()
            self.life -= 1
            self.hearts -= 1
            if self.life <= 0:
                level.score += 150
                return True
