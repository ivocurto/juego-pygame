import pygame, json
from button import Button
from levels import *
from menu_object import Menu
from music import Music
from ranking import Ranking

def initial_menu(music):
    main_menu = Menu()

    PLAY_BUTTON = Button("assets/Play Rect.png",(400, 200), 
                        "Play", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))
    OPTIONS_BUTTON = Button("assets/Play Rect.png", (400, 300), 
                        "Options", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))
    RANKING_BUTTON = Button("assets/Play Rect.png", (400, 400), 
                        "Ranking", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))
    EXIT_BUTTON = Button("assets/Play Rect.png", (400, 500), 
                        "Exit", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))

    run = True
    while run:

        button_list = [PLAY_BUTTON, OPTIONS_BUTTON, RANKING_BUTTON, EXIT_BUTTON]

        MENU_MOUSE_POS = main_menu.update("SAVING NIDEL", 40, 400, 100, button_list)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu.exit = select_level(music)
                    if main_menu.exit == 1:
                        run = False
                        return 1
                elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu.exit = open_options_menu(music)
                    if main_menu.exit == 1:
                        run = False
                        return 1
                elif RANKING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu.exit = open_ranking_menu(music)
                    if main_menu.exit == 1:
                        run = False
                        return 1
                elif EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    run = False
                    return 1

def open_options_menu(music):
    options_menu = Menu()

    DOWN_BUTTON = Button("assets/Play Rect.png", (250, 250), 
                        "-", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (75,75))
    UP_BUTTON = Button("assets/Play Rect.png", (550, 250), 
                        "+", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (75,75))
    BACK_BUTTON = Button("assets/Play Rect.png", (400, 500), 
                        "Back", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))

    run = True
    while run:

        button_list = [DOWN_BUTTON, UP_BUTTON, BACK_BUTTON]
        music_volume_rounded = music.show_voume()
        MENU_MOUSE_POS = options_menu.update("OPTIONS", 40, 400, 100, button_list)
        title = Menu.set_title("MUSIC", 25, 400, 200)
        Menu.show_title(options_menu, title)
        title2 = Menu.set_title(f"{music_volume_rounded}", 25, 400, 250)
        Menu.show_title(options_menu, title2)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DOWN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    music.decrease_volume()
                elif UP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    music.increase_volume()
                elif BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    run = False

with open('levels.json') as file:
    dataa = json.load(file)

def select_level(music):
    level_selector = Menu()

    LVL1_BUTTON = Button("assets/Play Rect.png", (400, 200), 
                        "LVL 1", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))
    LVL2_BUTTON = Button("assets/Play Rect.png", (400, 300), 
                        "LVL 2", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))
    LVL3_BUTTON = Button("assets/Play Rect.png", (400, 400), 
                        "LVL 3", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))
    MAIN_MENU_BUTTON = Button("assets/Play Rect.png", (400, 500), 
                        "MAIN MENU", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))

    run = True
    while run:

        button_list = [LVL1_BUTTON, LVL2_BUTTON, LVL3_BUTTON, MAIN_MENU_BUTTON]

        MENU_MOUSE_POS = level_selector.update("LEVELS", 40, 400, 100, button_list)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LVL1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selector.exit = run_level1(dataa)
                    if level_selector.exit == 1:
                        run = False
                        return 1
                elif LVL2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selector.exit = run_level2(dataa)
                    if level_selector.exit == 1:
                        run = False
                        return 1
                elif LVL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selector.exit = run_level3(dataa)
                    if level_selector.exit == 1:
                        run = False
                        return 1
                elif MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selector.exit = initial_menu(music)
                    if level_selector.exit == 1:
                        run = False
                        return 1

def open_ranking_menu(music):
    level_selector = Menu()

    LVL1_BUTTON = Button("assets/Play Rect.png", (400, 200), 
                        "RANKING LVL 1", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))
    LVL2_BUTTON = Button("assets/Play Rect.png", (400, 300), 
                        "RANKING LVL 2", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))
    LVL3_BUTTON = Button("assets/Play Rect.png", (400, 400), 
                        "RANKING LVL 3", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))
    MAIN_MENU_BUTTON = Button("assets/Play Rect.png", (400, 500), 
                        "MAIN MENU", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))

    run = True
    while run:

        button_list = [LVL1_BUTTON, LVL2_BUTTON, LVL3_BUTTON, MAIN_MENU_BUTTON]

        MENU_MOUSE_POS = level_selector.update("RANKINGS", 40, 400, 100, button_list)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LVL1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selector.exit = open_ranking_lvl_menu(1)
                    if level_selector.exit == 1:
                        run = False
                        return 1
                elif LVL2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selector.exit = open_ranking_lvl_menu(2)
                    if level_selector.exit == 1:
                        run = False
                        return 1
                elif LVL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selector.exit = open_ranking_lvl_menu(3)
                    if level_selector.exit == 1:
                        run = False
                        return 1
                elif MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selector.exit = initial_menu(music)
                    if level_selector.exit == 1:
                        run = False
                        return 1

def open_ranking_lvl_menu(lvl):
    ranking1 = Menu()

    BACK_BUTTON = Button("assets/Play Rect.png", (400, 500), 
                        "BACK", font_size= 25, base_color=((255, 255, 0)),
                        hovering_color=(255, 255, 255), size= (400,75))

    run = True
    while run:

        button_list = [BACK_BUTTON]

        MENU_MOUSE_POS = ranking1.update("RANKING", 40, 400, 100, button_list)
        top5 = Ranking.show_top5_list(lvl)
        pos_y = 150
        try:
            for player in top5:
                pos_y += 50
                title = Menu.set_title(f"{player['name']} - {player['score']}", 25, 400, pos_y)
                Menu.show_title(ranking1, title)
        except:
            title = Menu.set_title("Undefined - Undefined", 25, 400, 200)
            Menu.show_title(ranking1, title)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    run = False
                    return 0