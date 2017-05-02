import stellar

game = stellar.base.Base()
game.title = "Hello, world!"

room = stellar.rooms.Room()
room.background = (180, 0, 0)
game.add_room("main", room)
game.set_room("main")

<<<<<<< HEAD
game.start()
=======

class Player(objects.Object):
	def __init__(self):
		objects.Object.__init__(self)

		spr = sprites.Box((255, 0, 0), 10, 10)
		self.add_sprite("box", spr)
		self.set_sprite("box")

	def logic(self):
		print self.mouse_over()

	def control(self, buttons, mousepos):
		if buttons[S_HELD,K_UP]:
			self.y -= 1
		if buttons[S_HELD,K_DOWN]:
			self.y += 1
		if buttons[S_HELD,K_LEFT]:
			self.x -= 1
		if buttons[S_HELD,K_RIGHT]:
			self.x += 1

obj_player = Player()

rm_main = rooms.Room()
rm_main.add_object(obj_player)

game.add_room("rm_main", rm_main)
game.set_room("rm_main")

game.start()
>>>>>>> origin/master
