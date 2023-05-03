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
    screen.blit(character.portrait, (15, MAPHEIGHT * TILESIZE + 10))


# Blacks out the stats menu for updating displayed information
def reset_menu():
    # Creates a black box to cover the old data so new data could be displayed
    pygame.draw.rect(screen, BLACK, (0, 640, 640, 150))

#initialize sword slash sound effect
#taken from https://mixkit.co/free-sound-effects/sword/
sword_effect = pygame.mixer.Sound(os.path.join('Audio', 'mixkit-fantasy-sword-slide-2798.wav'))
#Create player positions and list of all player positioining
unitPos1 = [MAPWIDTH-1, MAPHEIGHT-1]
unitPos2 = [MAPWIDTH-2, MAPHEIGHT-1]
unitPos3 = [MAPWIDTH-3, MAPHEIGHT-1]

unitPosList = [unitPos1, unitPos2, unitPos3]
# tile set for the animations/ not set yet for direwctional
mage_tileset = pygame.image.load('Textures/mage_spritesheet.png')
#there are three animations each being at the top with the diemensions 34 I cant find any documentation on how the subsurface is working
frame1 = mage_tileset.subsurface([0, 0, 32, 32])
frame2 = mage_tileset.subsurface([32, 0, 32, 32])
frame3 = mage_tileset.subsurface([64, 0, 32, 32])
mageFrames = [frame1, frame2, frame3]
#Initialize Units
mage = Player("Mage", 25, 3, 1, 3, 7, "Magical", "mageframe0.png", "mage_portrait.jpeg", 0)
mage.rect.x = MAPWIDTH * TILESIZE- 325 - 16
mage.rect.y = MAPHEIGHT * TILESIZE - 600 - 16
mage_list = pygame.sprite.Group()
mage_list.add(mage)
mage.set_sprite(mage_list)
warrior = Player("Warrior", 100, 8, 5, 2, 10, "Physical", "warriorframe0.png", "fighter_portrait.jpeg", 0)
warrior.rect.x = MAPWIDTH * TILESIZE- 200 - 16
warrior.rect.y = MAPHEIGHT * TILESIZE - 600 - 16
warrior_list = pygame.sprite.Group()
warrior_list.add(warrior)
warrior.set_sprite(warrior_list)
tank = Player("Tank", 200, 1, 12, 7, 0, "Physical", "tankframe0.png", "knight_portrait.jpeg", 0)
tank.rect.x = MAPWIDTH * TILESIZE- 400 - 16
tank.rect.y = MAPHEIGHT * TILESIZE - 600 - 16
tank_list = pygame.sprite.Group()
tank_list.add(tank)
tank.set_sprite(tank_list)
thief0 = Player("Thief", 25, 1, 5, 2, 5, "Physical", "thiefframe0.png", "thief_portrait.jpeg", 0)
thief0.rect.x = MAPWIDTH * TILESIZE - 325 -16
thief0.rect.y = MAPHEIGHT * TILESIZE - 325 -16
thief0_list =pygame.sprite.Group()
thief0_list.add(thief0)
thief0.set_sprite(thief0_list)
thief1 = Player("Thief", 25, 1, 5, 2, 5, "Physical", "thiefframe0.png", "thief_portrait.jpeg", 0)
thief1.rect.x = MAPWIDTH * TILESIZE - 200 -16
thief1.rect.y = MAPHEIGHT * TILESIZE - 325 -16
thief1_list = pygame.sprite.Group()
thief1_list.add(thief1)
thief1.set_sprite(thief1_list)
#Create list of these units - when frames are done needed to add in the lists for both and update the collection of untis
units = [mage, warrior, tank]
baddies = [thief0, thief1]
unitsSprites = [mage_list]
baddiesSprites = [thief0_list, thief1_list]

# For tracking player units that haven't taken their turn yet. 1 is subtracted to keep track of unit position in array
unmoved_units = len(units) - 1

# For keeping track of number of living player units
remaining_player_units = len(units) - 1

