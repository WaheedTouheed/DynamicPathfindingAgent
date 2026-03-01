def heuristic(a,b):
    return abs(a.row-b.row)+abs(a.col-b.col)

from queue import PriorityQueue
import time

def astar(draw,grid,start,end):

    open_set=PriorityQueue()
    open_set.put((0,start))

    came_from={}
    g_score={node:float("inf") for row in grid for node in row}
    g_score[start]=0

    f_score={node:float("inf") for row in grid for node in row}
    f_score[start]=heuristic(start,end)

    visited_nodes=0
    start_time=time.time()

    while not open_set.empty():

        current=open_set.get()[1]
        visited_nodes+=1

        if current==end:
            exec_time=(time.time()-start_time)*1000
            return visited_nodes,exec_time

        for neighbor in current.neighbors:

            temp_g=g_score[current]+1

            if temp_g<g_score[neighbor]:
                came_from[neighbor]=current
                g_score[neighbor]=temp_g
                f_score[neighbor]=temp_g+heuristic(neighbor,end)

                open_set.put((f_score[neighbor],neighbor))
                neighbor.make_frontier()

        draw()
        current.make_visited()

    return None


def gbfs(draw,grid,start,end):

    open_set=PriorityQueue()
    open_set.put((0,start))

    visited=set()
    visited_nodes=0

    while not open_set.empty():

        current=open_set.get()[1]
        visited_nodes+=1

        if current==end:
            return visited_nodes

        visited.add(current)

        for neighbor in current.neighbors:
            if neighbor not in visited:
                h=heuristic(neighbor,end)
                open_set.put((h,neighbor))
                neighbor.make_frontier()

        draw()
        current.make_visited()