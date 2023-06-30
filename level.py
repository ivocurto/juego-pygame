import pygame
from chronometer import Chronometer
from heart import Heart
from platforms import Platform
from player import Player
from game import Game
from general_functions import *
from button import Button
from menu_object import Menu
from ranking import Ranking
from history import History
from config.images import *

class Level(Game):
    def __init__(self, dictionary):
        super().__init__()
        #Player
        self.player = Player(dictionary["player"]["x"], dictionary["player"]["y"])
        self.level_number = dictionary["level_number"]

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

        self.clock.tick(self.FPS)
        self.screen.blit(self.bg_img, (0,0))

        # Verify if the player lost a heart
        self.game_over = self.player.update(self.screen, self.platforms, enemies, self.projectiles, self.game_over, portals, self)

        self.platforms.draw(self.screen)
        self.projectiles.update(self.screen)
        self.hearts.update(self.screen, self.player)

        self.shot_cooldown = verify_shot(self.player, self.projectiles, self.shot_cooldown, self.game_over)
        verify_projectile_collision(self.projectiles, enemies, self.platforms)


        key_list = pygame.key.get_pressed()

        self.print_score()

        # Store level time elapsed
        self.time = self.chronometer.get_time_elapsed(self.screen)

        if (key_list[pygame.K_p] or key_list[pygame.K_ESCAPE]):
            pause = 0
            while pause == 0:
                exit = Level.pause_game()
                pause = 1
            self.chronometer.initial_time = pygame.time.get_ticks()
            return exit

    def print_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Score: {}".format(self.score), True, (255,255,255))
        self.screen.blit(text, (650, 550))

    def pause_game():
        pause_menu = Menu()

        RESUME_BUTTON = Button("assets/Play Rect.png",(400, 200), 
                            "Resume", font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))
        CONTROLS_BUTTON = Button("assets/Play Rect.png", (400, 300), 
                            "Controls", font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))
        MAIN_MENU_BUTTON = Button("assets/Play Rect.png", (400, 400), 
                            "Level Selector", font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))

        run = True
        while run:

            button_list = [RESUME_BUTTON, MAIN_MENU_BUTTON, CONTROLS_BUTTON]

            MENU_MOUSE_POS = pause_menu.update("PAUSE", 40, 400, 100, button_list)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS):
                        run = False
                        return 0
                    elif CONTROLS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        history = History(CONTROLS)
                        history = history.update()
                        if history == 1:
                            run = False
                    elif MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                        run = False
                        return 1

    def check_if_win_or_lose(self, win_level):
        if self.player.hearts == 1 or exit == 1 or self.time == 60:
            self.score = 0
            win_lose_menu("YOU LOSE", self.score)
            return -1
        if win_level:
            self.score += 60 - self.time
            name = open_insert_name_menu()
            if isinstance(name, str):
                Ranking(name, self.score, self.level_number)
            win_lose_menu("YOU WIN", self.score)
            return -1

def win_lose_menu(state, score):
    win_lose_menu = Menu()

    OK_BUTTON = Button("assets/Play Rect.png",(400, 450), 
                        "OK", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))

    run = True
    while run:

        button_list = [OK_BUTTON]

        MENU_MOUSE_POS = win_lose_menu.update(state, 40, 400, 100, button_list)
        title = Menu.set_title(f"Score: {score}", 40, 400, 300)
        Menu.show_title(win_lose_menu, title)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    run = False

def open_insert_name_menu():
    insert_name_menu = Menu()

    SUMBIT_BUTTON = Button("assets/Play Rect.png", (400, 500), 
                        "SUMBIT", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))

    font = pygame.font.Font(None, 36)

    name = ""
    text = font.render(name, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (325, 300)
    scaled_rect = pygame.Rect(0,0, 200, 50)
    scaled_rect.center = (400, 300)

    run = True
    while run:
        button_list = [SUMBIT_BUTTON]

        MENU_MOUSE_POS = insert_name_menu.update("Name:", 40, 400, 100, button_list)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    reproduce_something("assets\Sounds\select_option.wav", 0.4)
                    name = name[:-1]  # Remove the last character
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    run = False
                    return name
                else:
                    if len(name) < 11:
                        reproduce_something("assets\Sounds\select_option.wav", 0.4)
                        name += event.unicode  # Add the typed character
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if SUMBIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    run = False
                    return name
            # Update the rendered text
            text = font.render(name, True, (255, 255, 255))
            pygame.draw.rect(insert_name_menu.screen, (255,255,255), scaled_rect, 5, -1)

            insert_name_menu.screen.blit(text, text_rect)
            pygame.display.flip()
