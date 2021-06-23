# program entry point
import arcade
from game.screen import show_screen
from game.player import player
# from game.output_service import ArcadeOutputService




def main():
    """ Main method """
    window = show_screen()
    person = player()
    window.setup(person)
    arcade.run()

main()