# For tracking enemy units that haven't taken their turn yet. 1 is subtracted to keep track of unit position in array
unmoved_enemies = len(baddies) - 1

# For keeping track of number of enemy player units
remaining_enemy_units = len(baddies) - 1

#setting up the game over and You win "screens"/ logo
gameover = Logo('Gameover.png')
gameover.rect.x = MAPWIDTH * TILESIZE -325 -52
gameover.rect.y = MAPHEIGHT * TILESIZE - 325 - 48
gameover_list =pygame.sprite.Group()
gameover_list.add(gameover)

win = Logo('Win.png')
win.rect.x = MAPWIDTH * TILESIZE - 325 - 52
win.rect.y = MAPHEIGHT * TILESIZE - 325 - 48
win_list =pygame.sprite.Group()
win_list.add(win)
#Initialize mobs
#list here for set turn order


#Fill background with background color
#screen.fill(background_colour)

pygame.display.set_caption('Quest For the Life Gem')
clock = pygame.time.Clock()

running = True

#pygame.draw.rect(screen, WHITE, )
#pygame.draw.rect(screen, MAGENTA, (400, 100, 100, 150))

# For keeping track of what state the game is in
state_tracker = 0

# For keeping track of the last direction a character was moved
last_direction = pygame.key.get_pressed()

# signal start of player phase.
# This state has state_tracker value of 0.
def start_player_phase_state():
    # Gain access to global variable state_tracker, remaining_player_units, and unmoved_units
    global state_tracker
    global remaining_player_units
    global unmoved_units
    # Clear display window
    reset_menu()
    # Set the value of unmoved_units to the value of remaining_player_units
    unmoved_units = remaining_player_units
    # Create text to signal start of player phase
    player_phase_text = phase_font.render("Player Phase!", True, WHITE)
    player_phase_rect = player_phase_text.get_rect()
    player_phase_rect.center = (325, MAPHEIGHT*TILESIZE + 60)
    screen.blit(player_phase_text, player_phase_rect)
    # Create message to tell player how to start gameplay
    phase_change_text = stats_font.render("(Press c to continue)", True, WHITE)
    phase_change_rect = phase_change_text.get_rect()
    phase_change_rect.center = (325, MAPHEIGHT*TILESIZE + 110)
    screen.blit(phase_change_text, phase_change_rect)

    # when c key is pressed, update state_tracker for next phase
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_c]:
        # Update state_tracker to move on to show_next_player_state
        state_tracker = 9

# Allow the player to move the character when it is the character's turn.
# This state has state_tracker value of 1.
def move_state(character, spriteList):
    # Gain access to global variable state_tracker and last_direction
    global state_tracker
    global last_direction
    # Clear display window
    reset_menu()
    # Display stats of current character
    display_unit_data(character)
    # Allow player to move character
    character.move()
    # Check bounding + if character still has health
    character.update()
    # Record last direction the player character moved
    last_direction = pygame.key.get_pressed()

    # For checking for collisions
    for sprite in spriteList:
        collisions = pygame.sprite.groupcollide(sprite, character.spriteGrab, False, False)
        # If collision with an enemy occurred, move on to check_enemy_state
        #sprtite = theif1_list

        for collision in collisions:
            state_tracker = 2
            if sprite == thief0_list:
                character.attacked = 0
            if sprite == thief1_list:
                character.attacked = 1
# When an enemy is collided into, the player can check its stats. They then decide to attack or return to move_state.
# This state has state_tracker value of 2.
def check_enemy_state(character, enemy):
    # Gain access to global variables state_tracker and last_direction
    global state_tracker
    global last_direction
    # Clear display window
    reset_menu()
    # Display data of enemy that was collided into
    display_unit_data(enemy)

    # Display player options
    options_text = stats_font.render('Attack: a Go back: b', True, RED)
    screen.blit(options_text, (450, MAPHEIGHT * TILESIZE + 5))

    # when a key is pressed, go to battle_forcast_state
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_a]:
        state_tracker = 3
    # when n key is pressed, return to move_state and move player character back
    '''
    TO DO: Change this so player character returns to previous location
    '''
    if key_state[pygame.K_b]:
        character.knockback(last_direction)
        state_tracker = 1


