class Player():

    def __init__(self, position, grid):
        self.position = [position[0], position[1]]
        self.grid = grid
        self.max = len(grid)
        self.inventory = []

    # Usage
    def check_space(self):
        return grid[self.position[0]][self.position[1]]

    # Player Movement
    def move_up(self):
        if self.position[1] > 0:
            self.position[1] -= 1

    def move_down(self):
        if self.position[1] < self.max:
            self.position[1] += 1

    def move_right(self):
        if self.position[0] < self.max:
            self.position[0] += 1

    def move_left(self):
        if self.position[0] > 0:
            self.position[0] -= 1

    def current_position(self):
        print(self.position)
