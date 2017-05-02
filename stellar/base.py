import pygame

class Room:
	def __init__(self, game):
		self.game = game
		self.background = (0, 0, 0)
		self.objects = []

	def draw(self):
		for obj in self.objects:
			obj._draw(self.game)

	def logic(self):
		for obj in self.objects:
			obj._logic(self.game)