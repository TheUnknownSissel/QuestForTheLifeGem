#import random
#import webbrowser
import pygame
#import os

#Initialize the pygame
pygame.init()
#


#Create the window
background_colour = (0, 133, 66)
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Quest For the Life Gem')

pygame.display.flip()

running = True

#create the screen
White = (0, 0, 0)
CYAN = (0, 100, 100)
MAGENTA = (255, 0, 255)
#pygame.draw.rect(screen, White, screen.Rect(200, 200, 100, 50))
#pygame.draw.rect(screen, CYAN, screen.Rect(300, 150, 100, 100))
#pygame.draw.rect(screen, MAGENTA, (400, 100, 100, 150))


