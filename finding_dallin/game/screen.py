
import arcade
from game import constants
from game.player import Player
from game.obstacles import Obstacles
from game.game_over import Over
from game.dallin import Dallin


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "DALLIN IS A G"


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
        self.right = 800
        self.top = 6400
        self.bottom = 5800

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
                            
    # ? Why is "delta_time" here?
    def on_update(self, delta_time):
        """ Player avatar position, movement speed,
        game logic, and view port"""
        # Calculate speed based on the keys pressed
        self.player.change_x = 0
        self.player.change_y = 0
        # This is how fast the character moves.
        MOVEMENT_SPEED_X = 8
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
            self.right -= 8
            self.left -= 8
        if self.player.center_y <= (self.bottom +100):
            self.top -= 8
            self.bottom -= 8
        if self.player.center_x >= (self.right -100):
            self.right += 8
            self.left += 8
        if self.player.center_y >= (self.top -100):
            self.top += 8
            self.bottom += 8

        sound = arcade.load_sound(constants.COLLISION_SOUND)
        
        wall_hit = arcade.check_for_collision_with_list(self.player, self.wall_list)
        for wall in wall_hit:
            if wall.center_y > self.player.center_y:
                self.player.center_y -= 6
                arcade.play_sound(sound)
            if wall.center_y < self.player.center_y:
                self.player.center_y += 6
                arcade.play_sound(sound)
            if wall.center_x > self.player.center_x:
                self.player.center_x -= 6
                arcade.play_sound(sound)
            if wall.center_x < self.player.center_x:
                self.player.center_x += 6
                arcade.play_sound(sound)

        door_hit = arcade.check_for_collision_with_list(self.player, self.gold_door)
        for door in door_hit:
            if 1 in self.player.keys:
                self.gold_door.remove(door)
            else:
                if door.center_y > self.player.center_y:
                    self.player.center_y -= 5
                elif door.center_y < self.player.center_y:
                    self.player.center_y += 5
                if door.center_x > self.player.center_x:
                    self.player.center_x -= 5
                elif door.center_x < self.player.center_x:
                    self.player.center_x += 5


        door_hit = arcade.check_for_collision_with_list(self.player, self.red_door)
        for door in door_hit:
            if 2 in self.player.keys:
                self.red_door.remove(door)
            else:
                if door.center_y > self.player.center_y:
                    self.player.center_y -= 5
                elif door.center_y < self.player.center_y:
                    self.player.center_y += 5
                if door.center_x > self.player.center_x:
                    self.player.center_x -= 5
                elif door.center_x < self.player.center_x:
                    self.player.center_x += 5
        door_hit = arcade.check_for_collision_with_list(self.player, self.green_door)
        for door in door_hit:
            if 3 in self.player.keys:
                self.green_door.remove(door)
            else:
                if door.center_y > self.player.center_y:
                    self.player.center_y -= 5
                elif door.center_y < self.player.center_y:
                    self.player.center_y += 5
                if door.center_x > self.player.center_x:
                    self.player.center_x -= 5
                elif door.center_x < self.player.center_x:
                    self.player.center_x += 5

        door_hit = arcade.check_for_collision_with_list(self.player, self.blue_door)
        for door in door_hit:
            if 4 in self.player.keys:
                self.blue_door.remove(door)
            else:
                if door.center_y > self.player.center_y:
                    self.player.center_y -= 5
                elif door.center_y < self.player.center_y:
                    self.player.center_y += 5
                if door.center_x > self.player.center_x:
                    self.player.center_x -= 5
                elif door.center_x < self.player.center_x:
                    self.player.center_x += 5
            

        keys = [self.gold_key,self.red_key,self.green_key,self.blue_key]
        m = 1
        for key in keys:
            key_hit = arcade.check_for_collision_with_list(self.player, key)
            for k in key_hit:
                key.remove(k)
                self.player.keys.append(m)
            
            m += 1
            

        dallin_hit = arcade.check_for_collision(self.player, self.dallin)
        if dallin_hit:
            show_view = Over()
            # show_view.setup()
            self.window.show_view(show_view)
        # # This is what we see on screen.
        arcade.set_viewport(self.left, self.right, self.bottom, self.top)

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        self.player.update()
        
        """ Movement and game logic """

        # --- Manage Scrolling ---


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
        
        # Adds sprites to list
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        self.player_list.append(self.dallin)
        
        print(self.dallin.center_x, self.dallin.center_y)
        
        music = arcade.load_sound(constants.MUSIC)
        arcade.play_sound(music, .5, looping=True)

        # Now for the background.               
        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(constants.MAP)
        # self.end_of_map = my_map.map_size.width * constants.GRID_PIXEL_SIZE
        # --- Wall Layer ---
        self.wall_list = arcade.tilemap.process_layer(my_map,
                                                      'Walls',
                                                      constants.TILE_SCALING,
                                                      use_spatial_hash=True)
                                                    
        self.gold_door = arcade.tilemap.process_layer(my_map,
                                                      'Gold doors',
                                                      constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        self.gold_key = arcade.tilemap.process_layer(my_map,
                                                      'Gold key',
                                                      constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        self.blue_door = arcade.tilemap.process_layer(my_map,
                                                      'Blue door',
                                                      constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        self.blue_key = arcade.tilemap.process_layer(my_map,
                                                     'Blue Key',
                                                     constants.TILE_SCALING,
                                                     use_spatial_hash=True)
        self.green_door = arcade.tilemap.process_layer(my_map,
                                                      'Green door',
                                                      constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        self.green_key = arcade.tilemap.process_layer(my_map,
                                                     'Green Key',
                                                     constants.TILE_SCALING,
                                                     use_spatial_hash=True)
        self.red_door = arcade.tilemap.process_layer(my_map,
                                                      'Red door',
                                                      constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        self.red_key = arcade.tilemap.process_layer(my_map,
                                                     'Red Key',
                                                     constants.TILE_SCALING,
                                                     use_spatial_hash=True)
        self.deco = arcade.tilemap.process_layer(my_map,
                                                 'Decorations',
                                                 constants.TILE_SCALING,
                                                 use_spatial_hash=True)
        self.background_list = arcade.tilemap.process_layer(my_map,
                                                     'Floor',
                                                     constants.TILE_SCALING,
                                                     use_spatial_hash=True)
        
        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)
        

        # Keep player from running through the wall_list layer
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=constants.GRAVITY) 
       

        
    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        
        self.background_list.draw()
        self.wall_list.draw()
        self.gold_door.draw()
        self.blue_door.draw()
        self.red_door.draw()
        self.green_door.draw()
        self.green_key.draw()
        self.blue_key.draw()
        self.red_key.draw()
        self.gold_key.draw()
        self.deco.draw()
        self.player_list.draw()

        # Code to draw the screen goes here

