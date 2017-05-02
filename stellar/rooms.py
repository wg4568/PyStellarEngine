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
