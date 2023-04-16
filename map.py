import pygame, sys
# This code is based off of another project found at https://github.com/cmwchoi/PygameFireEmblem/blob/master/SacaeMap.py
# This
Grass = 0
Tree = 1


textures = {
             Grass : pygame.image.load('Textures/downdload.jpeg'),
             Tree : pygame.image.load('Textures/Tree.png')

           }

# Tilemap
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

