import os
import random
import pygame
import string
import sys


class Player:
    def __init__(self, name, health, speed, defen, res, atk, type, imageref):
        self.name = (name)
        self.health = (health)
        self.speed = (speed)
        self.defen = (defen)
        self.res = (res)
        self.atk  = (atk)
        self.type = (type)
        self.image = pygame.image.load(imageref)
        self.rect = self.image.get_rect()  # checks images and get rect...



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
