
import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "DALLIN IS A G"


class show_screen(arcade.Window):

    def __init__(self):

            # Call the parent class and set up the window
            super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

            arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
            self.player_sprite = None
            self.player_list = None

    def setup(self, person):
        """ Set up the game here. Call this function to restart the game. """

        self.player_list = arcade.SpriteList()
        self.player_list.append(person)
        

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        self.player_list.draw()
        # Code to draw the screen goes here

