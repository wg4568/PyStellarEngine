import stellar

class Button(stellar.objects.Object):
	def __init__(self, default, hover):
		stellar.objects.Object.__init__(self)
		self.add_sprite("default", default)
		self.add_sprite("hover", hover)
		self.set_sprite("default")
		self.clicked = None

	def logic(self):
		if self.mouse_over():
			self.set_sprite("hover")
		else:
			self.set_sprite("default")

	def control(self, buttons, mousepos):
		if self.mouse_over() and buttons[stellar.keys.M_1]:
			self.clicked()

class Player(stellar.objects.Object):
	def __init__(self):
		stellar.objects.Object.__init__(self)

		self.add_sprite("default", stellar.sprites.Ellipse((0, 0, 255), 30, 30))
		self.set_sprite("default")
		self.movespeed = 3

	def control(self, buttons, mousepos):
		if buttons[stellar.keys.K_UP]:
			self.move_by(0, -self.movespeed)
		if buttons[stellar.keys.K_DOWN]:
			self.move_by(0, self.movespeed)
		if buttons[stellar.keys.K_LEFT]:
			self.move_by(-self.movespeed, 0)
		if buttons[stellar.keys.K_RIGHT]:
			self.move_by(self.movespeed, 0)

class Menu(stellar.rooms.Room):
	def __init__(self):
		stellar.rooms.Room.__init__(self)

		fix_title = stellar.sprites.Text("Cool Game", stellar.tools.Font("arial.ttf", 40, (255, 255, 255)))
		fix_author = stellar.sprites.Text("A demo by Leap", stellar.tools.Font("arial.ttf", 20, (180, 180, 180), italic=True))

		spr_start_default = stellar.sprites.Compound(
			stellar.sprites.Box((180, 0, 0), 180, 50),
			stellar.sprites.Text("Start", stellar.tools.Font("arial.ttf", 30, (255, 255, 255)), xoffset=5, yoffset=5)
		)
		spr_start_hover = stellar.sprites.Compound(
			stellar.sprites.Box((120, 0, 0), 180, 50),
			stellar.sprites.Text("Start", stellar.tools.Font("arial.ttf", 30, (255, 255, 255)), xoffset=5, yoffset=5)
		)

		obj_start = Button(spr_start_default, spr_start_hover)
		obj_start.move_to(20, 100)
		obj_start.clicked = self.begin_game

		self.add_fixture(fix_title, (20, 20))
		self.add_fixture(fix_author, (20, 60))

		self.add_object(obj_start)

	def begin_game(self):
		self.game.set_room("main")

class Main(stellar.rooms.Room):
	def __init__(self):
		stellar.rooms.Room.__init__(self)

		fix_help = stellar.sprites.Text("Press escape to return to the menu", stellar.tools.Font("arial.ttf", 20, (180, 180, 180), italic=True))

		obj_player = Player()
		obj_player.move_to(250, 250)

		self.add_fixture(fix_help, (10, 10))

		self.add_object(obj_player)

	def control(self, buttons, mousepos):
		if buttons[stellar.keys.K_ESCAPE]:
			self.game.set_room("menu")

game = stellar.base.Base()
game.title = "Stellar Testing"

game.add_room("menu", Menu())
game.add_room("main", Main())
game.set_room("menu")

game.start()