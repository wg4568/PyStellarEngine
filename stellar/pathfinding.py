import pygame
import math
import tools

class Node:
    def __init__(self):
        self.neighbors=[]
        self.moveCosts=[]
        self.blocked = False
        self.x = 0
        self.y = 0
        self.fScore= 0
        self.gScore= 0
        self.moveScore= 0
        self.parent= None
        self.child= None
      
class Grid:
    def __init__(self):
        self.nodes=[]

    
def autoBuildNeighborsLists(grid, min_dist=30):
    for node in grid.nodes:
        for potential in grid.nodes:
            if (potential != node and returnDistanceBetweenPoints(node.x,potential.x,node.y,potential.y) <= min_dist):
                node.neighbors.append(potential)
                node.moveCosts.append(1)

def wipeNodes(grid):
    for node in grind.nodes:
        self.fScore= 0
        self.gScore= 0
        self.moveScore= 0
        self.parent= None
        self.child= None
        
def pathfind(grid, startNode, endNode, nodeSize):
    openList = []
    openListPriorities = []
    closedList = []
    curNode = startNode
    closedList.append(curNode)
    while curNode != endNode:
        for neighbor in curNode.neighbors:
            if not neighbor.blocked:
                if not neighbor in openList:
                    neighbor.hScore= curNode.hScore + curNode.moveCosts[curNode.neighbors.index(neighbor)]
                    neighbor.gscore = returnDistanceBetweenPoints(neighbor.x,endNode.x,neighbor.y,endNode.y)/nodeSize
                    neighbor.mscore = neighbor.hscore + neighbor.gscore
                    openList.append(neighbor)
                    openListPriorities.append(neighbor.mscore)
                elif curNode.hScore + curNode.moveCosts[curNode.neighbors.index(neighbor)] < neighbor.hscore:
                    del openListPriorities[openList.index(neighbor)]
                    openList.remove(neighbor)
                    neighbor.hscore = curNode.hScore + curNode.moveCosts[curNode.neighbors.index(neighbor)]
                    neighbor.mscore = neighbor.hscore + neighbor.gscore
        if len(openList)==0:
            del openList
            del closedList
            return None
        else:
            minVal = 9999999999999
            minIndex = -1
            for index in range(0,len(openListPriorities)-1):
                if openListPriorities[index] < minVal:
                    minIndex = Index
                    minVal = openListPriorities[index]
            del openListPriorities[minIndex]
            newNode = openList[minIndex]
            openList.remove(newNode)
            newNode.parent = curNode
            curNode = newNode
            closedList.append(curNode)
    while curNode != startNode:
        curNode.parent.child=cur_node
        curNode=curNode.parent
    del openList
    del closedList
    wipeNodes(grid)
    return curNode.child
                    
