import pygame

class Room:
	def __init__(self, game):
		self.game = game
		self.background = (0, 0, 0)
		self.objects = []
		self.active = False

	def activate(self):
		self.active = True

	def deactivate(self):
		self.active = False

	def logic(self):
		for obj in self.objects:
			obj._logic(self.game)

	def control(self, buttons, mouse):
		for obj in self.objects:
			obj._control(buttons, mouse)

	def draw(self):
		for obj in self.objects:
			obj._draw(self.game)

class Base:
	def __init__(self):
		pygame.init()
		self.pygame = pygame
		self.clock = pygame.time.Clock()
		self.running = False
		self.current_room = None
		self.rooms = {}
		self.frame = 0

		self.title = "Stellar Game"
		self.rate = 60
		self.size = (500, 500)

	def get_current_room(self):
		return self.rooms[self.current_room]

	def add_room(self, name, room):
		self.rooms[name] = room

	def set_room(self, name):
		self.get_current_room().deactivate()
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
				self.get_current_room().handle_event(event)
				if event.type == pygame.QUIT:
					self.stop()

			buttons = keys.control_check()
			mouse = pygame.mouse.get_pos()

			self.get_current_room().control(buttons, mouse)
			self.get_current_room().draw()
			self.get_current_room().logic()

			pygame.display.update()
			self.clock.tick(self.rate)
