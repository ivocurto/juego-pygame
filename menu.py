import pygame, json
from button import Button
from levels import *
from menu_object import Menu

def initial_menu():
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
                    main_menu.exit = select_level()
                    if main_menu.exit == 1:
                        run = False
                        return 1
                elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("opciones")
                elif RANKING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("ranking")
                elif EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    run = False
                    return 1

with open('levels.json') as file:
    dataa = json.load(file)

def select_level():
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
                    level_selector.exit = initial_menu()
                    if level_selector.exit == 1:
                        run = False
                        return 1
