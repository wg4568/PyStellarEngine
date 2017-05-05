import stellar
import itertools

class Tile(stellar.objects.Object):
	def __init__(self, gridx, gridy):
		stellar.objects.Object.__init__(self)

		self.add_sprite("main", stellar.sprites.Compound(
			stellar.sprites.BoxOutline((255, 0, 0), 32, 32, linewidth=3)
		))
		self.set_sprite("main")

		self.gridx = gridx
		self.gridy = gridy

	def logic(self):
		self.x, self.y = self.room.screen_pos(self.gridx, self.gridy)

class TileRoom(stellar.rooms.Room):
	def __init__(self):
		stellar.rooms.Room.__init__(self)

		self.gridsize = (250, 250)
		self.tiles = {}

		self.tilesize = 32

		self.cam_x = 100
		self.cam_y = 100

		for x, y in itertools.product(xrange(self.gridsize[0]), xrange(self.gridsize[1])):
			newtile = Tile(x, y)
			# newtile.disable()
			self.tiles[x, y] = newtile
			self.add_object(newtile)

		for tile in self.objects:
			if self.in_camera(tile.gridx, tile.gridy):
				print tile
				tile.enable()

	def in_camera(self, x, y):
		t_wid = self.size[0]/float(self.tilesize)
		t_hid = self.size[1]/float(self.tilesize)
		
		x_range = xrange(self.cam_x, self.cam_x+t_wid)
		y_range = xrange(self.cam_y, self.cam_y+t_hid)

		return (x in x_range) and (y in y_range)

	def screen_pos(self, x, y):
		x_norm = x - self.cam_x
		y_norm = y - self.cam_y

		return x_norm * self.tilesize, y_norm * self.tilesize

	def logic(self):
		pass

game = stellar.base.Base()

tileroom = TileRoom()
game.add_room("tileroom", tileroom)
game.set_room("tileroom")

game.start()