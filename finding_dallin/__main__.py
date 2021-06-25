# program entry point
import arcade
from game.screen import Show_Screen


from game.player import Player #Like the Paddle
# from game.output_service import ArcadeOutputService




def main():
    """ Main method """
    
    
    
    window = Show_Screen()
    person = Player()
    window.setup(person)
    arcade.run()

main()
