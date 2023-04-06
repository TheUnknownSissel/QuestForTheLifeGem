import os
import random
import pygame
import string

class Unit:
    def __init__(self, name, health, speed, defen, res, phy, mag):
        self.name = string(name)
        self.health = int(health)
        self.speed = int(speed)
        self.defen = int(defen)
        self.res = int(res)
        self.phy = int(phy)
        self.mag = int(mag)