import arcade
from game import constants

class Obstacles(arcade.Sprite):
    
    def __init__(self):
        # IMAGE = "finding_dallin/assets/images/doorClosed_mid.png"
        # Inheriting from "arcade.Sprite"
        # Putting IMAGE in as the argument.
        super().__init__() #IMAGE
        
        # Sets where the avatar starts its position.
        self.center_x = constants.SCREEN_WIDTH/2 + 10
        self.center_y = constants.SCREEN_HEIGHT/2 + 10
        
        # Like the velocity in previous projects.
        self.change_x = 0
        self.change_y = 0
        
    def update(self):
        """ """
        self.center_x += self.change_x
        self.center_y += self.change_y
        
    def collision(self):
        """For when the player collides with the door."""
        pass
        