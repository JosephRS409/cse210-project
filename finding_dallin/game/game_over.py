
import arcade
from game import constants


class Over(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("finding_dallin\\assets\\cat.jpg")
    def setup(self):
        pass

    def on_draw(self):

        arcade.start_render()
        arcade.set_viewport(0, 800, 0, 600)
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("You Found Dallin!", constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2, arcade.color.RED, font_size=50, anchor_x="center")
