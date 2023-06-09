import os
import random
import pygame
import string
import sys
from map import *
import pygame.event as EVENTS
mage_tileset = pygame.image.load('Textures/mage_spritesheet.png')
#there are three animations each being at the top with the diemensions 34 I cant find any documentation on how the subsurface is working might not be working
frame1 = mage_tileset.subsurface([0, 0, 32, 32])
frame2 = mage_tileset.subsurface([32, 0, 32, 32])
frame3 = mage_tileset.subsurface([64, 0, 32, 32])
mageFrames = [frame1, frame2, frame3]
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self, name, health, speed, defen, res, atk, type, imageref, portrait, GOB):

        pygame.sprite.Sprite.__init__(self)
        # imageref: the sprite
        self.images = []
        for i in range(1,4):
            img = pygame.image.load(os.path.join('Textures', imageref)).convert()
            img.set_colorkey((0, 0, 0))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        # Character portrait for stats display. All portraits were drawn by Katherine
        self.portrait = pygame.image.load(os.path.join('Textures', portrait)).convert()
        # Name of the character
        self.name = (name)
        # Current health of the character: if this reaches 0, the character is removed from the field
        self.current_health = (health)
        # Maximum health of the character
        self.max_health = (health)
        # Speed of the character
        self.speed = (speed)
        # Defense of the character: reduces damage from physical type characters
        self.defen = (defen)
        # Resistance of the character: reduces damage from magical type characters
        self.res = (res)
        # Attack: controls how much damage a character deals
        self.atk = (atk)
        # Character type: controls what kind of damage
        self.type = (type)
        #outdated
        '''self.image = pygame.image.load(imageref)'''
        self.GOB = (GOB)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60
        # For tracking the array position of the last enemy the unit attacked (for player units)
        self.attacked = -1
        # For tracking the array position of the last unit that attacked them (for enemy units)
        self.last_attacked_by = -1
        #sprite list grab
        self.spriteGrab = None
    #Getters and setters for all unit stats
    def set_name(self, n):
        self.name = n

    def set_current_health(self, h):
        self.current_health = h

    def set_speed(self, s):
        self.speed = s

    def set_defen(self, d):
        self.defen = d

    def set_res(self, r):
        self.res = r

    def set_atk(self, a):
        self.atk = a

    def set_type(self, t):
        self.type = t

    def get_name(self):
        return self.name

    def get_current_health(self):
        return self.current_health

    def get_speed(self):
        return self.speed

    def get_defen(self):
        return self.defen

    def get_res(self):
        return self.res

    def get_atk(self):
        return self.atk

    def get_type(self):
        return self.type

    def get_GOB(self):
        return self.GOB
    def get_maxhealth(self):
        return self.max_health
    def set_maxhealth(self):
        return self.max_health
    def set_sprite(self, x):
        self.spriteGrab = x
    # the way damage was calculated was updated and changed as the project went along
    '''
    Original idea for how damage was calculated but needed to be revised to account for unit types and def and res
    def take_damage (self, damage, magdamage):
        defen = self.get_defen()
        res = self.get_res()
        health = self.get_health()
        physDamage = damage - defen
        magDamage = magdamage - res
        healthChangePhys = health - physDamage
        healthChangeMag = health - magDamage
        if physDamage > 0:
            self.set_health(self, healthChangePhys)
        if magDamage > 0:
            self.set_health(self, healthChangeMag)

        return 0
    '''

    # Here's my interpretation of the take_damage function. Please try testing this

    # This is a function to calcuate how much damage is taken when a unit is attacked
    def calculate_damage(self, enemy_atk, enemy_type):
        # Initialize the variable to store how much damage will be taken
        total_damage = 0
        # If enemy type is physical, calculate damage by subtracting unit's defen
        # from enemy's atk
        if enemy_type == "Physical":
            total_damage = enemy_atk - self.defen

        # Else, if enemy type is magical, calculate damage by subtracting unit's res
        # from enemy's atk
        else:
            total_damage = enemy_atk - self.res
        # returns value of total_damage
        return total_damage

    # This function allows a unit to take damage
    def take_damage(self, enemy_atk, enemy_type):
        # get the total damage taken using calculate_damage
        total_damage = self.calculate_damage(enemy_atk, enemy_type)
        # Prevent unit from taking negative damage
        if total_damage > 0:
            # Update previous_health to value of current_health
            self.previous_health = self.current_health
            # Update current health to account for damage
            self.current_health = self.current_health - total_damage

    # Controls character movement
    def move(self):

        dis = self.get_speed()
        x = self.rect.x
        y = self.rect.y
        c = 0

        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.rect.x = x - 4
            dis = dis + 1

        if key_state[pygame.K_RIGHT]:
            self.rect.x = x + 4
            dis = dis + 1

        if key_state[pygame.K_UP]:
            self.rect.y = y - 4
            dis = dis + 1
            # update to ckeck for bounding
        if key_state[pygame.K_DOWN]:
            self.rect.y = y + 4

    # moves a character the opposite direction from the direction last pressed
    def knockback(self, last_key):

        dis = self.get_speed()
        x = self.rect.x
        y = self.rect.y
        c = 0

        key_state = last_key
        if key_state[pygame.K_LEFT]:
            self.rect.x = x + 4
            dis = dis + 1

        if key_state[pygame.K_RIGHT]:
            self.rect.x = x - 4
            dis = dis + 1

        if key_state[pygame.K_UP]:
            self.rect.y = y + 4
            dis = dis + 1

        if key_state[pygame.K_DOWN]:
            self.rect.y = y - 4

    # Controls bounding, removes units from map when defeated, and controls sprite animation and positioning
    def update(self):
        if self.get_current_health() <= 0:
            self.kill()
        if self.rect.top < MAXTOP:
            self.rect.top = MAXTOP
        if self.rect.left < MAXLEFT:
            self.rect.left = MAXLEFT
        if self.rect.right > MAXRIGHT:
            self.rect.right = MAXRIGHT
        if self.rect.bottom > MAXBOTTOM:
            self.rect.bottom = MAXBOTTOM
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 1:
                image = pygame.image.load(
                    os.path.join('Textures', self.name + 'frame' + str(self.frame - 1) + '.png')).convert()
                image.set_colorkey(BLACK)
                self.image = image
            if self.frame == 2:
                image = pygame.image.load(
                    os.path.join('Textures', self.name + 'frame' + str(self.frame - 1) + '.png')).convert()
                image.set_colorkey(BLACK)
                self.image = image
            if self.frame == 2:
                image = pygame.image.load(
                    os.path.join('Textures', self.name + 'frame' + str(self.frame - 1) + '.png')).convert()
                image.set_colorkey(BLACK)
                self.image = image
                self.frame = 0