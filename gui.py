import pygame
from grid import Grid
from astar import astar
from agent import Agent

CELL = 30
WIDTH = 600
HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)


def draw(screen, grid, agent, path):

    for r in range(20):
        for c in range(20):

            rect = pygame.Rect(c*CELL,
                               r*CELL,
                               CELL,
                               CELL)

            color = WHITE

            if grid.grid[r][c] == 1:
                color = BLACK

            pygame.draw.rect(screen,
                             color,
                             rect)

            pygame.draw.rect(screen,
                             (200,200,200),
                             rect,1)

    for node in path:
        pygame.draw.rect(screen,
                         GREEN,
                         (node[1]*CELL,
                          node[0]*CELL,
                          CELL,
                          CELL))

    pygame.draw.rect(screen,
                     RED,
                     (agent.position[1]*CELL,
                      agent.position[0]*CELL,
                      CELL,
                      CELL))


def run_app():

    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    grid = Grid()
    agent = Agent(grid.start)

    path = []

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:
                x,y = pygame.mouse.get_pos()
                grid.toggle_wall(y//CELL,
                                 x//CELL)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    path = astar(grid.grid,
                                 agent.position,
                                 grid.goal)
                    agent.set_path(path)

        agent.move()

        screen.fill(WHITE)
        draw(screen,grid,agent,path)

        pygame.display.update()
        clock.tick(10)

    pygame.quit()