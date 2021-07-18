import arcade
import random as r
from game import constants

class Dallin(arcade.Sprite):

    def __init__(self):
        """Sets up the Dallin spritee in a random location on the map"""
        super().__init__(constants.DALLIN)

        # self.center_y = 3100
        # self.center_x = 100

        self.center_x = r.randint(100, 6300)
        self.center_y = r.randint(100, 6300)

    
