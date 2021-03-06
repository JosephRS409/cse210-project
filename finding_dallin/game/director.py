import arcade
from game.title_view import Title
from game.player import Player
from game import constants

class Director():

    def __init__(self):
        """Directs the game"""
        self.window = arcade.Window(
            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        self.main()
        self.player = Player()
        # Track the current state of what key is pressed
        
    def main(self):
            """ Main method """
            # Class for displaying the screen.
            start_view = Title()

            self.window.show_view(start_view)
            arcade.run()
