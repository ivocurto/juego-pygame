import pygame
class Music:
    def __init__(self, song_path:str, volume: float):
        self.path = song_path
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(-1)
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)

    def increase_volume(self):
        if self.volume <= 0.9:
            self.volume = round(self.volume, 2) + 0.1
            pygame.mixer.music.set_volume(self.volume)

    def decrease_volume(self):
        if self.volume >= 0.1:
            self.volume = round(self.volume, 2) - 0.1
            pygame.mixer.music.set_volume(self.volume)

    def show_voume(self):
        rounded_volume = int(round(self.volume * 10, 1))
        return rounded_volume
