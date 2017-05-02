import pygame
import random

#PURPOSE - To build mazes easily for games.
#index of 0 = up
#index of 1 = left
#index of 2 = down
#index of 3 = right

class Node:
    def __init__(self, row=-1, column=-1):
        self.holes = [False,False,False,False]
        self.neighbors = [-1,-1,-1,-1]
        self.row = row
        self.column = column

    def addHole(self,direction):
        self.holes[direction] = True

class Grid:
    def __init__(self, width=30, height=30):
        self.nodes = [[Node()] * width] * height]
        for n in range(0,width-1):
            for m in range(0,height-1):
                self.nodes[n,m].row = n
                self.nodes[n,m].column = m



        
def buildMaze(grid):
    seed()
    #wip
    
    
        

        
    
