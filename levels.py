import pygame
from pygame.locals import *
from player import Player
from enemy import Enemy
from portal import Portal
from general_functions import *
from platforms import Platform
from key import Key
from boss import Boss
from heart import Heart
from trap import Trap
from chronometer import Chronometer
from menu_object import Menu
from level import Level

def run_level1(dataa):
    level_data = Level(dataa[0])

    #TEMPORIZADOR CREADOR DE ENEMIGOS
    pygame.time.set_timer(pygame.USEREVENT, 7000)

    #Traps
    traps = pygame.sprite.Group()
    trap_left = Trap(25, 475, "right")
    trap_right = Trap(750, 50, "left")
    traps.add(trap_left, trap_right)

    #Portals
    portals = pygame.sprite.Group()
    portal_left_bottom = Portal("img/platforms/portal_horizontal.png", 25, 400, 100, 25)
    portal_left_top = Portal("img/platforms/portal_horizontal.png", 25, 0, 100, 25)
    portal_right_bottom = Portal("img/platforms/portal_horizontal.png", 675, 400, 100, 25)
    portal_right_top = Portal("img/platforms/portal_horizontal.png", 675, 0, 100, 25)
    portal_center_bottom = Portal("img/platforms/portal_horizontal.png", 325, 575, 150, 25)
    portal_center_top = Portal("img/platforms/portal_horizontal.png", 325, 275, 150, 25)
    portals.add(portal_left_bottom, portal_left_top, portal_right_bottom, portal_right_top, portal_center_bottom, portal_center_top)

    #Keys
    keys = pygame.sprite.Group()
    key_left_top = Key(60, 70)
    key_right_top = Key(710, 70)
    key_left_bottom = Key(60, 510)
    key_right_bottom = Key(710, 510)
    keys.add(key_left_top, key_right_top, key_left_bottom, key_right_bottom)

    #Entities
    enemy = Enemy(150, 40)
    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    run = True
    print(level_data.data)
    while run:
        print(level_data.data["score"])
        level_data.clock.tick(level_data.FPS) # IGUAL EN TODOS
        level_data.screen.blit(level_data.bg_img, (0,0)) # IGUAL EN TODOS

        level_data.platforms.draw(level_data.screen) # IGUAL EN TODOS

        level_data.shot_cooldown = verify_shot(level_data.player, level_data.projectiles, level_data.shot_cooldown, level_data.game_over) # IGUAL EN TODOS
        level_data.game_over = level_data.player.update(level_data.screen, level_data.platforms, enemies, level_data.projectiles, level_data.game_over, portals, level_data.data) # IGUAL EN TODOS
        enemies.update(level_data.screen, level_data.platforms, portals)
        level_data.projectiles.update(level_data.screen) # IGUAL EN TODOS
        portal_left_bottom.teleport(level_data.screen, level_data.projectiles, portal_left_top, level_data.player, "horizontal")
        portal_right_bottom.teleport(level_data.screen, level_data.projectiles, portal_right_top, level_data.player, "horizontal")
        portal_center_bottom.teleport(level_data.screen, level_data.projectiles, portal_center_top, level_data.player, "horizontal")
        keys.update(level_data.screen)
        if len(traps) > 0:
            trap_left.get_hurt(level_data.projectiles, level_data.data)
            trap_right.get_hurt(level_data.projectiles, level_data.data)
            traps.update(level_data.screen, level_data.player, level_data.projectiles)
        level_data.hearts.update(level_data.screen, level_data.player) # IGUAL EN TODOS
        win_level = level_data.player.get_keys(keys, 4)
        if level_data.player.hearts == 1:
            run = False
            return level_data.data
        if win_level: # IGUAL EN TODOS
            level_data.data["score"] += 60 - level_data.data["time"]
            level_data.data["level"] += 1
            run = False
            return level_data.data
        verify_projectile_collision(level_data.projectiles, enemies, level_data.platforms) # IGUAL EN TODOS

        level_data.data["time"] = level_data.chronometer.get_time_elapsed(level_data.screen, level_data.data) # IGUAL EN TODOS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            elif event.type == pygame.USEREVENT:
                generate_enemy(enemies, 150, 40, 550, 40)

        pygame.display.update()

