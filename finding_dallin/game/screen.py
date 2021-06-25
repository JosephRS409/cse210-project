# import tkinter as tk
import arcade
from game import constants
from game.player import Player


# Commented out till we figure out the background/full-screen mechanism.
# width = tk.Tk().winfo_screenwidth()
# height = tk.Tk().winfo_screenheight()

# Replaced by Constants class
# width = 800
# height = 600
# SCREEN_WIDTH = width
# SCREEN_HEIGHT = height
# SCREEN_TITLE = "DALLIN IS A G"

class Show_screen(arcade.Window):

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.background = "finding_dallin\\assets\\cat.jpg"
        self.player_sprite = None
        self.player_list = None
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        self.player = Player()
        
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
        
        # Our physics engine
        # self.physics_engine = None

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
        
        """ Movement and game logic """

        # Move the player with the physics engine
        # self.physics_engine.update()


        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + constants.LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)

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
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
        
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        
        # # Set up the player, specifically placing it at these coordinates.
        image_source = "finding_dallin\\assets\\flying_down.png"
        self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
        # self.player_sprite.center_x = 64
        # self.player_sprite.center_y = 96
        # self.player_list.append(self.player_sprite)
        
        self.background = arcade.load_texture("finding_dallin\\assets\\cat.jpg" )
        

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(200, 0,
                                            constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT,
                                            self.background)
        self.player_list.draw()

        # Code to draw the screen goes here

