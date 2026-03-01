import heapq
from heuristics import manhattan


def gbfs(grid, start, goal):

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    visited = set()

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        visited.add(current)

        r, c = current

        neighbors = [
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1)
        ]

        for n in neighbors:

            nr, nc = n

            if nr < 0 or nc < 0 or nr >= 20 or nc >= 20:
                continue

            if grid[nr][nc] == 1:
                continue

            if n in visited:
                continue

            priority = manhattan(n, goal)

            heapq.heappush(open_set,
                           (priority, n))

            came_from[n] = current

    return []