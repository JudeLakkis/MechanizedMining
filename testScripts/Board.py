from random import random, randint, triangular

# Diamond, Emerald, Ruby
ORES = ['D', 'E', 'R']
SIZE = 14
ore_locations = [int(triangular(0, SIZE, SIZE//2)) for i in range(SIZE)]
grid = []

for row in range(SIZE):
    grid.append([])
    for column in range(SIZE):
        # Adds the powerstations to the center of the grid
        if (row == SIZE//2 - 1 or row == SIZE//2) \
            and (column == SIZE//2 - 1 or column == SIZE//2):
            grid[row].append('P')

        # Adds the autominers to the top of the grid
        elif row == 1 and (column == 1 or column == SIZE - 2):
            grid[row].append('A')

        # Adds the markets in the mid corners
        # (∇, Δ) == (red, blue)
        elif (row == SIZE // 4 or row == (SIZE // 4)*3) \
                and (column == SIZE // 4 or column == (SIZE // 4) * 3):
                if row == SIZE // 4 and column == SIZE // 4:
                    grid[row].append('∇')

                if row == SIZE // 4 and column == (SIZE // 4) * 3:
                    grid[row].append('Δ')

                if row == (SIZE // 4) * 3 and column == SIZE // 4:
                    grid[row].append('Δ')

                if row == (SIZE // 4)*3 and column == (SIZE // 4) * 3:
                    grid[row].append('∇')

        else:
            if random() > 0.5 and ore_locations[row] != 0:
                grid[row].append(ORES[randint(0, len(ORES)-1)])
                ore_locations[row] -= 1
            else:
                grid[row].append(' ')

# Visuals
[print(i) for i in grid]