# Show the results of a battle between two characters.
# This state has state_tracker value of 3.
def battle_forcast_state(character, enemy):
    # Gain access to global variables state_tracker and last_direction
    global state_tracker
    global last_direction
    # Clear display window
    reset_menu()
    # This label is used for both characters involved in combat
    remaining_health_label = stats_font.render('Remaining Health: ', True, WHITE)

    # Player Unit
    # Calculate how much damage the player would take if attack goes through
    character_damage = character.calculate_damage(enemy.atk, enemy.type)
    # For storing the character's remaining health if damage is dealt
    character_remaining_health = character.current_health
    # If any damage will be dealt from the attack, update character_remaining_health to reflect that
    if character_damage > 0:
        # Update current health to account for damage
        character_remaining_health = character_remaining_health - character_damage
        # Prevent character from having negative health
        if character_remaining_health < 0:
            character_remaining_health = 0
    # Place player character's portrait on the left side
    screen.blit(character.portrait, (15, MAPHEIGHT * TILESIZE + 10))
    # Prepare text to display character's remaining health
    character_health_text = stats_font.render(str(character_remaining_health) + "/" + str(character.max_health), True, WHITE)
    # Display character's remaining health to screen
    screen.blit(character_health_text, (155, MAPHEIGHT * TILESIZE + 55))

    # Enemy Unit
    # Calculate how much damage the enemy would take if attack goes through
    enemy_damage = enemy.calculate_damage(character.atk, character.type)
    # For storing the enemy's remaining health if damage is dealt
    enemy_remaining_health = enemy.current_health
    # If any damage will be dealt from the attack, update enemy_remaining_health to reflect that
    if enemy_damage > 0:
        # Update current health to account for damage
        enemy_remaining_health = enemy_remaining_health - enemy_damage
        # Prevent enemy from having negative health
        if enemy_remaining_health < 0:
            enemy_remaining_health = 0
    # Place enemy character's portrait on the right side
    screen.blit(enemy.portrait, (500, MAPHEIGHT * TILESIZE + 10))
    # Prepare text to display enemy's remaining health
    enemy_health_text = stats_font.render(str(enemy_remaining_health) + "/" + str(enemy.max_health), True, WHITE)
    # Display enemy's remaining health to screen
    screen.blit(enemy_health_text, (450, MAPHEIGHT * TILESIZE + 55))

    # Battle Forcast label
    battle_forcast_text = label_font.render("Battle Forcast", True, WHITE)
    screen.blit(battle_forcast_text, (240, MAPHEIGHT*TILESIZE + 5))

    # Attack question label
    attack_question_text = label_font.render("Attack?", True, WHITE)
    screen.blit(attack_question_text, (275, MAPHEIGHT * TILESIZE + 55))

    # Yes label
    yes_label = stats_font.render("Yes: y", True, WHITE)
    screen.blit(yes_label, (210, MAPHEIGHT * TILESIZE + 100))

    # No label
    no_label = stats_font.render("No: n", True, WHITE)
    screen.blit(no_label, (390, MAPHEIGHT * TILESIZE + 100))

    # when y key is pressed, go to attack_state
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_y]:
        character.knockback(last_direction)
        state_tracker = 4
    # when n key is pressed, return to move_state
    if key_state[pygame.K_n]:
        character.knockback(last_direction)
        state_tracker = 1

