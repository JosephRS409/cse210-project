from PIL.Image import Image
import arcade
class player(arcade.Sprite):

    def __init__(self):
        IMAGE = "finding_dallin\\assets\\robot.png"
        super().__init__(IMAGE)

        self.center_x = 50
        self.center_y = 50
