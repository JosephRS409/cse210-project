import arcade
from game import constants
class Player(arcade.Sprite):

    def __init__(self):        
        # Not this (which is for Window OS):
        # IMAGE = "finding_dallin\\assets\\robot.png"
        
        # # This works on any OS.
        # bat = constants.PATH + "/../assets/flying_down.png"
        # # Better to do it this way:
        super().__init__(constants.PLAYER_BAT)
        
        # Sets where the avatar starts its position.
        # self.center_x = constants.SCREEN_WIDTH/2
        # self.center_y = constants.SCREEN_HEIGHT/2
        self.center_x = 200
        self.center_y = 3100
        
        self.change_x = 0
        self.change_y = 0
        self.keys = []


    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        #     Check for out-of-bounds
        # if self.left < 0:
        #             self.left = 0
        # elif self.right > SCREEN_WIDTH - 1:
        #             self.right = SCREEN_WIDTH - 1

        # if self.bottom < 0:
        #             self.bottom = 0
        # elif self.top > SCREEN_HEIGHT - 1:
        #             self.top = SCREEN_HEIGHT - 1