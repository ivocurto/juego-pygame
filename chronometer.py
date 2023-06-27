import pygame
class Chronometer:
    def __init__(self):
        self.initial_time = 0
        self.time_elapsed = 0
        self.aux = 1

    def init_chronometer(self):
        self.initial_time = pygame.time.get_ticks()

    def get_time_elapsed(self, screen):
        self.time_elapsed = pygame.time.get_ticks() - self.initial_time
        if self.time_elapsed // 1000 == self.aux:
            self.aux += 1
        Chronometer.print_time_elapsed(self, screen)
        return self.aux

    def print_time_elapsed(self, screen):
        time_elapsed = self.aux
        font = pygame.font.Font(None, 36)
        text = font.render("Time: {}".format(time_elapsed), True, (255,255,255))
        screen.blit(text, (250, 30))