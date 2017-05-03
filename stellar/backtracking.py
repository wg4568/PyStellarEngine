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

	def addNeighor(self,direction,neighbor):
		self.neighbors[direction]=neighbor

class Grid:
	def __init__(self):
		self.nodes = None
		
	def createCells(self, width=30, height=30):
		self.nodes = [[Node()] * width] * height]
		self.width = width
		self.height = height
		for n in range(0,width-1):
			for m in range(0,height-1):
				self.nodes[n][m].row = n
				self.nodes[n][m].column = m
		for n in range(0,width-1):
			for m in range(0,height-1):
				if n > 0:
					self.nodes[n][m].addNeighbor(1,self.nodes[n-1][m])
				if m > 0:
					self.nodes[n][m].addNeighbor(0,self.nodes[n][m-1])
				if n < width - 1:
					self.nodes[n][m].addNeighbor(3,self.nodes[n+1][m])
				if m < height - 1:
					self.nodes[n][m].addNeighbor(2,self.nodes[n][m+1])

def randomHoles(grid,holeCount=30,seed=-1):
	if seed == -1:
		random.seed()
	else:
		random.seed(seed)
	for hole in range(holeCount - 1):
		curTile = grid.nodes[random.range(0,grid.width-1)][random.range(0,grid.height-1)]
		hole = rand.range(4-1)

		while len(curTile.neighbors) < hole:
			hole = rand.range(4-1)

		curTile.makeHole(hole)
		
def buildMaze(grid,seed=-1):
	if seed == -1:
		random.seed()
	else:
		random.seed(seed)
	side = random.range(1)
	cap = random.range(1)
	if cap == 1:
		startM = 0
	else:
		startM = grid.height - 1
	if side == 1:
		startN = 0
	else:
		startN = grid.width - 1
	curTile = grid.nodes[n][m]
	stack = []
	pathed = []
	stack.append(curTile)
	pathed.append(curTile)
	while len(stack) != 0:
		hasUnpathedNeighbor = False
		for neighbor in curTile.neighbors:
			if not neighbor in pathed:
				hasUnpathedNeighbor = True
		if hasUnpathedNeighbor:
			nextTile = random.range(len(curTile.neighbors)-1)
			while nextTile in pathed:
				nextTile = random.range(len(curTile.neighbors)-1)
			index = curTile.neighbors.index(nextTile)
			if index == 0:
				nextTile.addHole(2)
				curTile.addHole(0)
			elif index == 2:
				curTile.addHole(2)
				nextTile.addHole(0)
			elif index == 1:
				curTile.addHole(1)
				nextTile.addHole(3)
			elif index == 3:
				curTile.addHole(3)
				nextTile.addHole(3)
		else:
			curTile = pathed.pop(len(pathed)-1)