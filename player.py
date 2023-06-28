import pygame

class Player:
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.images_dead = []
        self.index = 0
        self.counter = 0
        self.on_ground = True
        for number in range(1,7):
            img_dead = pygame.image.load(f'img\char\dying{number}.png')
            img_dead = pygame.transform.scale(img_dead, (40, 70))
            self.images_dead.append(img_dead)
        for number in range(1,10):
            img_right = pygame.image.load(f'img\char\guy{number-1}.png')
            img_right = pygame.transform.scale(img_right, (40, 70))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.spawn_point = [x, y]
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.is_jumping = False
        self.direction = 1
        self.keys_achieved = 0
        self.hearts = 4
        self.game_over = False
        self.sound_pickup_key = pygame.mixer.Sound("assets/Sounds/collect_key.mp3")
        self.sound_pickup_key.set_volume(0.4)
        self.sound_death = pygame.mixer.Sound("assets/Sounds/death.mp3")
        self.sound_death.set_volume(0.4)

    def get_keys(self, keys, lvl_keys):
        if pygame.sprite.spritecollide(self, keys, True):
            self.sound_pickup_key.play()
            self.keys_achieved += 1
            if self.keys_achieved == lvl_keys:
                return True

    def update(self, screen, platform_list, enemies, projectiles, game_over, portals, level):
        next_position_x = 0
        next_position_y = 0
        walk_countdown = 3
        if not game_over:

            #Verificar colisión con un enemigo, #Verificar colisión con un proyectil, #Verificar colisión con el jefe
            if (pygame.sprite.spritecollide(self, enemies, False) or
            pygame.sprite.spritecollide(self, projectiles, True) or
            self.game_over):
                self.sound_death.play()
                if level.score - 10 < 0:
                    level.score = 0
                else:
                    level.score -= 10
                game_over = True
                self.index = 0
                self.counter = 0
                self.game_over = False

            key_list = pygame.key.get_pressed()

            if (key_list[pygame.K_w] or key_list[pygame.K_UP]) and (self.is_jumping is False and self.on_ground is True):
                self.vel_y = -15
                self.is_jumping = True
                self.on_ground = False
            if (key_list[pygame.K_w] or key_list[pygame.K_UP]) == False:
                self.is_jumping = False
            if key_list[pygame.K_LEFT] or key_list[pygame.K_a]:
                next_position_x -= 4
                self.counter += 1
                self.direction = -1
            if key_list[pygame.K_RIGHT] or key_list[pygame.K_d]:
                next_position_x += 4
                self.counter += 1
                self.direction = 1
            #Cuando el personaje se queda quieto, su imagen se cambia a la imagen idle
            if ((not key_list[pygame.K_LEFT] and not key_list[pygame.K_a]) and (not key_list[pygame.K_RIGHT] and not key_list[pygame.K_d])):
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            #Controlar animación
            if self.counter > walk_countdown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


        elif game_over:
            if self.index == -1:
                self.hearts -= 1
                self.rect.x = self.spawn_point[0]
                self.rect.y = self.spawn_point[1]
                game_over = False
            else:
                if self.counter > walk_countdown:
                    self.counter = 0
                    self.index += 1
                if self.index >= len(self.images_dead):
                    self.index = -1
                self.image = self.images_dead[self.index]
                self.counter += 1

        #Añadir gravedad
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        next_position_y += self.vel_y

        #Verificar colisión
        for platform in platform_list:
            #Verificar colisión en x
            if platform.rect.colliderect(self.rect.x + next_position_x, self.rect.y, self.width, self.height):
                next_position_x = 0
            #Verificar colisión en y
            if platform.rect.colliderect(self.rect.x, self.rect.y + next_position_y, self.width, self.height):
                if not pygame.sprite.spritecollide(self, portals, False) or not self.is_jumping:
                #Verificar cuando salta
                    if self.vel_y < 0:
                        next_position_y = platform.rect.bottom - self.rect.top
                        self.vel_y = 0
                    #Verificar cuando cae
                    elif self.vel_y >= 0:
                        next_position_y = platform.rect.top - self.rect.bottom
                        self.vel_y = 0
                        self.on_ground = True

        #actualizar las coordenadas del jugador
        self.rect.x += next_position_x
        self.rect.y += next_position_y


        #Dibujar al jugador en la ventana
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, (255,255,255), self.rect, 1)
        return game_over
