import stellar

game = stellar.base.Base()
game.title = "Hello, world!"

room = stellar.rooms.Room()
room.background = (180, 0, 0)
game.add_room("main", room)
game.set_room("main")

game.start()