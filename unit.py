import os
import random
import pygame
import string
import sys
from map import *
import pygame.event as EVENTS

CYAN = (0, 255, 255)
class Player(pygame.sprite.Sprite):
    def __init__(self, name, health, speed, defen, res, atk, type, imageref, GOB, positionx, positiony):

        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('Textures', imageref)).convert()
        #future implementation
        #img = pygame.image.load(os.path.join('Textures', str(imageref))).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.name = (name)
        self.health = (health)
        self.max_health = (health)
        self.speed = (speed)
        self.defen = (defen)
        self.res = (res)
        self.atk = (atk)
        self.type = (type)
        #outdated
        '''self.image = pygame.image.load(imageref)'''
        self.GOB = (GOB)




    #Getters and setters for all unit stats
    def set_name(self, n):
        self.name = n

    def set_health(self, h):
        self.health = h

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

    def get_health(self):
        return self.health

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
    #out dated
    def get_maxhealth(self):
        return self.max_health
    def set_maxhealth(self):
        return self.max_health
    '''
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
     #Here's my interpretation of the take_damage function. Please try testing this
    
    #This is a function to calcuate how much damage is taken when a unit is attacked 
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
            
        # Prevent unit from taking negative damage
        if total_damage > 0:
            self.health = self.health - total_damage


    def move(self):

        dis = self.get_speed()
        x = self.rect.x
        y = self.rect.y
        c = 0

        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.rect.x = x -4
            dis = dis + 1

        if key_state[pygame.K_RIGHT]:
            self.rect.x = x + 4
            dis = dis + 1

        if key_state[pygame.K_UP]:
            self.rect.y = y - 4
            dis = dis + 1
            #update to ckeck for bounding
        if key_state[pygame.K_DOWN]:
            self.rect.y = y + 4




    def update(self):
        if self.get_health() <= 0:
            self.kill()
        if self.rect.top < MAXTOP:
            self.rect.top = MAXTOP
        if self.rect.left < MAXLEFT:
            self.rect.left = MAXLEFT
        if self.rect.right > MAXRIGHT:
            self.rect.right = MAXRIGHT
        if self.rect.bottom > MAXBOTTOM:
            self.rect.bottom = MAXBOTTOM
