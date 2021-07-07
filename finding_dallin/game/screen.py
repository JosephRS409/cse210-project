# import tkinter as tk
import arcade
from game import constants
from game.player import Player
from game.obstacles import Obstacles
from game.game_over import Over
from game.dallin import Dallin


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "DALLIN IS A G"

# Commented out till we figure out the background/full-screen mechanism.
# width = tk.Tk().winfo_screenwidth()
# height = tk.Tk().winfo_screenheight()


# Replaced by Constants class
# width = 800
# height = 600
# SCREEN_WIDTH = width
# SCREEN_HEIGHT = height
# SCREEN_TITLE = "DALLIN IS A G"

class Show_screen(arcade.View):

    def __init__(self):

    # This calls the parent class to set up the window
        super().__init__()
    # And color
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # self.background = "finding_dallin\\assets\\cat.jpg"
        self.background = arcade.csscolor.TAN
        
    # Initialize
        self.player_sprite = None
    # Why do we have a list for player?
        self.player_list = None
        self.enemy_list = None
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.left = 0
        self.right = 600
        self.top = 3200
        self.bottom = 2600

    # Initialize the player class here. (To use it!)
        self.player = Player()
        self.dallin = Dallin()
    
    # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
        
    # Initialize the objects. e.g. "door"
    # ? Why do these work?
        self.door = Obstacles()
        self.wall = Obstacles()
        self.enemy = Obstacles()
        
    # Initialize the background and objects.
        self.wall_list = None
        self.door_list = None
        self.key_list = None
        self.background_list = None
                            
    # Our physics engine
        self.physics_engine = None
        # self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
        #                                                      self.wall_list,
        #                                                      gravity_constant=0)

    # ? Why is "delta_time" here?
    def on_update(self, delta_time):
        """ Player avatar position, movement speed,
        game logic, and view port"""
        # Calculate speed based on the keys pressed
        self.player.change_x = 0
        self.player.change_y = 0
        # This is how fast the character moves.
        MOVEMENT_SPEED_X = 6
        MOVEMENT_SPEED_Y = 8
        # 
        if self.up_pressed and not self.down_pressed:
            self.player.change_y = MOVEMENT_SPEED_Y
        elif self.down_pressed and not self.up_pressed:
            self.player.change_y = -MOVEMENT_SPEED_Y
        if self.left_pressed and not self.right_pressed:
            self.player.change_x = -MOVEMENT_SPEED_X
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x = MOVEMENT_SPEED_X
        

        if self.player.center_x <= (self.left + 100):
            self.right -= 6
            self.left -= 6
        elif self.player.center_y <= (self.bottom +100):
            self.top -= 8
            self.bottom -= 8
        elif self.player.center_x >= (self.right -100):
            self.right += 6
            self.left += 6
        elif self.player.center_y >= (self.top -100):
            self.top += 8
            self.bottom += 8

        sound = arcade.load_sound("finding_dallin\\assets\sounds\\fall3.wav")
        # if self.player.center_x >= 1000:
        #     self.player.center_x = 990
        #     arcade.play_sound(sound)
        # elif self.player.center_x <= 0:
        #     self.player.center_x = 10
        #     # sound = arcade.load_sound("finding_dallin\\assets\sounds\\fall3.wav")
        #     arcade.play_sound(sound)
        # elif self.player.center_y >= 2000:
        #     self.player.center_y = 1990
        #     # sound = arcade.load_sound("finding_dallin\\assets\sounds\\fall3.wav")
        #     arcade.play_sound(sound)
        # elif self.player.center_y <= 0:
        #     self.player.center_y = 10
        #     # sound = arcade.load_sound("finding_dallin\\assets\sounds\\fall3.wav")
        #     arcade.play_sound(sound)
        # for wall in self.wall_list:
        #     print(wall.center_x)
        #     if self.player.center_x == wall.center_x:
        #         # self.player.center_x = wall.center_x - 200
        #         print("yeet")
        wall_hit = arcade.check_for_collision_with_list(self.player, self.wall_list)
        for wall in wall_hit:
            if wall.center_y > self.player.center_y:
                self.player.center_y -= 5
                arcade.play_sound(sound)
            elif wall.center_y < self.player.center_y:
                self.player.center_y += 5
                arcade.play_sound(sound)
            if wall.center_x > self.player.center_x:
                self.player.center_x -= 5
                arcade.play_sound(sound)
            elif wall.center_x < self.player.center_x:
                self.player.center_x += 5
                arcade.play_sound(sound)
           
        door_hit = arcade.check_for_collision_with_list(self.player, self.door_list)
        for door in door_hit:
            if "room_key" in self.player.keys:
                self.door_list.remove(door)
            else:
                if door.center_y > self.player.center_y:
                    self.player.center_y -= 5
                elif door.center_y < self.player.center_y:
                    self.player.center_y += 5
                if door.center_x > self.player.center_x:
                    self.player.center_x -= 5
                elif door.center_x < self.player.center_x:
                    self.player.center_x += 5

        key_hit = arcade.check_for_collision_with_list(self.player, self.key_list)
        for key in key_hit:
            self.key_list.remove(key)
            self.player.keys.append("room_key")
            

        dallin_hit = arcade.check_for_collision(self.player, self.dallin)
        if dallin_hit:
            show_view = Over()
            show_view.setup()
            self.window.show_view(show_view)
        # # This is what we see on screen.
        arcade.set_viewport(self.left, self.right, self.bottom, self.top)

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

            # Does the scrolling
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. 
        The "Controls," if you will. """

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
        
        # Makes the character
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        self.player_list.append(self.dallin)
                # self.player_list.append(self.enemy)
        
        # self.enemy_list = arcade.SpriteList()
        # self.enemy_list.append(self.enemy)
        # Makes our door
        # ? Do we need this with the background as it is?
        # self.door_list = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        # door = "finding_dallin/assets/images/doorClosed_mid.png"
        # self.door_list.append(self.door)
        
        # # Set up the player, specifically placing it at these coordinates.
        image_source = "finding_dallin\\assets\\flying_down.png"
        self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
        # self.player_sprite.center_x = 64
        # self.player_sprite.center_y = 96
        # self.player_list.append(self.player_sprite)
        
        # self.background = arcade.load_texture("finding_dallin\\assets\\cat.jpg" )
        self.background = arcade.csscolor.TAN
        
        
        
        
        # Now for the background.       
        map_name = "finding_dallin/assets/test.tmx"
        
        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)
        self.end_of_map = my_map.map_size.width * constants.GRID_PIXEL_SIZE
        # --- Wall Layer ---
        self.wall_list = arcade.tilemap.process_layer(my_map,
                                                      'walls',
                                                      constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        self.door_list = arcade.tilemap.process_layer(my_map,
                                                      'doors',
                                                      constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        self.key_list = arcade.tilemap.process_layer(my_map,
                                                      'keys',
                                                      constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        self.background_list = arcade.tilemap.process_layer(my_map,
                                                     'background',
                                                     constants.TILE_SCALING,
                                                     use_spatial_hash=True)
        # --- Coins ---
        # self.coin_list = arcade.tilemap.process_layer(my_map,
        #                                               'Coins',
        #                                               TILE_SCALING,
        #                                               use_spatial_hash=True)
        
        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)
        
        #             # --- Other stuff
        # # Set the background color
        # if self.tile_map.tiled_map.background_color:
        #     arcade.set_background_color(self.tile_map.tiled_map.background_color)

        # Keep player from running through the wall_list layer
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=constants.GRAVITY) 
       
       
    #    2.5.7
        # map_name = "finding_dallin\assets\map_basic.json"
        
        # # Layer Specific Options for the Tilemap
        # layer_options = {
        #     "wall Tile Layer": {
        #         "use_spatial_hash": True,
        #     },
        # }
        
        # # Read in the tiled map
        # self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # # Initialize Scene with our TileMap, this will automatically add all layers
        # # from the map as SpriteLists in the scene in the proper order.
        # self.scene = arcade.Scene.from_tilemap(self.tile_map)
        
    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()

        # arcade.draw_lrwh_rectangle_textured(0, 0,
        #                                     1000, 2000,
        #                                     self.background)
        
        arcade.draw_lrtb_rectangle_filled(0, 1000, 2000, 0, (210, 180, 140))
        
        self.background_list.draw()
        self.wall_list.draw()
        self.door_list.draw()
        self.key_list.draw()
        # self.enemy_list.draw()
        self.player_list.draw()
        # self.door.draw()

        # Code to draw the screen goes here