# Have both player and enemy units attack each other and update health to reflect that.
# This state has state_tracker value of 4
def attack_state(character, enemy):
    # Gain access to global variables state_tracker, unmoved_units, remaining_player_units, and remaining_enemy_units
    global state_tracker
    global unmoved_units
    global remaining_player_units
    global remaining_enemy_units
    # Clear display window
    reset_menu()
    # Enemy takes damage
    enemy.take_damage(character.atk, character.type)
    # Check if enemy is dead: update remaining_enemy_units and remove from map if true
    if enemy.current_health <= 0:
        remaining_enemy_units -= 1
    enemy.update()
    # Character takes damage
    character.take_damage(enemy.atk, enemy.type)
    # Check if character is dead: update remaining_enemy_units and remove from map if true
    if character.current_health <= 0:
        remaining_player_units -= 1
    character.update()
    # Update value of unmoved_units to reflect that current player character has finished their turn
    unmoved_units -= 1
    # If win/lose conditions are not met and there are no more player characters to move,
    # move on to start_enemy_phase_state
    if unmoved_units == -1:
        state_tracker = 5
        winorlose()
    # Otherwise, go to show_next_player_state for the next player character's turn
    else:
        state_tracker = 9
        winorlose()

# signal start of enemy phase.
# This state has state_tracker value of 5.
def start_enemy_phase_state():
    # Gain access to global variable state_tracker, unmoved_enemies, and remaining_enemy_units
    global state_tracker
    global unmoved_enemies
    global remaining_enemy_units
    # Clear display window
    reset_menu()
    # Set the value of unmoved_enemies to the value of remaining_enemy_units
    unmoved_enemies = remaining_enemy_units
    # Create text to signal start of Enemy phase
    player_phase_text = phase_font.render("Enemy Phase!", True, WHITE)
    player_phase_rect = player_phase_text.get_rect()
    player_phase_rect.center = (325, MAPHEIGHT*TILESIZE + 60)
    screen.blit(player_phase_text, player_phase_rect)
    # Create message to tell player how to start gameplay
    phase_change_text = stats_font.render("(Press c to continue)", True, WHITE)
    phase_change_rect = phase_change_text.get_rect()
    phase_change_rect.center = (325, MAPHEIGHT*TILESIZE + 110)
    screen.blit(phase_change_text, phase_change_rect)

    # when y key is pressed, update state_tracker for next phase
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_c]:
        # Update state_tracker to move on to show_next_enemy_state
        state_tracker = 10

