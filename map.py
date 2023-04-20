import pygame, sys
# This code is based off of another project found at https://github.com/cmwchoi/PygameFireEmblem/blob/master/SacaeMap.py
# This includes their map class and some implementation of how units operate in that system
Grass = 0
#Tree = 1
Grass2 = 2
Grass3 = 3
Grass4 = 4
Grass5 = 5
Grass6 = 6
Grass7 = 7
Grass8 = 8
Grass9 = 9

# Stores the tile sets for cropping and creating the map.
# These use free assets found at https://cainos.itch.io/pixel-art-top-down-basic
grass_tileset = pygame.image.load('Textures/TX_Tileset_Grass.png')
tree_tileset = pygame.image.load('Textures/TX_Plant.png')

# TO DO: Due to the nature of the tile sets, I believe it would be best to change the formatting for adding trees/plants
# to map: maybe similar way to adding characters to screen?
textures = {
            # Subsurface used to crop exact parts of tile set for use
            Grass : grass_tileset.subsurface([0, 0, 32, 32]),
            Grass2 : grass_tileset.subsurface([32, 0, 32, 32]),
            Grass3 : grass_tileset.subsurface([64, 0, 32, 32]),
            Grass4 : grass_tileset.subsurface([0, 32, 32, 32]),
            Grass5 : grass_tileset.subsurface([32, 32, 32, 32]),
            Grass6 : grass_tileset.subsurface([64, 32, 32, 32]),
            Grass7 : grass_tileset.subsurface([0, 64, 32, 32]),
            Grass8 : grass_tileset.subsurface([32, 64, 32, 32]),
            Grass9 : grass_tileset.subsurface([64, 64, 32, 32]),
            #Tree : pygame.image.load('Textures/Tree.png')

           }

#Tilemap
tilemap = [
            [Grass, Grass2, Grass3, Grass, Grass2, Grass3, Grass, Grass2,  Grass3, Grass, Grass2],
            [Grass4, Grass5, Grass6, Grass4, Grass5, Grass6, Grass4, Grass5, Grass6, Grass4, Grass5],
            [Grass7, Grass8, Grass9, Grass7, Grass8, Grass9, Grass7, Grass8, Grass9, Grass7, Grass8],
            [Grass, Grass2, Grass3, Grass, Grass2, Grass3, Grass, Grass2,  Grass3, Grass, Grass2],
            [Grass4, Grass5, Grass6, Grass4, Grass5, Grass6, Grass4, Grass5, Grass6, Grass4, Grass5],
            [Grass7, Grass8, Grass9, Grass7, Grass8, Grass9, Grass7, Grass8, Grass9, Grass7, Grass8],
            [Grass, Grass2, Grass3, Grass, Grass2, Grass3, Grass, Grass2,  Grass3, Grass, Grass2],
            [Grass4, Grass5, Grass6, Grass4, Grass5, Grass6, Grass4, Grass5, Grass6, Grass4, Grass5],
            [Grass7, Grass8, Grass9, Grass7, Grass8, Grass9, Grass7, Grass8, Grass9, Grass7, Grass8],
            [Grass, Grass2, Grass3, Grass, Grass2, Grass3, Grass, Grass2,  Grass3, Grass, Grass2],
            [Grass4, Grass5, Grass6, Grass4, Grass5, Grass6, Grass4, Grass5, Grass6, Grass4, Grass5],
          ]

# Game Dimensions
TILESIZE = 32
MAPWIDTH = 11
MAPHEIGHT = 10

