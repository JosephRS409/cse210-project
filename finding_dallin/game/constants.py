from os import path
# This works as written.
import os
'''
PUT PATHS HERE
# '''

# __file__ refers to the file it's in
# PATH refers to the "game" folder in this case.
# PATH + ../images/robot.png
PATH = os.path.dirname(os.path.abspath(__file__))

# bat = PATH + "\\..\\assets\\flying_down.png"
# print(bat)
# # The above is the same for every OS as follows:
PLAYER_BAT = os.path.join(PATH, "..", "assets", "flying_down.png")
        
# PATH = os.path.dirname(os.path.abspath(__file__))
# BALL_IMAGE = os.path.join(PATH, '..', 'images', 'ball-0.png')
# PADDLE_IMAGE = os.path.join(PATH, '..', 'images', 'paddle-0.png')
# BRICK_IMAGE = os.path.join(PATH, '..', 'images', 'brick-0.png')


# print(__file__)
# # Prints:
# #     c:\Users\default.DESKTOP-P3E3RAC\Documents\School\BYU-I\Spring_2021\2.CSE_210�Programming_with_Classes\project_template\cse210-project\finding_dallin\game\constants.py

# print(PATH)
# # Prints the directory of "constants.py"s directory:
#     # c:\Users\default.DESKTOP-P3E3RAC\Documents\School\BYU-I\Spring_2021\2.CSE_210�Programming_with_Classes\project_template\cse210-project\finding_dallin\game


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
