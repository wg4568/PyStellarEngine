class Object:
	def __init__(self, x=0, y=0, scale=1.0 persistent=False, runsInBackground=False, priority=0):
		self.x = x
		self.y = y
		self.start_x = x
		self.start_y = y
		self.scale = scale
		self.room = None
		self.persistent = False
		self.runsInBackground = False
		self.priority=priority
		self.type = "Object_Base"

		self.nodes = []
		self.sprites = []


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

	def _control(self, buttons, mouse):
                for node in nodes:
                        node._control(buttons, mouse)

                for sprite in sprites:
                        sprite._control(buttons, mouse)

		try: self.control(buttons, mouse)
		except AttributeError: pass

	def _early_control(self, buttons, mouse):
                for node in nodes:
                        node._early_control(buttons, mouse)

                for sprite in sprites:
                        sprite._early_control(buttons, mouse)
                        
		try: self.early_control(buttons, mouse)
		except AttributeError: pass

	def _late_control(self, buttons, mouse):
                for node in nodes:
                        node._late_control(buttons, mouse)

                for sprite in sprites:
                        sprite._late_control(buttons, mouse)
                        
		try: self.early_control(buttons, mouse)
		except AttributeError: pass

	def _gui_control(self, buttons, mouse):
                for node in nodes:
                        node._gui_control(buttons, mouse)

                for sprite in sprites:
                        sprite._gui_control(buttons, mouse)
                
                try: self.gui_control(buttons, mouse)
                except AttributeError: pass

        def _physics_control(self, buttons, mouse):
                for node in nodes:
                        node._physics_control(buttons, mouse)

                for sprite in sprites:
                        sprite._physics_control(buttons, mouse)
                                
                try: self.physics_control(buttons, mouse)
                except AttributeError: pass

class GUI(Object):
        def __init__(self, x=0, y=0, scale=1.0, persistent=False, runsInBackground=False):
                Object.__init__(self, x, y, scale, persistent, runsInBackground)
                self.type = "Object_GUI"

        def _control(self, buttons, mouse):
                for node in nodes:
                        node._control(buttons, mouse)

                for sprite in sprites:
                        sprite._control(buttons, mouse)


	def _early_control(self, buttons, mouse):
                for node in nodes:
                        node._early_control(buttons, mouse)

                for sprite in sprites:
                        sprite._early_control(buttons, mouse)

	def _late_control(self, buttons, mouse):
                for node in nodes:
                        node._late_control(buttons, mouse)

                for sprite in sprites:
                        sprite._late_control(buttons, mouse)

	def _gui_control(self, buttons, mouse):
                for node in nodes:
                        node._gui_control(buttons, mouse)

                for sprite in sprites:
                        sprite._gui_control(buttons, mouse)
                        
                try: self.physics_control(buttons, mouse)
                except AttributeError: pass

        def _physics_control(self, buttons, mouse):
                pass

class Rigidbody(Object):
        def __init__(self, x=0, y=0, scale=1.0, persistent=False, runsInBackground=False):
                Object.__init__(self, x, y, scale, persistent, runsInBackground)
                self.type = "Object_Rigidbody"

        def _control(self, buttons, mouse):
                for node in nodes:
                        node._control(buttons, mouse)

                for sprite in sprites:
                        sprite._control(buttons, mouse)


	def _early_control(self, buttons, mouse):
                for node in nodes:
                        node._early_control(buttons, mouse)

                for sprite in sprites:
                        sprite._early_control(buttons, mouse)

	def _late_control(self, buttons, mouse):
                for node in nodes:
                        node._late_control(buttons, mouse)

                for sprite in sprites:
                        sprite._late_control(buttons, mouse)

	def _gui_control(self, buttons, mouse):
                 for node in nodes:
                        node._gui_control(buttons, mouse)

                for sprite in sprites:
                        sprite._gui_control(buttons, mouse)
        
        def _physics_control(self, buttons, mouse):
                for node in nodes:
                        node._physics_control(buttons, mouse)

                for sprite in sprites:
                        sprite._physics_control(buttons, mouse)
                
                try: self.physics_control(buttons, mouse)
                except AttributeError: pass

class Static(Object):
        def __init__(self, x=0, y=0, scale=1.0, persistent=False, runsInBackground=False):
                Object.__init__(self, x, y, scale, persistent, runsInBackground)
                self.type = "Object_Rigidbody"
                
	def _control(self, buttons, mouse):
                for node in nodes:
                        node._control(buttons, mouse)

                for sprite in sprites:
                        sprite._control(buttons, mouse)
                        
		try: self.control(buttons, mouse)
		except AttributeError: pass

	def _early_control(self, buttons, mouse):
                for node in nodes:
                        node._early_control(buttons, mouse)

                for sprite in sprites:
                        sprite._early_control(buttons, mouse)
                        
		try: self.early_control(buttons, mouse)
		except AttributeError: pass

	def _late_control(self, buttons, mouse):
                for node in nodes:
                        node._late_control(buttons, mouse)

                for sprite in sprites:
                        sprite._late_control(buttons, mouse)

		try: self.early_control(buttons, mouse)
		except AttributeError: pass

	def _gui_control(self, buttons, mouse):
                for node in nodes:
                        node._gui_control(buttons, mouse)

                for sprite in sprites:
                        sprite._gui_control(buttons, mouse)
        
        def _physics_control(self, buttons, mouse):
                pass

class Empty(Object):
        def __init__(self, x=0, y=0, scale=1.0):
                Object.__init__(self, x, y, scale, False, False)
                self.type = "Object_Empty"

	def _control(self, buttons, mouse):
                for node in nodes:
                        node._control(buttons, mouse)

                for sprite in sprites:
                        sprite._control(buttons, mouse)


	def _early_control(self, buttons, mouse):
                for node in nodes:
                        node._early_control(buttons, mouse)

                for sprite in sprites:
                        sprite._early_control(buttons, mouse)

	def _late_control(self, buttons, mouse):
                for node in nodes:
                        node._late_control(buttons, mouse)

                for sprite in sprites:
                        sprite._late_control(buttons, mouse)

	def _gui_control(self, buttons, mouse):
                for node in nodes:
                        node._gui_control(buttons, mouse)

                for sprite in sprites:
                        sprite._gui_control(buttons, mouse)
        
        def _physics_control(self, buttons, mouse):
                pass

