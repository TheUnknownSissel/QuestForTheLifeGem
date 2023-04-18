import random, webbrowser
import pygame
import pygame.event as Events
import os
import sys
import unit
from unit import *
import mob
import string
import map
from map import *

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
mage = Player("Mage", 70, 3, 1, 3, -5, 10, "Textures/MageTest.png")
warrior = Player("Warrior", 100, 8, 5, 2, 10, 0, "Textures/FighterTest.png")
tank = Player("Tank", 200, 1, 12, 7, 0, 0, "Textures/WarriorTest.png")


#Create list of these units
units = [warrior, mage, tank]

#Create player positions and list of all player positioining
unitPos1 = [MAPWIDTH-1, MAPHEIGHT-1]
unitPos2 = [MAPWIDTH-2, MAPHEIGHT-1]
unitPos3 = [MAPWIDTH-3, MAPHEIGHT-1]

unitPosList = [unitPos1, unitPos2, unitPos3]

#Initialize mobs
#list here for turn order

#Turn order sort both lists on speed



#screen start up - note the way in how I use tilesize and the map dementions was seen from PygameFireEmblem by cmwchoi on GitHub
screen = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

pygame.display.set_caption('Quest For the Life Gem')
clock = pygame.time.Clock()

pygame.display.flip()

running = True

#pygame.draw.rect(screen, WHITE, )
#pygame.draw.rect(screen, MAGENTA, (400, 100, 100, 150))


#Starting the game loop
