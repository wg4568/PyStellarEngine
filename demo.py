import stellar

# Button class, takes two sprites as arguments: default and hover
# Will call self.clicked when clicked on, regardless if set
class Button(stellar.objects.Object):
	def __init__(self, default, hover, down):
		stellar.objects.Object.__init__(self)
		self.add_sprite("default", default)
		self.add_sprite("hover", hover)
		self.add_sprite("down", down)
		self.set_sprite("default")
		self.clicked = None

	def logic(self):
		pass	

	def control(self, buttons, mousepos):
		if self.mouse_over():
			if buttons[stellar.keys.S_HELD][stellar.keys.M_1]:
				self.set_sprite("down")
			else:
				self.set_sprite("hover")
			if buttons[stellar.keys.S_RELEASED][stellar.keys.M_1]:
					self.clicked()
		else:
			self.set_sprite("default")


# Player class, basically a blue ball that moves around with the arrow keys
class Player(stellar.objects.Object):
	def __init__(self):
		stellar.objects.Object.__init__(self)

		self.add_sprite("default", stellar.sprites.Ellipse((0, 0, 255), 30, 30))
		self.set_sprite("default")
		self.movespeed = 3

	def control(self, buttons, mousepos):	   # Movement code, listens to keystrokes
		if buttons[stellar.keys.S_HELD][stellar.keys.K_UP]:
			self.move_by(0, -self.movespeed)
		if buttons[stellar.keys.S_HELD][stellar.keys.K_DOWN]:
			self.move_by(0, self.movespeed)
		if buttons[stellar.keys.S_HELD][stellar.keys.K_LEFT]:
			self.move_by(-self.movespeed, 0)
		if buttons[stellar.keys.S_HELD][stellar.keys.K_RIGHT]:
			self.move_by(self.movespeed, 0)


# Menu room, has some text, and a Button which calls self.begin_game
class Menu(stellar.rooms.Room):
	def __init__(self):
		stellar.rooms.Room.__init__(self)

		# 'Fixtures' are basically objects but don't move/have hitboxes
		# I added them to speed up the game when you have lots of objects that just sit around looking pretty
		#   and not actually doing anything
		fix_title = stellar.sprites.Text("Cool Game", stellar.tools.Font("arial.ttf", 40, (255, 255, 255)))
		fix_author = stellar.sprites.Text("A demo by Leap", stellar.tools.Font("arial.ttf", 20, (180, 180, 180), italic=True))

		# Define the two sprites for the button object in a minute
		# 'Compound' sprites are simply sprites made up of multiple other sprites, in this case,
		#   a box with a text sprite on top
		spr_start_default = stellar.sprites.Compound(
			stellar.sprites.Box((120, 0, 0), 180, 50),
			stellar.sprites.Text("Start", stellar.tools.Font("arial.ttf", 30, (255, 255, 255)), xoffset=5, yoffset=5)
		)
		spr_start_hover = stellar.sprites.Compound(
			stellar.sprites.Box((180, 0, 0), 180, 50),
			stellar.sprites.Text("Start", stellar.tools.Font("arial.ttf", 30, (255, 255, 255)), xoffset=5, yoffset=5)
		)
		spr_start_down = stellar.sprites.Compound(
			stellar.sprites.Box((250, 0, 0), 180, 50),
			stellar.sprites.Text("Start", stellar.tools.Font("arial.ttf", 30, (255, 255, 255)), xoffset=5, yoffset=5)
		)

		# Create button object, add the previous sprites
		obj_start = Button(spr_start_default, spr_start_hover, spr_start_down)
		obj_start.move_to(20, 100)
		obj_start.clicked = self.begin_game
		self.add_object(obj_start)
		
		# Add fixtures and objects to the room
		self.add_fixture(fix_title, (20, 20))
		self.add_fixture(fix_author, (20, 60))



	def begin_game(self):					   # Called by the obj_start Button when it's clicked
		self.game.set_room("main")			  # Switch to 'main' room, essentially starting the game


# The room in which the 'gameplay' takes place, has some help text
# Will return to menu if the escape key is pressed
class Main(stellar.rooms.Room):
	def __init__(self):
		stellar.rooms.Room.__init__(self)

		fnt_help = stellar.tools.Font("arial.ttf", 12, (180, 180, 180), italic=True, bold=True)

		# Another fixture, more compound sprites
		fix_help = stellar.sprites.Compound(
			stellar.sprites.Text("Press escape to return to menu", fnt_help),
			stellar.sprites.Text("Arrow keys to move", fnt_help, yoffset=16)
		)

		# Create player instance, from class defined above
		obj_player = Player()
		obj_player.move_to(250, 250)

		# Add the things
		self.add_fixture(fix_help, (10, 10))

		self.add_object(obj_player)

	def control(self, buttons, mousepos):	   # Will return to menu if escape is pressed
		if buttons[stellar.keys.S_PUSHED][stellar.keys.K_ESCAPE]:
			self.game.set_room("menu")


# Create new game, set title
game = stellar.base.Base()
game.title = "Stellar Testing"

# Add rooms, set to menu room
game.add_room("menu", Menu())
game.add_room("main", Main())
game.set_room("menu")

# Launch the game (no duh)
game.start()
