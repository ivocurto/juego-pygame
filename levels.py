import pygame
from pygame.locals import *
from enemy import Enemy
from portal import Portal
from general_functions import *
from key import Key
from boss import Boss
from heart import Heart
from trap import Trap
from level import Level
from music import Music
from history import History
from config.images import *
from config.colors import *


def run_level1(dataa, music):
    data_lvl_1 = dataa[0]
    Music(data_lvl_1["music_path"], music.volume)
    history = History(LVL_1_HISTORY)
    history = history.update()
    if history == 1:
        return -1
    history = History(LVL_1_HISTORY2)
    history = history.update()
    if history == 1:
        return -1
    level_data = Level(data_lvl_1)

    #TEMPORIZADOR CREADOR DE ENEMIGOS
    pygame.time.set_timer(pygame.USEREVENT, 4000)

    #Traps
    traps = pygame.sprite.Group()
    trap1 = Trap(25, 180, "right")
    traps.add(trap1)

    #Portals
    portals = pygame.sprite.Group()
    portal_left_bottom = Portal(WALL_IMG, 275, 475, 25, 100)
    portal_right_bottom = Portal(WALL_IMG, 775, 475, 25, 100)
    portal_left1 = Portal(PLATFORM_IMG, 25, 150, 100, 25)
    portal_left2 = Portal(PLATFORM_IMG, 25, 450, 100, 25)
    portal_right1 = Portal(PLATFORM_IMG, 150, 425, 100, 25)
    portal_right2 = Portal(PLATFORM_IMG, 150, 0, 100, 25)
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

        exit = level_data.update(enemies, portals)
        enemies.update(level_data.screen, level_data.platforms, portals)
        portal_left_bottom.teleport(level_data.screen, level_data.projectiles, portal_right_bottom, level_data.player, "vertical")
        portal_left1.teleport(level_data.screen, level_data.projectiles, portal_left2, level_data.player, "horizontal")
        portal_right1.teleport(level_data.screen, level_data.projectiles, portal_right2, level_data.player, "horizontal")
        keys.update(level_data.screen)
        win_level = level_data.player.get_keys(keys, 3, level_data)
        if len(traps) > 0:
            trap1.get_hurt(traps, level_data.projectiles, level_data)
            traps.update(level_data.screen, level_data.player, level_data.projectiles)
        level_data.hearts.update(level_data.screen, level_data.player)

        final = level_data.check_if_win_or_lose(win_level)
        if final == -1 or exit == 1:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return -1
            elif event.type == pygame.USEREVENT:
                generate_enemy(enemies, 375, 40, 660, 40)

        pygame.display.update()

def run_level2(dataa, music):
    data_lvl_2 = dataa[1]
    level_data = Level(data_lvl_2)
    Music(data_lvl_2["music_path"], music.volume)
    history = History(LVL_2_HISTORY)
    history = history.update()
    if history == 1:
        return -1

    #TEMPORIZADOR CREADOR DE ENEMIGOS
    pygame.time.set_timer(pygame.USEREVENT, 4000)

    #Traps
    traps = pygame.sprite.Group()
    trap_left = Trap(25, 475, "right")
    trap_right = Trap(750, 50, "left")
    traps.add(trap_left, trap_right)

    #Portals
    portals = pygame.sprite.Group()
    portal_left_bottom = Portal(HORIZONTAL_PORTAL_IMG, 25, 400, 100, 25)
    portal_left_top = Portal(HORIZONTAL_PORTAL_IMG, 25, 0, 100, 25)
    portal_right_bottom = Portal(HORIZONTAL_PORTAL_IMG, 675, 400, 100, 25)
    portal_right_top = Portal(HORIZONTAL_PORTAL_IMG, 675, 0, 100, 25)
    portal_center_bottom = Portal(HORIZONTAL_PORTAL_IMG, 325, 575, 150, 25)
    portal_center_top = Portal(HORIZONTAL_PORTAL_IMG, 325, 275, 150, 25)
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
    while run:

        exit = level_data.update(enemies, portals)

        enemies.update(level_data.screen, level_data.platforms, portals)
        portal_left_bottom.teleport(level_data.screen, level_data.projectiles, portal_left_top, level_data.player, "horizontal")
        portal_right_bottom.teleport(level_data.screen, level_data.projectiles, portal_right_top, level_data.player, "horizontal")
        portal_center_bottom.teleport(level_data.screen, level_data.projectiles, portal_center_top, level_data.player, "horizontal")
        keys.update(level_data.screen)
        if len(traps) > 0:
            trap_left.get_hurt(traps, level_data.projectiles, level_data)
            trap_right.get_hurt(traps, level_data.projectiles, level_data)
            traps.update(level_data.screen, level_data.player, level_data.projectiles)

        win_level = level_data.player.get_keys(keys, 4, level_data)

        final = level_data.check_if_win_or_lose(win_level)
        if final == -1 or exit == 1:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return -1
            elif event.type == pygame.USEREVENT:
                generate_enemy(enemies, 150, 40, 550, 40)

        pygame.display.update()

