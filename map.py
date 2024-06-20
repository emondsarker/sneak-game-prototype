import copy

from enums.noise_levels import NoiseLevel


class Map:

    start_coordinate = (4,2)

    initial_layout =[
        ["#"]*25,
        ["#"]+[" "]*23+["#"],
        ["#"]+[" "]*23+["#"],
        ["#"]+[" "]*23+["#"],
        ["#"]+[" "]*23+["#"],
        ["#"]+[" "]*23+["#"],
        ["#"]+[" "]*23+["#"],
        ["#"]+[" "]*23+["#"],
        ["#"]*25,
    ]
    layout = initial_layout

    max_depth = len(layout)
    max_width = len(layout[0])

    def __init__(self):
        pass

    def draw_noise(self, x_coordinate, y_coordinate, noise_level: NoiseLevel):
        try:
            if noise_level.value > 0:
                for i in range(noise_level.value):
                    # up and down
                    self.layout[y_coordinate+i][x_coordinate] = "!"
                    self.layout[y_coordinate-i][x_coordinate] = "!"
                    # left and right
                    self.layout[y_coordinate][x_coordinate+i] = "!"
                    self.layout[y_coordinate][x_coordinate-i] = "!"
                    # diagonal
                    self.layout[y_coordinate+i][x_coordinate+i] = "!"
                    self.layout[y_coordinate+i][x_coordinate-i] = "!"
                    self.layout[y_coordinate-i][x_coordinate+i] = "!"
                    self.layout[y_coordinate-i][x_coordinate-i] = "!"
        except:
            pass

    def draw_boundary(self):
        for i in range(self.max_depth):
            for j in range(self.max_width):
                if self.initial_layout[i][j] == "#":
                    self.layout[i][j] = "#"
    
    def print_map(self, x_coordinate, y_coordinate, icon, noise_level):
        self.layout = copy.deepcopy(self.initial_layout)
        
        self.draw_noise(x_coordinate, y_coordinate, noise_level)
        self.layout[y_coordinate][x_coordinate] = icon
        self.draw_boundary()
        
        for line in self.layout:
            for char in line:
                print(char, end="", flush=True)
            print(flush=True)
    
        
            