# Enemy attacks player unit that attacked it last
# This state has state_tracker value of 6.
'''
TO DO: make the enemy AI more complicated
'''
def enemy_attack_phase(enemy, character):
    # Gain access to global variables state_tracker, unmoved_enemies, remaining_player_units, and remaining_enemy_units
    global state_tracker
    global unmoved_enemies
    global remaining_player_units
    global remaining_enemy_units
    # Clear display window
    reset_menu()

    # Display what the enemy did
    # Player Unit
    # Calculate how much damage the player would take if attack goes through
    character_damage = character.calculate_damage(enemy.atk, enemy.type)
    # For storing the character's remaining health if damage is dealt
    character_remaining_health = character.current_health
    # If any damage will be dealt from the attack, update character_remaining_health to reflect that
    if character_damage > 0:
        # Update current health to account for damage
        character_remaining_health = character_remaining_health - character_damage
        # Prevent character from having negative health
        if character_remaining_health < 0:
            character_remaining_health = 0
    # Place player character's portrait on the left side
    screen.blit(character.portrait, (15, MAPHEIGHT * TILESIZE + 10))
    # Prepare text to display character's remaining health
    character_health_text = stats_font.render(str(character_remaining_health) + "/" + str(character.max_health), True,
                                              WHITE)
    # Display character's remaining health to screen
    screen.blit(character_health_text, (155, MAPHEIGHT * TILESIZE + 55))

    # Enemy Unit
    # Calculate how much damage the enemy would take if attack goes through
    enemy_damage = enemy.calculate_damage(character.atk, character.type)
    # For storing the enemy's remaining health if damage is dealt
    enemy_remaining_health = enemy.current_health
    # If any damage will be dealt from the attack, update enemy_remaining_health to reflect that
    if enemy_damage > 0:
        # Update current health to account for damage
        enemy_remaining_health = enemy_remaining_health - enemy_damage
        # Prevent enemy from having negative health
        if enemy_remaining_health < 0:
            enemy_remaining_health = 0
    # Place enemy character's portrait on the right side
    screen.blit(enemy.portrait, (500, MAPHEIGHT * TILESIZE + 10))
    # Prepare text to display enemy's remaining health
    enemy_health_text = stats_font.render(str(enemy_remaining_health) + "/" + str(enemy.max_health), True, WHITE)
    # Display enemy's remaining health to screen
    screen.blit(enemy_health_text, (450, MAPHEIGHT * TILESIZE + 55))


    # Enemy name
    enemy_name_text = label_font.render(enemy.name, True, WHITE)
    screen.blit(enemy_name_text, (275, MAPHEIGHT*TILESIZE + 5))

    # Attacked label
    attacked_text = label_font.render("attacked", True, WHITE)
    screen.blit(attacked_text, (275, MAPHEIGHT * TILESIZE + 40))

    # character name
    character_name_text = label_font.render(character.name + "!", True, WHITE)
    screen.blit(character_name_text, (275, MAPHEIGHT*TILESIZE + 70))

    # character name
    character_name_text = label_font.render(character.name + "!", True, WHITE)
    screen.blit(character_name_text, (275, MAPHEIGHT*TILESIZE + 70))

    phase_change_text = stats_font.render("(Press e to continue)", True, WHITE)
    phase_change_rect = phase_change_text.get_rect()
    phase_change_rect.center = (325, MAPHEIGHT * TILESIZE + 130)
    screen.blit(phase_change_text, phase_change_rect)

    # when e key is pressed, update state_tracker for next phase
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_e]:
        # Both characters are updated with damage. Done here to prevent an infinite loop of constant damage
        # Character takes damage
        character.take_damage(enemy.atk, enemy.type)
        # Enemy takes damage
        enemy.take_damage(character.atk, character.type)
        # Check if character is dead:
        if character.current_health <= 0:
            remaining_player_units -= 1
        character.update()
        # Check if enemy is dead
        if enemy.current_health <= 0:
            remaining_enemy_units -= 1
        enemy.update()
        unmoved_enemies -= 1
        # If win/lose conditions are not met and all enemies have finished their turns, move on to start_player_phase
        if unmoved_enemies <= -1:
            state_tracker = 0
        # Otherwise, go to show_next_enemy_state
        else:
            state_tracker = 10
        # Will go to lose_state or win_state if conditions are met
        winorlose()

# Displayed when the player loses.
# This state has state_tracker value of 7.
def lose_state():
    reset_menu()
    gameover_list.draw(screen)

# Displayed when the player wins.
# This state has state_tracker value of 8.
def win_state():
    reset_menu()
    win_list.draw(screen)

# Tells the player which player character is moving next.
# This state has state_tracker value of 9.
def show_next_player_state(character):
    # Gain access to global variables state_tracker
    global state_tracker
    # Clear display window
    reset_menu()
    # Create text to tell whose turn it is
    player_phase_text = phase_font.render(character.name + "'s Turn!", True, WHITE)
    player_phase_rect = player_phase_text.get_rect()
    player_phase_rect.center = (325, MAPHEIGHT*TILESIZE + 60)
    screen.blit(player_phase_text, player_phase_rect)

    # Create message to tell player how to start turn
    phase_change_text = stats_font.render("(Press o to continue)", True, WHITE)
    phase_change_rect = phase_change_text.get_rect()
    phase_change_rect.center = (325, MAPHEIGHT*TILESIZE + 110)
    screen.blit(phase_change_text, phase_change_rect)

    # Portrait of character
    screen.blit(character.portrait, (15, MAPHEIGHT * TILESIZE + 10))

    # when y key is pressed, update state_tracker for next phase
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_o]:
        # Update state_tracker to move on to move state
        state_tracker = 1

