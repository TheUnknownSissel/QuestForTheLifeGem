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
