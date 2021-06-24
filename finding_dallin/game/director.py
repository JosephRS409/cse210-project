import arcade
from game.screen import show_screen
from game.player import player

class director():

    def __init__(self):
        self.main()
        self.player = player()
        # Track the current state of what key is pressed
        
    def main(self):
            """ Main method """
            window = show_screen()
            window.setup()

            arcade.run()
