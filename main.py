import pygame
from pygame.locals import *
from levels import *
from menu import *

pygame.init()

run = True
while run:
    initial_menu()
    run = False
pygame.quit()