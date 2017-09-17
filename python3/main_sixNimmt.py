from base.boardgame import BoardGame
from sixNimmt.game import SixNimmt
from sixNimmt.player import SixNimmtPlayer

p = SixNimmtPlayer()
b = BoardGame(SixNimmt(),[p])
b.play()
