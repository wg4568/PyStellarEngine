import keys

class Object:
	def __init__(self, x=0, y=0, scale=1.0):
		self.x = x
		self.y = y
		self.scale = scale
		self.room = None

		self.layer = 0

		self.enabled = True

		self.current_sprite = None
		self.sprites = {}

	def disable(self):
		self.enabled = False

	def enable(self):
		self.enable = True

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
		self.logic()

	def _control(self, buttons, mouse):
		if self.mouse_over() and buttons[keys.S_PUSHED][keys.M_1]:
			self.on_click()
		self.control(buttons, mouse)

	def _draw(self):
		self.get_current_sprite().draw(self.room, self.get_position(), self.scale)

		self.draw()


	def logic(self):
		pass

	def control(self, buttons, mouse):
		pass

	def draw(self):
		pass

	def on_click(self):
		pass

class Button(Object):
	def __init__(self, default, hover, down, hover_sound=None, click_sound=None):
		Object.__init__(self)
		self.add_sprite("default", default)
		self.add_sprite("hover", hover)
		self.add_sprite("down", down)
		self.set_sprite("default")

		self.click_sound = click_sound
		self.hover_sound = hover_sound

		self.clicked = None
		self.click_inp = keys.M_1

		self.new_mouseover = False

	def when_clicked(self, func):
		self.clicked = func

	def control(self, buttons, mousepos):
		if self.mouse_over():
			if not self.new_mouseover:
				if self.hover_sound:
					self.hover_sound.play()
				self.new_mouseover = True
			if buttons[keys.S_HELD][self.click_inp]:
				self.set_sprite("down")
			else:
				self.set_sprite("hover")
			if buttons[keys.S_RELEASED][self.click_inp]:
				if self.click_sound:
					self.click_sound.play()
				self.clicked()
		else:
			self.new_mouseover = False
			self.set_sprite("default")