import arcade
import random as r
class Dallin(arcade.Sprite):

    def __init__(self):
        super().__init__("finding_dallin\\assets\\robot.png")

        self.center_y = 3100
        self.center_x = 100

        # self.center_x = r.randint(100, 3100)
        # self.center_y = r.randint(100, 3100)

    
