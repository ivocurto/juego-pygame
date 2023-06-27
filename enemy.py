import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img\enemy/blob1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x + 10
        self.rect.y = y - 10
        self.vel_y = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity = 0
        self.counter = 0
        self.index = 0
        self.direction = 1
        self.falling = True
        #Animación al caer contra el piso
        self.fell = False
        self.images_fell_right = []
        self.images_fell_left = []
        self.len_fall_secuence = 16
        self.walk_countdown = 3
        for number in range(1,18):
            img_fell_right = pygame.image.load(f'img\enemy/fell{number}.png')
            img_fell_left = pygame.transform.flip(img_fell_right, True, False)
            self.images_fell_right.append(img_fell_right)
            self.images_fell_left.append(img_fell_left)
        #Animación al caminar:
        self.images_right = []
        self.images_left = []
        for number in range(1,3):
            img_right = pygame.image.load(f'img\enemy/blob{number+1}.png')
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.times_teleported = 0
        self.teleport_cooldown = 10
        self.teleport_counter = 0
        self.sound_death = pygame.mixer.Sound("assets\Sounds\kill_slime.mp3")
        self.sound_death.set_volume(0.4)

    def update(self, screen, platform_list, portal_list):
        next_position_y = 0

        #Controlar animaciónes
        self.counter += 1
        if self.counter > self.walk_countdown:
            self.counter = 0
            #Animación al caer
            if self.velocity == 0 and self.fell:
                self.walk_countdown = 1
                if self.index <= 16:
                    match self.direction:
                        case 1:
                            self.image = self.images_fell_right[self.index]
                        case -1:
                            self.image = self.images_fell_left[self.index]
                elif self.index > 16:
                    self.len_fall_secuence -= 1
                    match self.direction:
                        case 1:
                                self.image = self.images_fell_right[self.len_fall_secuence]
                        case -1:
                            self.image = self.images_fell_left[self.len_fall_secuence]
                if self.index > 31:
                    self.len_fall_secuence = 16
                    self.walk_countdown = 3
                    if self.direction == 1:
                        self.velocity = 2
                    elif self.direction == -1:
                        self.velocity = -2
                    self.index = 0
                    self.fell = False
            #Animación al caminar
            else:
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1 and not self.falling:
                    self.image = self.images_left[self.index]
            self.index += 1

        #Añadir gravedad
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        next_position_y += self.vel_y

        #Dibujar al enemigo
        screen.blit(self.image, self.rect)

        #Verificar colisión
        self.falling = True
        for platform in platform_list:
            #Verificar colisión en x
            if platform.rect.colliderect(self.rect.x + self.velocity, self.rect.y, self.width, self.height):
                self.velocity *= -1
                self.direction *= -1
            #Verificar colisión en y
            if platform.rect.colliderect(self.rect.x, self.rect.y + next_position_y, self.width, self.height):
                self.falling = False
                self.fell = True
                #Verificar cuando salta
                if self.vel_y < 0:
                    next_position_y = platform.rect.bottom - self.rect.top
                    self.vel_y = 0
                #Verificar cuando cae
                elif self.vel_y >= 0:
                    next_position_y = platform.rect.top - self.rect.bottom
                    self.vel_y = 0
                    self.rect.x += self.velocity
        if self.falling:
            if self.direction == 1:
                self.image = pygame.image.load("img/enemy/blob1.png")
            elif self.direction == -1:
                self.image = pygame.image.load("img/enemy/blob-1.png")
            self.velocity = 0
            self.fell = False

        #verificar colision con portales
        if pygame.sprite.spritecollide(self, portal_list, False):
            self.sound_death.play()
            self.kill()

        #actualizar las coordenadas del jugador
        self.rect.y += next_position_y
        if self.rect.y > 700 or self.rect.x > 900:
            self.kill()
        # pygame.draw.rect(screen, (255,255,255), self.rect)
