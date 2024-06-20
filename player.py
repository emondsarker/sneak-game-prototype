import time
from enums.noise_levels import NoiseLevel as NL
from enums.directions import Direction

class Player:
    name = ""
    icon = "?"

    initialTime = time.time()
    timeSinceLastMovement = initialTime

    noise_level = NL.NONE
    
    x_coordinate = -1
    y_coordinate = -1

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.name = input("Enter your name: ")
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.icon = self.name[0].capitalize()

    def calculateNoiseLevel(self):
        time_delta = time.time() - self.timeSinceLastMovement
        self.timeSinceLastMovement = time.time()

        if time_delta > 1.0:
            self.noise_level = NL.LOW
        elif time_delta > 0.5:
            self.noise_level = NL.MEDIUM
        else:
            self.noise_level = NL.HIGH
    
    def move(self, direction: Direction):
        self.calculateNoiseLevel()
        print(
            self.name, "moved", direction,
            "noise level", self.noise_level,
            "time delta", self.noise_level
            )
        
        if direction == Direction.UP:
            self.y_coordinate -= 1
        elif direction == Direction.DOWN:
            self.y_coordinate += 1
        elif direction == Direction.LEFT:
            self.x_coordinate -= 1
        elif direction == Direction.RIGHT:
            self.x_coordinate += 1
        
        
        
        
        
