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
from gameScreens import Logo
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
phase_font = pygame.font.SysFont('gabriola', 60)

def display_unit_data(character):
    # Sets up display for given character of type Player stats
    # Set up name of character on screen
    name_text = label_font.render(character.name, True, WHITE)
    # For centering the text for character's name
    name_text_rect = name_text.get_rect()
    name_text_rect.center = (325, MAPHEIGHT*TILESIZE + 20)
    # Place name in top middle of textbox
    screen.blit(name_text, name_text_rect)

    # Health: will be updated if a character takes damage. Displays both current and max health
    # Remove previous health by drawing over in black
    '''
    TO DO: Consider moving to collision function         
    '''
    health_text = stats_font.render('HP: ' + str(character.previous_health) + '/' + str(character.max_health), True, BLACK)
    health_text_rect = name_text.get_rect()
    health_text_rect.center = (325, MAPHEIGHT * TILESIZE + 60)
    screen.blit(health_text, health_text_rect)
    # Place value of current health on screen
    health_text = stats_font.render('HP: ' + str(character.current_health) + '/' + str(character.max_health), True, WHITE)
    health_text_rect = name_text.get_rect()
    health_text_rect.center = (325, MAPHEIGHT * TILESIZE + 60)
    screen.blit(health_text, health_text_rect)

    # Atk
    atk_text = stats_font.render('Attack: ' + str(character.atk), True, WHITE)
    screen.blit(atk_text, (200, MAPHEIGHT * TILESIZE + 75))

    #Type
    type_text = stats_font.render('Unit Type: ' + str(character.type), True, WHITE)
    screen.blit(type_text, (350, MAPHEIGHT * TILESIZE + 75))

    # Def
    def_text = stats_font.render('Defense: ' + str(character.defen), True, WHITE)
    screen.blit(def_text, (200, MAPHEIGHT * TILESIZE + 100))

    # Res
    res_text = stats_font.render('Resistance: ' + str(character.res), True, WHITE)
    screen.blit(res_text, (350, MAPHEIGHT * TILESIZE + 100))

    # Portrait
    screen.blit(character.portrait, (25, MAPHEIGHT * TILESIZE + 10))


# Blacks out the stats menu for updating displayed information
def reset_menu():
    # Creates a black box to cover the old data so new data could be displayed
    pygame.draw.rect(screen, BLACK, (0, 640, 640, 150))


#Create player positions and list of all player positioining
unitPos1 = [MAPWIDTH-1, MAPHEIGHT-1]
unitPos2 = [MAPWIDTH-2, MAPHEIGHT-1]
unitPos3 = [MAPWIDTH-3, MAPHEIGHT-1]

unitPosList = [unitPos1, unitPos2, unitPos3]

#Initialize Units
mage = Player("Mage", 70, 3, 1, 3, 100, "Magical", "MageTest.png", "mage_portrait.jpeg", 0, MAPWIDTH-2, MAPHEIGHT-1)
mage.rect.x = MAPWIDTH-32
mage.rect.y = MAPHEIGHT-32
player_list = pygame.sprite.Group()
player_list.add(mage)
warrior = Player("Warrior", 100, 8, 5, 2, 10, "Physical", "FighterTest.png", "fighter_portrait.jpeg", 0, MAPWIDTH-2, MAPHEIGHT-1)
# ISSUE when spawning multiple units how to get multiple to draw from player_list
'''warrior.rect.x = MAPWIDTH-2
warrior.rect.y = MAPHEIGHT-1
player_list = pygame.sprite.Group()
player_list.add(warrior)'''
tank = Player("Tank", 200, 1, 12, 7, 0, "Physical", "WarriorTest.png", "knight_portrait.jpeg", 0,  MAPWIDTH-3, MAPHEIGHT-1)
'''tank.rect.x = MAPWIDTH-3
tank.rect.y = MAPHEIGHT-1
player_list = pygame.sprite.Group()
player_list.add(tank)'''

baddie = Player("badguy", 100000, 1, 12, 7, 40, "Physical", "WarriorTest.png", "thief_portrait.jpeg", 0,  MAPWIDTH-3, MAPHEIGHT-1)
baddie.rect.x = MAPWIDTH * TILESIZE - 325 -16
baddie.rect.y = MAPHEIGHT * TILESIZE - 325 -16
baddie_list =pygame.sprite.Group()
baddie_list.add(baddie)
#Create list of these units
units = [warrior, mage, tank]
baddies = [baddie]



#setting up the game over and You win "screens"/ logo
gameover = Logo('Gameover.png')
gameover.rect.x = MAPWIDTH * TILESIZE -325 -52
gameover.rect.y = MAPHEIGHT * TILESIZE - 325 - 48
gameover_list =pygame.sprite.Group()
gameover_list.add(gameover)

win = Logo('Gameover.png')
win.rect.x = MAPWIDTH * TILESIZE -325
win.rect.y = MAPHEIGHT * TILESIZE - 325
win_list =pygame.sprite.Group()
win_list.add(gameover)
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

# For keeping track of what state the game is in
state_tracker = 0

