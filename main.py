import random
import webbrowser
import pygame
import pygame.event as Events
import os
import sys
import unit
from unit import *
import mob
import string

#Initialize the pygame
pygame.init()

#Create the window
background_colour = (0, 133, 66)
screen_width = 480
screen_height = 640
FPS = 60
#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
#Initialize Units
mage = Player("MAGE", 70, 3, 1, 3, -5, 10, "download.jpeg")
warrior = Player("Warrior", 100, 8, 5, 2, 10, 0, "download.jpeg")
tank = Player("Tank", 200, 1, 12, 7, 0, 0, "download.jpeg")


#Create list of these units
units = [warrior, mage, tank]

#Initialize mobs
#list here

#Turn order sort both lists on speed



#screen start up
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Quest For the Life Gem')

pygame.display.flip()

running = True

#pygame.draw.rect(screen, WHITE, )
#pygame.draw.rect(screen, MAGENTA, (400, 100, 100, 150))

#Starting the game loop