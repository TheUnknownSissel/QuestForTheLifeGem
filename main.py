import random, webbrowser
import pygame
import pygame.event as EVENTS
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
#initialize music
pygame.mixer.init()
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

#screen start up - note the way in how I use tilesize and the map dementions was seen from PygameFireEmblem by cmwchoi on GitHub
#150 is there for box containing unit information
screen = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 150))

# initialize fonts for displaying unit information
label_font = pygame.font.SysFont('gabriola', 40)
stats_font = pygame.font.SysFont('gabriola', 30)

def display_unit_data(character):
    # Sets up display for given character of type Player stats

    # Set up name of character on screen
    name_text = label_font.render(character.name, True, (255, 255, 255))
    # For centering the text for character's name
    name_text_rect = name_text.get_rect()
    name_text_rect.center = (325, MAPHEIGHT*TILESIZE + 20)
    # Place name in top middle of textbox
    screen.blit(name_text, name_text_rect)

    # Health: will be updated if a character takes damage. Displays both current and max health
    '''
    TO DO: Consider adding a health bar: stretch goal?
    '''
    health_text = stats_font.render('HP: ' + str(character.health) + '/' + str(character.max_health), True, (255, 255, 255))
    health_text_rect = name_text.get_rect()
    health_text_rect.center = (325, MAPHEIGHT * TILESIZE + 60)
    screen.blit(health_text, health_text_rect)

    # Atk
    atk_text = stats_font.render('Attack: ' + str(character.atk), True, (255, 255, 255))
    screen.blit(atk_text, (200, MAPHEIGHT * TILESIZE + 75))

    #Type
    type_text = stats_font.render('Unit Type: ' + str(character.type), True, (255, 255, 255))
    screen.blit(type_text, (350, MAPHEIGHT * TILESIZE + 75))

    # Def
    def_text = stats_font.render('Defense: ' + str(character.defen), True, (255, 255, 255))
    screen.blit(def_text, (200, MAPHEIGHT * TILESIZE + 100))

    # Res
    res_text = stats_font.render('Resistance: ' + str(character.res), True, (255, 255, 255))
    screen.blit(res_text, (350, MAPHEIGHT * TILESIZE + 100))


#Create player positions and list of all player positioining
unitPos1 = [MAPWIDTH-1, MAPHEIGHT-1]
unitPos2 = [MAPWIDTH-2, MAPHEIGHT-1]
unitPos3 = [MAPWIDTH-3, MAPHEIGHT-1]

unitPosList = [unitPos1, unitPos2, unitPos3]

#Initialize Units
mage = Player("Mage", 70, 3, 1, 3, 100, "Magical", "MageTest.png", 0, MAPWIDTH-2, MAPHEIGHT-1)
mage.rect.x = MAPWIDTH-32
mage.rect.y = MAPHEIGHT-32
player_list = pygame.sprite.Group()
player_list.add(mage)
warrior = Player("Warrior", 100, 8, 5, 2, 10, "Physical", "FighterTest.png", 0, MAPWIDTH-2, MAPHEIGHT-1)
# ISSUE when spawning multiple units how to get multiple to draw from player_list
'''warrior.rect.x = MAPWIDTH-2
warrior.rect.y = MAPHEIGHT-1
player_list = pygame.sprite.Group()
player_list.add(warrior)'''
tank = Player("Tank", 200, 1, 12, 7, 0, "Physical", "WarriorTest.png", 0,  MAPWIDTH-3, MAPHEIGHT-1)
'''tank.rect.x = MAPWIDTH-3
tank.rect.y = MAPHEIGHT-1
player_list = pygame.sprite.Group()
player_list.add(tank)'''

baddie = Player("badguy", 100000, 1, 12, 7, 40, "Physical", "WarriorTest.png", 0,  MAPWIDTH-3, MAPHEIGHT-1)
baddie.rect.x = MAPWIDTH * TILESIZE - 325
baddie.rect.y = MAPHEIGHT * TILESIZE - 325
baddie_list =pygame.sprite.Group()
baddie_list.add(baddie)
#Create list of these units
units = [warrior, mage, tank]



#Initialize mobs
#list here for set turn order


#pygame.mixer.music.load(os.path.join('Audio', 'nonstopix-rising-drum-beat-20804.wav'))



#Fill background with background color
#screen.fill(background_colour)

pygame.display.set_caption('Quest For the Life Gem')
clock = pygame.time.Clock()

running = True

#pygame.draw.rect(screen, WHITE, )
#pygame.draw.rect(screen, MAGENTA, (400, 100, 100, 150))

tracker = 0
def touch():
    # this was found from pygame.org and the professor's code
    collisions = pygame.sprite.groupcollide(baddie_list, player_list, False, False)
    for collision in collisions:
        baddie.calculate_damage(mage.get_atk(), mage.get_type())
        mage.calculate_damage(baddie.get_atk(), baddie.get_type())
        # for testing purposes only
        print(baddie.get_health())
        print(mage.get_health())
    if pygame.sprite.collide_rect(mage, baddie):
        # needs to change for the future
        mage.rect.x += 1 + mage.rect.x

# Starting the game loop
while running:
    clock.tick(FPS)
    # the game events
    for event in pygame.event.get():

        # Check for quit event to stop game
        if event.type == pygame.QUIT:
            running = False

    # Sets up the map from map.py. Code taken from https://github.com/cmwchoi/PygameFireEmblem/blob/master/Game.py
    for row in range(MAPHEIGHT):
        # Loop through each column in the row
        for column in range(MAPWIDTH):
            # Draw the resource at that position in the tilemap
            screen.blit(textures[Grass5], (column * TILESIZE, row * TILESIZE))
    #set Units
    player_list.draw(screen)
    baddie_list.draw(screen)
    #Game iterarion loop
    # Pull Unit from unit order list, reset order if need
    # Check if unit is Player controlable if movement and attack by player: if GOB (good or bad) is 0 it is a player controlled unit
    '''
    for playable in units:

        # Player controlled - movement, attack, check stats
        if mage.get_GOB() == 0:
            #impliment a move function/ control here

        # Enemy controled - AI do the thing (find out what that entails)
        if mage.get_GOB() == 1:
            #AI movement/ attack here
    '''
    # Display stats of current character
    display_unit_data(mage)


    #move here
    #for x in range(1,mage.set_speed()):

    mage.move()
    pygame.display.flip()
    mage.update()
    touch()


    # end movement and attack

    # Update status of units, check for deaths and remove units

    # Check if there are any enemies left or if there are any friendly units left

    # Check game over or win is true then move to a win or game over screen

    # go back to beginning of loop
    # checks for death
    pygame.display.update()

