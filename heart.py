import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y, num, color = "Red"):
        pygame.sprite.Sprite.__init__(self)
        match color:
            case "Red":
                self.image = pygame.image.load("img/hearts/full_heart.png")
            case "Purple":
                self.image = pygame.image.load("img/hearts/full_heart_boss.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.heart_number = num

    def update(self, screen, entity):
        #Dibujar el corazon
        screen.blit(self.image, self.rect)
        Heart.lose_heart(self, entity)

    def lose_heart(self, entity):
        if entity.hearts == self.heart_number:
            self.kill()
