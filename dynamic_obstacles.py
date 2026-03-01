import random


def spawn_obstacle(grid):

    if random.random() < 0.05:

        r = random.randint(0, 19)
        c = random.randint(0, 19)

        if grid[r][c] == 0:
            grid[r][c] = 1