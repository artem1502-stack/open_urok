from config import *
from ball import Ball
from score import Score


class BoardControl(pg.sprite.Sprite):
	def __init__(self, window, sp_group):
		pg.sprite.Sprite.__init__(self)
		self.ball = Ball(self)
		self.score = Score()
		self.window = window
		self.image = pg.image.load("data/board.jpeg").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.bottomleft = (0, WINDOW_HEIGHT)
		sp_group.add(self)
		sp_group.add(self.ball)
		sp_group.add(self.score)

	def left(self):
		self.ball.left()

	def right(self):
		self.ball.right()

	def restart(self):
		self.ball.restart()
		self.score.restart()
