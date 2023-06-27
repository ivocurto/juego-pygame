import pygame
from game import Game
class Menu(Game):
    def __init__(self):
        super().__init__()

    def get_font(letter_size:int):
        return pygame.font.Font("assets/font.ttf", letter_size)

    def update(self, title:str, letter_size:int, pos_x:int, pos_y:int, button_list):
        self.screen.blit(self.bg_img, (0,0))
        title = Menu.set_title(title, letter_size, pos_x, pos_y)
        menu_mouse_pos = Menu.get_position(self)
        Menu.pass_mouse(self, button_list, menu_mouse_pos)
        Menu.show_title(self, title)
        return menu_mouse_pos

    def get_position(self):
        menu_mouse_pos = pygame.mouse.get_pos()
        return menu_mouse_pos

    def set_title(title:str, letter_size:int, pos_x:int, pos_y:int):
        TITLE_TEXT = Menu.get_font(letter_size).render(title, True, "#ffffff")
        TITLE_RECT = TITLE_TEXT.get_rect(center=(pos_x, pos_y))
        TITLE = [TITLE_TEXT, TITLE_RECT]
        return TITLE

    def show_title(self, title):
        self.screen.blit(title[0], title[1])

    def pass_mouse(self, button_list, menu_mouse_pos):
        for button in button_list:
            button.changeColor(menu_mouse_pos)
            button.update(self.screen)