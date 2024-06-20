import time
from pynput import keyboard

import helpers
from player import Player
from map import Map
from enums.directions import Direction

map = Map()
player = Player(map.start_coordinate[0], map.start_coordinate[1])

def keep_in_bounds(direction: Direction):
     if direction == Direction.UP and player.y_coordinate - 1 <= 0:
          return
     elif direction == Direction.DOWN and player.y_coordinate + 1 >= map.max_depth - 1:
          return 
     elif direction == Direction.LEFT and player.x_coordinate - 1 <= 0:
          return 
     elif direction == Direction.RIGHT and player.x_coordinate + 1 >= map.max_width - 1:
          return 
     else:
          return direction
          

def on_press(key):
        helpers.clear_terminal()

        if key == keyboard.Key.up:
            player.move(keep_in_bounds(Direction.UP))
        elif key == keyboard.Key.down:
            player.move(keep_in_bounds(Direction.DOWN))
        elif key == keyboard.Key.left:
            player.move(keep_in_bounds(Direction.LEFT))
        elif key == keyboard.Key.right:
            player.move(keep_in_bounds(Direction.RIGHT))
        elif key == keyboard.Key.esc:
            listener.stop()
        
        map.print_map(
             player.x_coordinate,
             player.y_coordinate,
             player.icon,
             player.noise_level
        )
    
    
with keyboard.Listener(on_press=on_press) as listener:
        while listener.running:
             time.sleep(1)
            
             helpers.clear_terminal() 
             map.print_map(
                 player.x_coordinate,
                 player.y_coordinate,
                 player.icon,
                 noise_level=0
             )

        