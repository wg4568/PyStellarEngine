class Room:
	def __init__(self):
		self.game = None
		self.background = (0, 0, 0)
		self.all_objects = []
		self.objects = []
		self.fixtures = []
		self.active = False
		self.size = None

	def game_link(self, game):
		self.game = game
		self.size = self.game.size

	def add_object(self, obj):
		obj.room_link(self)
		self.all_objects.append(obj)

	def add_fixture(self, fixture, posn):
		self.fixtures.append([fixture, posn])

	def activate(self):
		self.active = True
		self.on_load()

	def deactivate(self):
		self.active = False
		self.on_unload()

	def _handle_event(self, event):
		self.handle_event(event)

	def _logic(self):
		self.objects = filter(lambda x: x.enabled, self.all_objects)
		# self.objects = sorted(self.objects, key=lambda x: x.layer)

		for obj in self.objects:
			obj._logic()

		self.logic()

	def _control(self, buttons, mouse):
		for obj in self.objects:
			obj._control(buttons, mouse)

		self.control(buttons, mouse)

	def _draw(self):
		self.game.screen.fill(self.background)

		for fixture, posn in self.fixtures:
			fixture.draw(self, posn)

		for obj in self.objects:
			obj._draw()

		self.draw()

	def mouse_pos(self):
		return self.game.mousepos

	def draw_rect(self, color, dims):
		self.game.pygame.draw.rect(self.game.screen, color, dims)


	def draw_lines(self, color, lines, width):
		self.game.pygame.draw.lines(self.game.screen, color, True, lines, width)
		
	def draw_ellipse(self, color, dims):
		self.game.pygame.draw.ellipse(self.game.screen, color, dims)

	def draw_blit(self, surf, posn):
		self.game.screen.blit(surf, posn)





	def logic(self):
		pass

	def control(self, buttons, mouse):
		pass

	def draw(self):
		pass

	def handle_event(self, event):
		pass

	def on_load(self):
		pass

	def on_unload(self):
		pass