# signal start of player phase.
# This state has state_tracker value of 0.
def start_player_phase_state():
    # Gain access to global variable state_tracker
    global state_tracker
    # Clear display window
    reset_menu()
    # Create text to signal start of player phase
    player_phase_text = phase_font.render("Player Phase!", True, WHITE)
    player_phase_rect = player_phase_text.get_rect()
    player_phase_rect.center = (325, MAPHEIGHT*TILESIZE + 60)
    screen.blit(player_phase_text, player_phase_rect)
    # Create message to tell player how to start gameplay
    phase_change_text = stats_font.render("(Press y to continue)", True, WHITE)
    phase_change_rect = phase_change_text.get_rect()
    phase_change_rect.center = (325, MAPHEIGHT*TILESIZE + 110)
    screen.blit(phase_change_text, phase_change_rect)

    # when y key is pressed, update state_tracker for next phase
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_y]:
        # Update state_tracker to move on to move state
        state_tracker = 1

# Allow the player to move the character when it is the character's turn.
# This state has state_tracker value of 1.
def move_state(character):
    # Gain access to global variable state_tracker
    global state_tracker
    # Clear display window
    reset_menu()
    # Display stats of current character
    display_unit_data(character)
    # Allow player to move character
    character.move()
    # Check bounding + if character still has health
    character.update()

    # For checking for collisions
    collisions = pygame.sprite.groupcollide(baddie_list, player_list, False, False)
    # If collision with an enemy occurred, move on to check_enemy_state
    for collision in collisions:
        state_tracker = 2

# When an enemy is collided into, the player can check its stats. They then decide to attack or return to move_state.
# This state has state_tracker value of 2.
def check_enemy_state(enemy):
    # Gain access to global variable state_tracker
    global state_tracker
    # Clear display window
    reset_menu()
    # Display data of enemy that was collided into
    display_unit_data(enemy)

    # Display player options
    options_text = stats_font.render('Attack: y Go back: n', True, RED)
    screen.blit(options_text, (450, MAPHEIGHT * TILESIZE + 5))

    # when y key is pressed, go to battle_forcast_state
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_y]:
        state_tracker = 3
    # when n key is pressed, return to move_state
    if key_state[pygame.K_n]:
        state_tracker = 1


# Show the results of a battle between two characters.
# This state has state_tracker value of 3.
'''
Incomplete
'''
def battle_forcast_state(character, enemy):
    # Gain access to global variable state_tracker
    global state_tracker
    # Clear display window
    reset_menu()
    # when y key is pressed, go to attack_state
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_y]:

        state_tracker = 4
    # when n key is pressed, return to move_state
    if key_state[pygame.K_n]:

        state_tracker = 1

# Have both player and enemy units attack each other and update health to reflect that.
# This state has state_tracker value of 4
def attack_state(character, enemy):
    # Gain access to global variable state_tracker
    global state_tracker
    # Clear display window
    reset_menu()
    # Enemy takes damage
    enemy.take_damage(character.atk, character.type)
    # Check if enemy is dead
    enemy.update()
    # Character takes damage
    character.take_damage(enemy.atk, enemy.type)
    # Check if character is dead
    character.update()
    # Check if winning or losing conditions were met
    '''
    TO DO: change this to reflect victory and defeat states
    '''
    winorlose()
    # If win/lose conditions are not met, move on to start_enemy_phase_state
    state_tracker = 5

# signal start of enemy phase.
# This state has state_tracker value of 5.
def start_enemy_phase_state():
    # Gain access to global variable state_tracker
    global state_tracker
    # Clear display window
    reset_menu()
    # Create text to signal start of Enemy phase
    player_phase_text = phase_font.render("Enemy Phase!", True, WHITE)
    player_phase_rect = player_phase_text.get_rect()
    player_phase_rect.center = (325, MAPHEIGHT*TILESIZE + 60)
    screen.blit(player_phase_text, player_phase_rect)
    # Create message to tell player how to start gameplay
    phase_change_text = stats_font.render("(Press y to continue)", True, WHITE)
    phase_change_rect = phase_change_text.get_rect()
    phase_change_rect.center = (325, MAPHEIGHT*TILESIZE + 110)
    screen.blit(phase_change_text, phase_change_rect)

    # when y key is pressed, update state_tracker for next phase
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_y]:
        # Update state_tracker to move on to enemy_attack_state
        state_tracker = 6

def touch():
    # this was found from pygame.org and the professor's code
    collisions = pygame.sprite.groupcollide(baddie_list, player_list, False, False)
    for collision in collisions:
        baddie.take_damage(mage.get_atk(), mage.get_type())
        mage.take_damage(baddie.get_atk(), baddie.get_type())
        # for testing purposes only
        print(baddie.get_current_health())
        print(mage.get_current_health())
    if pygame.sprite.collide_rect(mage, baddie):
        # needs to change for the future
        mage.rect.x += 1 + mage.rect.x
def winorlose():
    #for unit in units
    # unit.get_current_health
    if mage.get_current_health() <= 0:
        gameover_list.draw(screen)
        print("gameover")
    #for baddie in baddies
    if baddie.get_current_health() <= 0:
        gameover_list.draw(screen)
        print("win")
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
    #display_unit_data(mage)



    #move here
    #for x in range(1,mage.set_speed()):

    #start_player_phase_state()
    #mage.move()
    #pygame.display.flip()
    #mage.update()
    #touch()
    if state_tracker == 0:
        start_player_phase_state()
    elif state_tracker == 1:
        move_state(mage)
    elif state_tracker == 2:
        check_enemy_state(baddie)


    # end movement and attack

    # Update status of units, check for deaths and remove units

    # Check if there are any enemies left or if there are any friendly units left

    # Check game over or win is true then move to a win or game over screen
    #call the game over funtion once in that state machine
    winorlose()
    # go back to beginning of loop
    # checks for death
    pygame.display.update()

