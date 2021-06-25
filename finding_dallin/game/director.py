import arcade
from game.screen import Show_screen
from game.player import Player

class Director():

    def __init__(self):
        self.main()
        self.player = Player()
        # Track the current state of what key is pressed
        
    def main(self):
            """ Main method """
            # Class for displaying the screen.
            window = Show_screen()
            # And its method.
            window.setup()

            arcade.run()
