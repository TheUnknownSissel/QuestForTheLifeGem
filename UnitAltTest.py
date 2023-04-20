import pygame
import os
ship_img = pygame.image.load(os.path.join(Textures, "ship-blue.png")).convert()
BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = pygame.transform.scale(MageTest, (49, 37))
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(BLACK)
        #check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = winWidth / 2
        self.rect.bottom = winHeight - 20
        # set default x-axis speed
        self.speed_x = 0
        # set default health for our player - start at max 100% and then decrease...
        self.stShield = 100
        # firing delay between laser beams
        self.firing_delay = 200
        # time in ms since last fired
        self.last_fired = pygame.time.get_ticks()

    # update per loop iteration
    def update(self):
        self.speed_x = 0
        # check key presses
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speed_x = -5
        if key_state[pygame.K_RIGHT]:
            self.speed_x = 5
        # check space bar for firing projectile
        if key_state[pygame.K_SPACE]:
            # fire laser beam
            self.fire()
        self.rect.x += self.speed_x
        if self.rect.right > winWidth:
            self.rect.right = winWidth
        if self.rect.left < 0:
            self.rect.left = 0