def run_level2(dataa):
    level_data = Level(dataa[1])

    #TEMPORIZADOR CREADOR DE ENEMIGOS
    pygame.time.set_timer(pygame.USEREVENT, 7000)

    #Traps
    traps = pygame.sprite.Group()
    trap1 = Trap(25, 50, "right")
    traps.add(trap1)

    #Portals
    portals = pygame.sprite.Group()
    portal_left_bottom = Portal("img/platforms/portal_vertical.png", 275, 475, 25, 100)
    portal_right_bottom = Portal("img/platforms/portal_vertical.png", 775, 475, 25, 100)
    portal_left1 = Portal("img/platforms/portal_horizontal.png", 25, 150, 100, 25)
    portal_left2 = Portal("img/platforms/portal_horizontal.png", 25, 450, 100, 25)
    portal_right1 = Portal("img/platforms/portal_horizontal.png", 150, 425, 100, 25)
    portal_right2 = Portal("img/platforms/portal_horizontal.png", 150, 0, 100, 25)
    portals.add(portal_left_bottom, portal_right_bottom, portal_left1, portal_left2, portal_right1, portal_right2)

    #Keys
    keys = pygame.sprite.Group()
    key_left_top = Key(180, 70)
    key_left_bottom = Key(180, 510)
    key_right_bottom = Key(710, 510)
    keys.add(key_left_top, key_left_bottom, key_right_bottom)

    #Entities
    enemy = Enemy(340, 40)
    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    run = True
    while run:
        print(level_data.data["score"])
        level_data.clock.tick(level_data.FPS)
        level_data.screen.blit(level_data.bg_img, (0,0))

        level_data.platforms.draw(level_data.screen)

        level_data.shot_cooldown = verify_shot(level_data.player, level_data.projectiles, level_data.shot_cooldown, level_data.game_over)
        level_data.game_over = level_data.player.update(level_data.screen, level_data.platforms, enemies, level_data.projectiles, level_data.game_over, portals, level_data.data)
        enemies.update(level_data.screen, level_data.platforms, portals)
        level_data.projectiles.update(level_data.screen)
        portal_left_bottom.teleport(level_data.screen, level_data.projectiles, portal_right_bottom, level_data.player, "vertical")
        portal_left1.teleport(level_data.screen, level_data.projectiles, portal_left2, level_data.player, "horizontal")
        portal_right1.teleport(level_data.screen, level_data.projectiles, portal_right2, level_data.player, "horizontal")
        keys.update(level_data.screen)
        win_level = level_data.player.get_keys(keys, 3)
        if len(traps) > 0:
            trap1.get_hurt(level_data.projectiles, level_data.data)
            traps.update(level_data.screen, level_data.player, level_data.projectiles)
        level_data.hearts.update(level_data.screen, level_data.player)
        if level_data.player.hearts == 1:
            run = False
            return level_data.data
        if win_level:
            level_data.data["level"] += 1
            level_data.data["score"] += 60 - level_data.data["time"]
            run = False
            return level_data.data
        verify_projectile_collision(level_data.projectiles, enemies, level_data.platforms)


        level_data.data["time"] = level_data.chronometer.get_time_elapsed(level_data.screen, level_data.data)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            elif event.type == pygame.USEREVENT:
                generate_enemy(enemies, 375, 40, 660, 40)

        pygame.display.update()

def run_level3(dataa):
    level_data = Level(dataa[2])

    #HeartsBoss
    boss_hearts = pygame.sprite.Group()
    boss_heart1 = Heart(370, 30, 1, "Purple")
    boss_heart2 = Heart(410, 30, 2, "Purple")
    boss_heart3 = Heart(450, 30, 3, "Purple")
    boss_heart4 = Heart(490, 30, 4, "Purple")
    boss_heart5 = Heart(530, 30, 5, "Purple")
    boss_heart6 = Heart(570, 30, 6, "Purple")
    boss_heart7 = Heart(610, 30, 7, "Purple")
    boss_heart8 = Heart(650, 30, 8, "Purple")
    boss_heart9 = Heart(690, 30, 9, "Purple")
    boss_heart10 = Heart(730, 30, 10, "Purple")
    boss_heart11 = Heart(370, 70, 11, "Purple")
    boss_heart12 = Heart(410, 70, 12, "Purple")
    boss_heart13 = Heart(450, 70, 13, "Purple")
    boss_heart14 = Heart(490, 70, 14, "Purple")
    boss_heart15 = Heart(530, 70, 15, "Purple")
    boss_heart16 = Heart(570, 70, 16, "Purple")
    boss_heart17 = Heart(610, 70, 17, "Purple")
    boss_heart18 = Heart(650, 70, 18, "Purple")
    boss_heart19 = Heart(690, 70, 19, "Purple")
    boss_heart20 = Heart(730, 70, 20, "Purple")
    boss_hearts.add(boss_heart1, boss_heart2, boss_heart3, boss_heart4, boss_heart5,
                    boss_heart6, boss_heart7, boss_heart8, boss_heart9, boss_heart10,
                    boss_heart11, boss_heart12, boss_heart13, boss_heart14, boss_heart15,
                    boss_heart16, boss_heart17, boss_heart18, boss_heart19, boss_heart20)

    #Portals
    portals = pygame.sprite.Group()
    portal_bottom = Portal("img/platforms/portal_horizontal.png", 25, 575, 750, 25)
    portal_top = Portal("img/platforms/portal_horizontal.png", 25, 0, 750, 25)
    portals.add(portal_bottom, portal_top)

    #Entities
    boss = Boss(300, 250)
    enemies = pygame.sprite.Group()
    enemies.add()

    run = True
    while run:
        print(level_data.data["score"])
        level_data.clock.tick(level_data.FPS)
        level_data.screen.blit(level_data.bg_img, (0,0))

        level_data.platforms.draw(level_data.screen)

        level_data.shot_cooldown = verify_shot(level_data.player, level_data.projectiles, level_data.shot_cooldown, level_data.game_over)
        level_data.game_over = level_data.player.update(level_data.screen, level_data.platforms, enemies, level_data.projectiles, level_data.game_over, portals, level_data.data)
        enemies.update(level_data.screen, level_data.platforms, portals)
        level_data.projectiles.update(level_data.screen)
        portal_bottom.teleport(level_data.screen, level_data.projectiles, portal_top, level_data.player, "horizontal")
        boss.update(level_data.screen, level_data.player, level_data.projectiles)
        win_level = boss.get_hurt(level_data.projectiles, level_data.data)
        boss_hearts.update(level_data.screen, boss)
        level_data.hearts.update(level_data.screen, level_data.player)
        level_data.data["time"] = level_data.chronometer.get_time_elapsed(level_data.screen, level_data.data)
        if level_data.player.hearts == 1:
            run = False
            return level_data.data
        if win_level:
            level_data.data["level"] += 1
            run = False
            level_data.data["score"] += 60 - level_data.data["time"]
            return level_data.data
        verify_projectile_collision(level_data.projectiles, enemies, level_data.platforms)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1

        pygame.display.update()
