
import arcade
from game import constants
# from game.director import Director



class Over(arcade.View):

    def __init__(self):
        """Shows the game over screen"""
        super().__init__()
        self.texture = arcade.load_texture(constants.END_SCREEN)
        # self.director = Director
    def setup(self):
        pass

    def on_draw(self):
        """Draws the items"""
        arcade.start_render()
        arcade.set_viewport(0, 800, 0, 600)
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("You Found Dallin!", constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2, arcade.color.RED, font_size=50, anchor_x="center")
        arcade.draw_text("RIP Dallin :'(", constants.SCREEN_WIDTH * (3/4),
                         constants.SCREEN_HEIGHT * (3/4), arcade.color.DEEP_MAGENTA, font_size=12, anchor_x="center")
