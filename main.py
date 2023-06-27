import pygame
from pygame.locals import *
from levels import *
from menu import *

pygame.init()
pygame.mixer.music.load("assets/Sounds/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

run = True
while run:
    initial_menu()
    run = False
pygame.quit()
