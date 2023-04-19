import pygame, sys
# This code is based off of another project found at https://github.com/cmwchoi/PygameFireEmblem/blob/master/SacaeMap.py
# This includes their map class and some implementation of how units operate in that system
Grass = 0
Tree = 1

# Stores the tile sets for cropping and creating the map.
# These use free assets found at https://cainos.itch.io/pixel-art-top-down-basic
grass_tileset = pygame.image.load('Textures/TX_Tileset_Grass.png')
tree_tileset = pygame.image.load('Textures/TX_Plant.png')

# TO DO: Due to the nature of the tile sets, I believe it would be best to change the formatting for adding trees/plants
# to map: maybe similar way to adding characters to screen?
textures = {
            # Subsurface used to crop exact parts of tile set for use
             Grass : grass_tileset.subsurface([32,32,32,32]),
             Tree : pygame.image.load('Textures/Tree.png')

           }

#Tilemap
tilemap = [
            [Tree, Tree, Tree, Tree, Tree, Grass, Grass, Tree,  Grass, Tree, Tree],
            [Grass,     Grass,     Tree, Tree, Tree, Grass, Grass, Grass, Grass, Grass,     Tree],
            [Grass,     Grass,     Tree, Tree, Tree, Grass, Grass, Grass, Grass, Grass,     Grass    ],
            [Grass,     Grass,     Grass,    Grass,    Grass,    Grass, Grass, Grass, Grass, Grass,     Grass    ],
            [Grass,     Grass,     Grass,    Grass,    Grass,    Grass, Grass, Grass, Grass, Grass,     Grass    ],
            [Grass,     Grass,     Grass,    Grass,    Grass,    Grass, Grass, Grass, Grass, Grass,     Grass    ],
            [Grass,     Grass,     Grass,    Grass,    Grass,    Grass, Grass, Grass, Grass, Grass,     Grass    ],
            [Tree,    Grass,     Grass,    Grass,    Grass,    Grass, Grass, Grass, Grass, Grass,     Grass    ],
            [Tree,    Grass,     Grass,    Grass,    Grass,    Grass, Grass, Grass, Grass, Tree,      Grass    ],
            [Tree,    Grass,     Tree,     Grass,    Grass,    Grass, Grass, Grass, Grass, Grass,     Tree      ]
          ]

# Game Dimensions
TILESIZE = 32
MAPWIDTH = 11
MAPHEIGHT = 10

