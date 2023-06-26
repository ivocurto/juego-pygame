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

    def update(self, screen, portal2):
        #Dibujar al portal
        screen.blit(self.image, self.rect)
        screen.blit(portal2.image, portal2.rect)

    def teleport(self, screen, projectiles, portal_2, player, axis:str):
        cooldown = 3
        self.counter += 1
        if self.counter >= cooldown:
            self.counter = 0
            for projectile in projectiles:
                if axis == "vertical":
                    if projectile.rect.colliderect(self.rect):
                        projectile.rect.x = portal_2.rect.x
                    elif projectile.rect.colliderect(portal_2.rect):
                        projectile.rect.x = self.rect.x
                elif axis == "horizontal":
                    if projectile.rect.colliderect(self.rect):
                        projectile.rect.y = portal_2.rect.y
                    elif projectile.rect.colliderect(portal_2.rect):
                        projectile.rect.y = self.rect.y

            if axis == "vertical":
                if player.rect.colliderect(self.rect):
                    player.rect.x = portal_2.rect.x - 40
                elif player.rect.colliderect(portal_2.rect):
                    player.rect.x = self.rect.x + 25
            elif axis == "horizontal":
                if player.rect.colliderect(self.rect):
                    player.rect.y = portal_2.rect.y + 10
                elif player.rect.colliderect(portal_2.rect):
                    player.rect.y = self.rect.y - 75

        self.update(screen, portal_2)
