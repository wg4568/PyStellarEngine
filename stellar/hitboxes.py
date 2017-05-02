class Hitbox:
	def __init__(self):
		pass

	def point_inside(self, obj, point):
		return False

class Box(Hitbox):
	def __init__(self, width, height):
		Hitbox.__init__(self)
		self.width = width
		self.height = height

	def point_inside(self, obj, pos):

		x = obj.x
		y = obj.y
		xm = x + (self.width*obj.scale)
		ym = y + (self.height*obj.scale)

		ix = pos[0]
		iy = pos[1]

		xgood = x <= ix < xm
		ygood = y <= iy < ym
		return xgood and ygood

class Ellipse(Hitbox):
	def __init__(self, width, height):
		Hitbox.__init__(self)
		self.width = width
		self.height = height

	def point_inside(self, obj, pos):

		h, k = obj.x, obj.y
		x, y = pos

		a = self.width/2.0
		b = self.height/2.0

		a *= obj.scale
		b *= obj.scale

		atop = (x-h-a)**2
		btop = (y-k-b)**2

		aside = atop/(a**2)
		bside = btop/(b**2)

		return aside + bside <= 1

class Compound(Hitbox):
	def __init__(self, *hitboxes):
		Hitbox.__init__(self)
		self.hitboxes = hitboxes

	def point_inside(self, obj, pos):
		inside = False
		for hitbox in self.hitboxes:
			if hitbox.point_inside(obj, pos):
				inside = True
		return inside