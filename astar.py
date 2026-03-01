import heapq
from heuristics import manhattan


def astar(grid, start, goal):

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        r, c = current

        neighbors = [
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1)
        ]

        for nr, nc in neighbors:

            if nr < 0 or nc < 0 or nr >= 20 or nc >= 20:
                continue

            if grid[nr][nc] == 1:
                continue

            new_cost = g_cost[current] + 1

            if (nr, nc) not in g_cost or new_cost < g_cost[(nr, nc)]:
                g_cost[(nr, nc)] = new_cost

                priority = new_cost + manhattan((nr, nc), goal)
                heapq.heappush(open_set,
                               (priority, (nr, nc)))

                came_from[(nr, nc)] = current

    return []