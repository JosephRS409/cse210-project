
import arcade
from game import constants
from game.game_over import Over
from game.screen import Show_screen

class Title(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.number = 1

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Finding Dallin", constants.SCREEN_WIDTH / 2,
                         constants.SCREEN_HEIGHT/2, arcade.color.CRIMSON, font_size=50, anchor_x="center")
        arcade.draw_text("Joseph, Alan, Austin", constants.SCREEN_WIDTH / 2,
                         constants.SCREEN_HEIGHT/2 - 50, arcade.color.CRIMSON, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        show_view = Show_screen()
        self.window.clear()
        show_view.setup()
        self.window.show_view(show_view)
