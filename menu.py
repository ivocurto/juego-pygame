import pygame, sys, json
from button import Button
from levels import *
from menu_object import Menu

def initial_menu():
    main_menu = Menu()
    run = True
    while run:

        text = "Play"
        PLAY_BUTTON = Button("assets/Play Rect.png",(400, 200), 
                            text, font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))
        text2 = "Options"
        OPTIONS_BUTTON = Button("assets/Play Rect.png", (400, 300), 
                            text2, font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))
        text3 = "Ranking"
        RANKING_BUTTON = Button("assets/Play Rect.png", (400, 400), 
                            text3, font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))
        text4 = "Exit"
        EXIT_BUTTON = Button("assets/Play Rect.png", (400, 500), 
                            text4, font_size= 25, base_color=((255, 255, 0)),
                            hovering_color=(255, 255, 255), size= (400,75))

        button_list = [PLAY_BUTTON, OPTIONS_BUTTON, RANKING_BUTTON, EXIT_BUTTON]

        MENU_MOUSE_POS = main_menu.update("SAVING NIDEL", 40, 400, 100, button_list)

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
    level_selctor = Menu()
    run = True
    while run:

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

        button_list = [LVL1_BUTTON, LVL2_BUTTON, LVL3_BUTTON, MAIN_MENU_BUTTON]

        MENU_MOUSE_POS = level_selctor.update("LEVELS", 40, 400, 100, button_list)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LVL1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selctor.exit = run_level1(dataa)
                    if level_selctor.exit == 1:
                        run = False
                        return 1
                elif LVL2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selctor.exit = run_level2(dataa)
                    if level_selctor.exit == 1:
                        run = False
                        return 1
                elif LVL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selctor.exit = run_level3(dataa)
                    if level_selctor.exit == 1:
                        run = False
                        return 1
                elif MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_selctor.exit = initial_menu()
                    if level_selctor.exit == 1:
                        run = False
                        return 1
