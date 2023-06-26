import pygame
from chronometer import Chronometer
from heart import Heart
from platforms import Platform
from player import Player
from game import Game

class Level(Game):
    def __init__(self, dictionary):
        super().__init__()
        #Player
        self.player = Player(dictionary["player"]["x"], dictionary["player"]["y"])

        #Chronometer
        self.chronometer = Chronometer()
        self.chronometer.init_chronometer()

        #Hearts
        self.hearts = pygame.sprite.Group()
        for dict in dictionary["hearts"]:
            heart = Heart(dict["x"], dict["y"], dict["num"])
            self.hearts.add(heart)

        #Platforms
        self.platforms = pygame.sprite.Group()
        for dict in dictionary["platforms"]:
            platform = Platform(dict["path"], dict["x"], dict["y"], dict["width"], dict["height"])
            self.platforms.add(platform)

        #Projectiles
        self.projectiles = pygame.sprite.Group()

        self.data = {"level": 0, "score": 0, "time": 0}
        self.shot_cooldown = False
        self.game_over = False

    # def upate(self):
    #     level1.clock.tick(level1.FPS) # IGUAL EN TODOS
    #     level1.screen.blit(level1.bg_img, (0,0)) # IGUAL EN TODOS

