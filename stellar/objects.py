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

	def move_to(self, x, y):
		self.x, self.y = x, y

	def move_by(self, x, y):
		self.x += x
		self.y += y

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