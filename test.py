# #for python 2.7.13
# import pygame
# import stellarEngine as se

# engine = se.engine.Engine()
# engine.revEngines(1366,768,"test")

# while not engine.shouldClose():
#         engine.singleStep()

# engine.stopEngines()

from stellar import objects, sprites, rooms, base
from stellar.keys import *

game = base.Base()


class Player(objects.Object):
	def __init__(self):
		objects.Object.__init__(self)

		spr = sprites.Box((255, 0, 0), 10, 10)
		self.add_sprite("box", spr)
		self.set_sprite("box")

	def logic(self):
		print self.mouse_over()

	def control(self, buttons, mousepos):
		if buttons[K_UP]:
			self.y -= 1
		if buttons[K_DOWN]:
			self.y += 1
		if buttons[K_LEFT]:
			self.x -= 1
		if buttons[K_RIGHT]:
			self.x += 1

obj_player = Player()

rm_main = rooms.Room()
rm_main.add_object(obj_player)

game.add_room("rm_main", rm_main)
game.set_room("rm_main")

game.start()