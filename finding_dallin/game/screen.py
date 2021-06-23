import tkinter as tk
import arcade
from game.player import player

width = tk.Tk().winfo_screenwidth()
height = tk.Tk().winfo_screenheight()

SCREEN_WIDTH = width
SCREEN_HEIGHT = height
SCREEN_TITLE = "DALLIN IS A G"


class show_screen(arcade.Window):

    def __init__(self):

            # Call the parent class and set up the window
            super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

            arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
            self.player_sprite = None
            self.player_list = None
            self.left_pressed = False
            self.right_pressed = False
            self.up_pressed = False
            self.down_pressed = False
            self.player = player()

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Calculate speed based on the keys pressed
        self.player.change_x = 0
        self.player.change_y = 0
        MOVEMENT_SPEED = 3
        if self.up_pressed and not self.down_pressed:
            self.player.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x = MOVEMENT_SPEED

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        self.player.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        self.player_list.draw()
        # Code to draw the screen goes here

