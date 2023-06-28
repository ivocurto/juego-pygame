import pygame
from pygame.locals import *
from levels import *
from menu import *
from music import Music

pygame.init()
music = Music("assets/Sounds/music.mp3", 0.1)
run = True
while run:
    initial_menu(music)
    run = False
pygame.quit()
