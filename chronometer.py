import pygame
class Chronometer:
    def __init__(self):
        self.initial_time = 0
        self.time_elapsed = 0
        self.aux = 1
        self.color = (255,255,255)

    def init_chronometer(self):
        self.initial_time = pygame.time.get_ticks()

    def get_time_elapsed(self, screen):
        self.time_elapsed = pygame.time.get_ticks()
        if self.time_elapsed  - self.initial_time >= 1000:
            self.aux += 1
            self.initial_time = self.time_elapsed
        Chronometer.print_time_elapsed(self, screen)
        return self.aux

    def print_time_elapsed(self, screen):
        time_elapsed = self.aux
        font = pygame.font.Font(None, 36)
        if time_elapsed >= 50:
            self.color = (255, 0, 0)
        text = font.render("Time: {}".format(time_elapsed), True, self.color)
        screen.blit(text, (250, 30))
