import arcade
from game import constants


class Player(arcade.Sprite):

    def __init__(self):
        """Sets up the player sprite"""
        super().__init__(constants.PLAYER_BAT, .4)

        self.center_x = 100
        self.center_y = 6300
        self.change_x = 0
        self.change_y = 0
        self.keys = []

    def update(self):
        """ Move the player """
        # Move player.
        self.center_x += self.change_x
        self.center_y += self.change_y
