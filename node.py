import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)

class Node:
    def __init__(self,row,col,size):
        self.row=row
        self.col=col
        self.x=row*size
        self.y=col*size
        self.color=WHITE
        self.neighbors=[]
        self.size=size

    def draw(self,win):
        pygame.draw.rect(win,self.color,
                        (self.x,self.y,self.size,self.size))

    def make_wall(self):
        self.color=BLACK

    def make_start(self):
        self.color=BLUE

    def make_goal(self):
        self.color=GREEN

    def make_visited(self):
        self.color=RED

    def make_frontier(self):
        self.color=YELLOW