import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.sound = pygame.mixer.Sound("assets/Sounds/teleport.wav")
        self.sound.set_volume(0.4)

    def update(self, screen, portal2):
        #Dibujar al portal
        screen.blit(self.image, self.rect)
        screen.blit(portal2.image, portal2.rect)

    def teleport(self, screen, projectiles, portal_2, player, axis:str):
        cooldown = 3
        self.counter += 1
        if self.counter >= cooldown:
            self.counter = 0

            if axis == "vertical":
                if player.rect.colliderect(self.rect):
                    player.rect.x = portal_2.rect.x - 40
                    self.sound.play()
                elif player.rect.colliderect(portal_2.rect):
                    player.rect.x = self.rect.x + 25
                    self.sound.play()
            elif axis == "horizontal":
                if player.rect.colliderect(self.rect):
                    player.rect.y = portal_2.rect.y + 10
                    self.sound.play()
                elif player.rect.colliderect(portal_2.rect):
                    player.rect.y = self.rect.y - 75
                    self.sound.play()

        self.update(screen, portal_2)
