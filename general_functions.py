import pygame, random
from enemy import Enemy
from projectile import Projectile

def verify_shot(player, projectiles, shot_cooldown, game_over):
    if not game_over:
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_SPACE] and shot_cooldown == False:
            if player.direction == -1:
                projectile = Projectile(player.rect.left - 15, player.rect.top + 25, -1, 5)
            elif player.direction == 1:
                projectile = Projectile(player.rect.right, player.rect.top + 25, 1, 5)
            projectile.sound.play()
            projectiles.add(projectile)
            shot_cooldown = True
        if not key_list[pygame.K_SPACE]:
            shot_cooldown = False

        return shot_cooldown

def verify_projectile_collision(projectiles, enemies, platform_list):
    pygame.sprite.groupcollide(projectiles, platform_list, True, False)
    for enemy in pygame.sprite.groupcollide(enemies, projectiles, True, True):
        enemy.sound_death.play()

def generate_enemy(enemies, x, y, x2, y2):
    print("enemigo creado")
    random_x = random.randint(0,1)
    match random_x:
        case 0:
            enemy = Enemy(x, y)
        case 1:
            enemy = Enemy(x2, y2)
            enemy.direction = -1
    enemies.add(enemy)