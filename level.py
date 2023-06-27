import pygame
from chronometer import Chronometer
from heart import Heart
from platforms import Platform
from player import Player
from game import Game
from general_functions import *
from button import Button
from menu_object import Menu
# from menu import *

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

        self.time = 0
        self.score = 0
        self.shot_cooldown = False
        self.game_over = False


    def update(self, enemies, portals):
        print(self.score)

        self.clock.tick(self.FPS)
        self.screen.blit(self.bg_img, (0,0))

        # Verify if the player lost a heart
        self.game_over = self.player.update(self.screen, self.platforms, enemies, self.projectiles, self.game_over, portals, self)

        self.platforms.draw(self.screen)
        self.projectiles.update(self.screen)
        self.hearts.update(self.screen, self.player)

        self.shot_cooldown = verify_shot(self.player, self.projectiles, self.shot_cooldown, self.game_over)
        verify_projectile_collision(self.projectiles, enemies, self.platforms)

        # Store level time elapsed
        self.time = self.chronometer.get_time_elapsed(self.screen)

        key_list = pygame.key.get_pressed()

        if (key_list[pygame.K_p] or key_list[pygame.K_ESCAPE]):
            pause = 0
            while pause == 0:
                exit = Level.pause_game()
                pause = 1
            return exit

    def pause_game():
        main_menu = Menu()

        RESUME_BUTTON = Button("assets/Play Rect.png",(400, 200), 
                            "Resume", font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))
        OPTIONS_BUTTON = Button("assets/Play Rect.png", (400, 300), 
                            "Options", font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))
        MAIN_MENU_BUTTON = Button("assets/Play Rect.png", (400, 400), 
                            "Level Selector", font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))

        run = True
        while run:

            button_list = [RESUME_BUTTON, OPTIONS_BUTTON, MAIN_MENU_BUTTON]

            MENU_MOUSE_POS = main_menu.update("PAUSE", 40, 400, 100, button_list)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS):
                        run = False
                        return 0
                    elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        print("opciones")
                    elif MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                        run = False
                        return 1