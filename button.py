import pygame
class Button():
    def __init__(self, image, pos, text_input, font_size, base_color, hovering_color, size):
        self.image = pygame.image.load(image)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font =  Button.get_font(font_size)
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.sound = pygame.mixer.Sound("assets/Sounds/teleport.wav")
        self.sound.set_volume(0.4)
        self.flag = 0
        self.click_sound = pygame.mixer.Sound("assets/Sounds/select_option.wav")
        self.click_sound.set_volume(0.4)

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.click_sound.play()
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            if self.flag == 0:
                self.flag = 1
                self.sound.play()
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.flag = 0

    def get_font(letter_size:int):
        return pygame.font.Font("assets/font.ttf", letter_size)
