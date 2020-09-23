from random import random, randint, triangular

class Board():
    # Diamond, Emerald, Ruby
    ORES = ['D', 'E', 'R']

    def __init__(self, size):
        self.size = size
        self.ore_locations = [int(triangular(0, self.size, self.size//2)) for i in range(self.size)]
        self.grid = None

    def generate(self):
        grid = []
        for row in range(self.size):
            # Creates new row
            grid.append([])
            for column in range(self.size):
                # Adds the powerstations to the center of the grid
                if (row == self.size//2 - 1 or row == self.size//2) \
                    and (column == self.size//2 - 1 or column == self.size//2):
                    grid[row].append('P')

                # Adds the autominers to the top of the grid
                elif row == 1 and (column == 1 or column == self.size - 2):
                    grid[row].append('A')

                # Adds the markets in the mid corners
                # (∇, Δ) == (red, blue)
                elif (row == self.size // 4 or row == (self.size // 4)*3) \
                        and (column == self.size // 4 or column == (self.size // 4) * 3):
                        # Specific Positions
                        if row == self.size // 4 and column == self.size // 4:
                            grid[row].append('∇')

                        if row == self.size // 4 and column == (self.size // 4) * 3:
                            grid[row].append('Δ')

                        if row == (self.size // 4) * 3 and column == self.size // 4:
                            grid[row].append('Δ')

                        if row == (self.size // 4)*3 and column == (self.size // 4) * 3:
                            grid[row].append('∇')

                # Fill in the rest with blank space
                else:
                    if random() > 0.5 and self.ore_locations[row] != 0:
                        grid[row].append(Board.ORES[randint(0, len(Board.ORES)-1)])
                        self.ore_locations[row] -= 1
                    else:
                        grid[row].append(' ')
        self.grid = grid

    def display(self):
        # Easy to read output
        print(f'Grid Size: {self.size}')
        print('Grid:')
        [print(i) for i in self.grid]
