import os
'''
PUT PATHS HERE
# '''
PATH = os.path.dirname(os.path.abspath(__file__))
PLAYER_BAT = os.path.join(PATH, "..", "assets", "flying_down.png")
DALLIN = os.path.join(PATH, "..", "assets", "robot.png")
COLLISION_SOUND = os.path.join(PATH, "..", "assets", "sounds", "fall3.wav")
MUSIC = os.path.join(PATH, "..", "assets", "song1.mp3")
MAP = os.path.join(PATH, "..", "assets", "Map.tmx")
END_SCREEN = os.path.join(PATH, "..", "assets", "cat.jpg")

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Finding Dallin"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 2
TILE_SCALING = 2
# COIN_SCALING = 2

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5 # or 10
GRAVITY = 0
# PLAYER_JUMP_SPEED = 20

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.

# pixel margin set for 4:3 ratio
LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 150

# for the background from Bro. Phillips
#? How big does this need to be?
# GRID_PIXEL_SIZE = 1
TILE_SCALING = 1

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
# TILE_SCALING = 0.5
# COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING
