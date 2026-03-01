from node import Node

def create_grid(rows,width):
    grid=[]
    gap=width//rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node=Node(i,j,gap)
            grid[i].append(node)

    return grid