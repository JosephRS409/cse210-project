import tkinter as tk
import arcade

# width = tk.Tk().winfo_screenwidth()
# height = tk.Tk().winfo_screenheight()
width = 800
height = 600

SCREEN_WIDTH = width
SCREEN_HEIGHT = height
SCREEN_TITLE = "DALLIN IS A G"


class Show_Screen(arcade.Window):

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

