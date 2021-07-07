import arcade
from game import constants


class Over(arcade.View):

    def __init__(self):
        super().__init__()

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.GRAY)
        arcade.draw_text("You Suck", constants.SCREEN_WIDTH / 2,
                         constants.SCREEN_HEIGHT/2, arcade.color.CRIMSON, font_size=50, anchor_x="center")
        arcade.draw_text("Go Die", constants.SCREEN_WIDTH / 2,
                         constants.SCREEN_HEIGHT/2 - 50, arcade.color.CRIMSON, font_size=20, anchor_x="center")

