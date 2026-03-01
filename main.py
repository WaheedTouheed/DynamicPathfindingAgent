import pygame
import random
from grid import create_grid
from algorithms import astar,gbfs

WIDTH=600
WIN=pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Dynamic Pathfinding Agent")

ROWS=30

def draw(win,grid):
    win.fill((255,255,255))

    for row in grid:
        for node in row:
            node.draw(win)

    pygame.display.update()


def random_obstacle(grid,prob=0.02):
    for row in grid:
        for node in row:
            if random.random()<prob:
                node.make_wall()


def main():
    grid=create_grid(ROWS,WIDTH)

    start=grid[0][0]
    goal=grid[ROWS-1][ROWS-1]

    start.make_start()
    goal.make_goal()

    run=True

    while run:
        draw(WIN,grid)

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                run=False

            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_a:
                    astar(lambda:draw(WIN,grid),
                          grid,start,goal)

                if event.key==pygame.K_g:
                    gbfs(lambda:draw(WIN,grid),
                         grid,start,goal)

                if event.key==pygame.K_d:
                    random_obstacle(grid)

    pygame.quit()

main()