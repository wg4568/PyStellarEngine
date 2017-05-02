import pygame, keys, tools

class Object:
	def __init__(self, x=0, y=0, scale=1.0):
		self.x = x
		self.y = y
		self.scale = scale
		self.room = None

		self.current_sprite = None
		self.sprites = {}

	def room_link(self, room):
		self.room = room

	def add_sprite(self, name, sprite):
		self.sprites[name] = sprite

	def set_sprite(self, name):
		self.current_sprite = name

	def get_current_sprite(self):
		return self.sprites[self.current_sprite]

	def mouse_over(self):
		psn = self.room.mouse_pos()
		return self.get_current_sprite().hitbox.point_inside(self, psn)

	def get_position(self):
		return (self.x, self.y)

	def _logic(self):
		try: self.logic()
		except AttributeError: pass

	def _control(self, buttons, mouse):
		try: self.control(buttons, mouse)
		except AttributeError: pass

	def _draw(self):
		self.get_current_sprite().draw(self.room, self.get_position(), self.scale)

		try: self.draw()
		except AttributeError: pass

class Room:
	def __init__(self):
		self.game = None
		self.background = (0, 0, 0)
		self.objects = []
		self.active = False

	def game_link(self, game):
		self.game = game

	def add_object(self, obj):
		obj.room_link(self)
		self.objects.append(obj)

	def activate(self):
		self.active = True

	def deactivate(self):
		self.active = False

	def _handle_event(self, event):
		try: self.handle_event(event)
		except AttributeError: pass

	def _logic(self):
		for obj in self.objects:
			obj._logic()

		try: self.logic()
		except AttributeError: pass

	def _control(self, buttons, mouse):
		for obj in self.objects:
			obj._control(buttons, mouse)

		try: self.control(buttons, mouse)
		except AttributeError: pass

	def _draw(self):
		self.game.screen.fill(self.background)

		for obj in self.objects:
			obj._draw()

		try: self.draw()
		except AttributeError: pass

	def mouse_pos(self):
		return self.game.mousepos

	def draw_rect(self, color, dims):
		self.game.pygame.draw.rect(self.game.screen, color, dims)

	# room.draw_rect(self.color, list(posn) + [self.width*scale, self.height*scale])
	# room.draw_ellipse(self.color, list(posn) + [self.width*scale, self.height*scale])
	# room.draw_image(img, posn)

class Base:
	def __init__(self):
		pygame.init()
		self.pygame = pygame
		self.clock = pygame.time.Clock()
		self.running = False
		self.current_room = None
		self.rooms = {}
		self.frame = 0

		self.buttons = []
		self.mousepos = None

		self.title = "Stellar Game"
		self.target_framerate = 60
		self.size = (500, 500)

	def get_current_room(self):
		return self.rooms[self.current_room]

	def add_room(self, name, room):
		room.game_link(self)
		self.rooms[name] = room

	def set_room(self, name):
		if self.current_room: self.get_current_room().deactivate()
		self.current_room = name
		self.get_current_room().activate()

	def stop(self):
		self.running = False

	def start(self):
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption(self.title)

		self.running = True

		while self.running:
			for event in pygame.event.get():
				self.get_current_room()._handle_event(event)
				if event.type == pygame.QUIT:
					self.stop()

			self.buttons = keys.control_check()
			self.mousepos = pygame.mouse.get_pos()

			self.get_current_room()._control(self.buttons, self.mousepos)
			self.get_current_room()._draw()
			self.get_current_room()._logic()

			pygame.display.update()
			self.clock.tick(self.target_framerate)
