from PIL.Image import Image
import arcade
class Player(arcade.Sprite):

    def __init__(self):
        # IMAGE = "finding_dallin\\assets\\robot.png"
        IMAGE = "finding_dallin\\assets\\flying_down.png"
        super().__init__(IMAGE)

        self.center_x = 50
        self.center_y = 50

