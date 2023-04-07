#import random
#import webbrowser
import pygame
import pygame.event as Events
#import os
import sys
import unit





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

#screen start up
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Quest For the Life Gem')

pygame.display.flip()

running = True

#pygame.draw.rect(screen, White, screen.Rect(200, 200, 100, 50))
#pygame.draw.rect(screen, CYAN, screen.Rect(300, 150, 100, 100))
#pygame.draw.rect(screen, MAGENTA, (400, 100, 100, 150))