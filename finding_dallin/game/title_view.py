
import arcade
from game import constants
from game.dallin import Dallin
from game.screen import Show_screen

class Title(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.texture = arcade.load_texture(constants.DALLIN)
        self.top = 100
        self.bottom = 100

    def setup(self):
        pass

    def on_update(self, delta_time):
        self.top += 5
        # self.bottom += 5
        if self.top == 800:
            self.top = 0
        # if self
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Finding Dallin", constants.SCREEN_WIDTH / 2,
                         constants.SCREEN_HEIGHT/2, arcade.color.CRIMSON, font_size=50, anchor_x="center")
        arcade.draw_text("Joseph, Alan, Austin", constants.SCREEN_WIDTH / 2,
                         constants.SCREEN_HEIGHT/2 - 50, arcade.color.CRIMSON, font_size=20, anchor_x="center")
        self.texture.draw_sized(self.top,self.bottom,64,64)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        show_view = Show_screen()
        self.window.clear()
        show_view.setup()
        self.window.show_view(show_view)
