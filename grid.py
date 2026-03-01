ROWS = 20
COLS = 20

EMPTY = 0
WALL = 1
START = 2
GOAL = 3


class Grid:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(COLS)]
                     for _ in range(ROWS)]

        self.start = (0, 0)
        self.goal = (ROWS - 1, COLS - 1)

    def toggle_wall(self, row, col):
        if self.grid[row][col] == WALL:
            self.grid[row][col] = EMPTY
        else:
            self.grid[row][col] = WALL