# Tells the player which player character is moving next.
# This state has state_tracker value of 10.
def show_next_enemy_state(enemy):
    # Gain access to global variables state_tracker
    global state_tracker
    # Clear display window
    reset_menu()
    # Create text to tell whose turn it is
    player_phase_text = phase_font.render(enemy.name + "'s Turn!", True, WHITE)
    player_phase_rect = player_phase_text.get_rect()
    player_phase_rect.center = (325, MAPHEIGHT*TILESIZE + 60)
    screen.blit(player_phase_text, player_phase_rect)

    # Create message to tell player how to start turn
    phase_change_text = stats_font.render("(Press o to continue)", True, WHITE)
    phase_change_rect = phase_change_text.get_rect()
    phase_change_rect.center = (325, MAPHEIGHT*TILESIZE + 110)
    screen.blit(phase_change_text, phase_change_rect)

    # Portrait of character
    screen.blit(enemy.portrait, (15, MAPHEIGHT * TILESIZE + 10))

    # when y key is pressed, update state_tracker for next phase
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_o]:
        # Update state_tracker to move on to enemy_attack_state
        state_tracker = 6
'''
original implimentation but had to be changed/revised to match state machine implimentation see movestate 
def touch():
    # this was found from pygame.org and the professor's code
    collisions = pygame.sprite.groupcollide(baddie_list, player_list, False, False)
    for collision in collisions:
        baddie.take_damage(mage.get_atk(), mage.get_type())
        mage.take_damage(baddie.get_atk(), baddie.get_type())
        sword_effect.play()
        # for testing purposes only
        print(baddie.get_current_health())
        print(mage.get_current_health())
    if pygame.sprite.collide_rect(mage, baddie):
        # needs to change for the future
        mage.rect.x += 1 + mage.rect.x
'''
def winorlose():
    # Gain access to global variables state_tracker, remaining_player_units, and remaining_enemy_units
    global state_tracker
    global remaining_player_units
    global remaining_enemy_units

    # If there are no more remaining player units, go to lose_state
    if remaining_player_units <= -1:
        state_tracker = 7
        #reset_menu()
        #gameover_list.draw(screen)
        #print("gameover")
    # If there are no more remaining enemy units, go to win_state
    if remaining_enemy_units <= -1:
        state_tracker = 8
        #reset_menu()
        #win_list.draw(screen)
        #print("win")

# music was made by Nonstopix https://pixabay.com/music/search/rising%20drum%20beat/
pygame.mixer.music.load(os.path.join('Audio', 'nonstopix-non-stop-rising-drum-beat-20804.wav'))
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(loops =-1)

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
            # Draw the resource at that position
            screen.blit(textures[Grass5], (column * TILESIZE, row * TILESIZE))
    #set Units
    mage_list.draw(screen)
    thief0_list.draw(screen)
    thief1_list.draw(screen)
    tank_list.draw(screen)
    warrior_list.draw(screen)
    #Game iterarion loop
    # Pull Unit from unit order list, reset order if needed
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

    # State machine
    if state_tracker == 0:
        start_player_phase_state()
    elif state_tracker == 1:
        move_state(units[unmoved_units], baddiesSprites)
    elif state_tracker == 2:
        check_enemy_state(units[unmoved_units], baddies[units[unmoved_units].attacked])
    elif state_tracker == 3:
        battle_forcast_state(mage, thief0)
    elif state_tracker == 4:
        attack_state(mage, thief0)
    elif state_tracker == 5:
        start_enemy_phase_state()
    elif state_tracker == 6:
        enemy_attack_phase(thief0, mage)
    elif state_tracker == 7:
        lose_state()
    elif state_tracker == 8:
        win_state()
    elif state_tracker == 9:
        show_next_player_state(mage)
    elif state_tracker == 10:
        show_next_enemy_state(thief0)


    # end movement and attack

    # Update status of units, check for deaths and remove units

    # Check if there are any enemies left or if there are any friendly units left

    # Check game over or win is true then move to a win or game over screen
    #call the game over funtion once in that state machine

    # go back to beginning of loop
    # checks for death
    pygame.display.update()

