import pygame
from pygame.locals import *
from levels import *
from menu import *
from music import Music
from config.music import *

pygame.init()
music = Music(MENU_MUSIC, 0.3)

run = True
while run:
    initial_menu(music)
    run = False
pygame.quit()
