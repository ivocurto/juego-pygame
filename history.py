import pygame
from config.images import BACKGROUND_IMAGE
class History():
    def __init__(self, img_path):
        super().__init__()
        self.bg_img = pygame.image.load(img_path)
        self.pressing_space = False
        self.space_pressed = False
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def update(self):
        while True:
            self.screen.blit(self.bg_img, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 1
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pressing_space = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.space_pressed = True

            # Realizar algo si el espacio se presiona y luego se deja de presionar
            if self.pressing_space and self.space_pressed:
                self.bg_img = pygame.image.load(BACKGROUND_IMAGE)
                break
            pygame.display.flip()