def run_level3(dataa, music):
    data_lvl_3 = dataa[2]
    Music(data_lvl_3["music_path"], music.volume)
    history = History(LVL_3_HISTORY)
    history = history.update()
    if history == 1:
        return -1
    level_data = Level(data_lvl_3)

    #Boss Hearts
    boss_hearts = pygame.sprite.Group()
    boss_heart1 = Heart(370, 30, 1, PURPLE)
    boss_heart2 = Heart(410, 30, 2, PURPLE)
    boss_heart3 = Heart(450, 30, 3, PURPLE)
    boss_heart4 = Heart(490, 30, 4, PURPLE)
    boss_heart5 = Heart(530, 30, 5, PURPLE)
    boss_heart6 = Heart(570, 30, 6, PURPLE)
    boss_heart7 = Heart(610, 30, 7, PURPLE)
    boss_heart8 = Heart(650, 30, 8, PURPLE)
    boss_heart9 = Heart(690, 30, 9, PURPLE)
    boss_heart10 = Heart(730, 30, 10, PURPLE)
    boss_heart11 = Heart(370, 70, 11, PURPLE)
    boss_heart12 = Heart(410, 70, 12, PURPLE)
    boss_heart13 = Heart(450, 70, 13, PURPLE)
    boss_heart14 = Heart(490, 70, 14, PURPLE)
    boss_heart15 = Heart(530, 70, 15, PURPLE)
    boss_heart16 = Heart(570, 70, 16, PURPLE)
    boss_heart17 = Heart(610, 70, 17, PURPLE)
    boss_heart18 = Heart(650, 70, 18, PURPLE)
    boss_heart19 = Heart(690, 70, 19, PURPLE)
    boss_heart20 = Heart(730, 70, 20, PURPLE)
    boss_hearts.add(boss_heart1, boss_heart2, boss_heart3, boss_heart4, boss_heart5,
                    boss_heart6, boss_heart7, boss_heart8, boss_heart9, boss_heart10,
                    boss_heart11, boss_heart12, boss_heart13, boss_heart14, boss_heart15,
                    boss_heart16, boss_heart17, boss_heart18, boss_heart19, boss_heart20)

    #Portals
    portals = pygame.sprite.Group()
    portal_bottom = Portal(HORIZONTAL_PORTAL_IMG, 25, 575, 750, 25)
    portal_top = Portal(HORIZONTAL_PORTAL_IMG, 25, 0, 750, 25)
    portals.add(portal_bottom, portal_top)

    #Entities
    boss = Boss(300, 250)
    enemies = pygame.sprite.Group()
    enemies.add()

    run = True
    while run:
        exit = level_data.update(enemies, portals)

        enemies.update(level_data.screen, level_data.platforms, portals)

        portal_bottom.teleport(level_data.screen, level_data.projectiles, portal_top, level_data.player, "horizontal")
        boss.update(level_data.screen, level_data.player, level_data.projectiles)
        win_level = boss.get_hurt(level_data.projectiles, level_data)
        boss_hearts.update(level_data.screen, boss)

        if win_level:
            history = History(WIN_HISTORY)
            history = history.update()
            if history == 1:
                return -1
        final = level_data.check_if_win_or_lose(win_level)
        if final == -1 or exit == 1:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return -1

        pygame.display.update()
