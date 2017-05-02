import pygame, keys, tools

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
