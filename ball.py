from config import *


class BallPlace(Enum):
	LeftGate = 0
	LeftDefence = 1
	Center = 2
	RightDefence = 3
	RightGate = 4


class Ball(pg.sprite.Sprite):
	ball_list = [BallPlace.LeftGate, BallPlace.LeftDefence, BallPlace.Center, BallPlace.RightDefence, BallPlace.RightGate]
	ball_pos = {
		BallPlace.LeftGate		: LEFT_GATE_COORDS,
		BallPlace.LeftDefence	: LEFT_DEFENCE_COORDS,
		BallPlace.Center		: CENTER_COORDS,
		BallPlace.RightDefence	: RIGHT_DEFENCE_COORDS,
		BallPlace.RightGate		: RIGHT_GATE_COORDS
	}

	def __init__(self, board_control):
		pg.sprite.Sprite.__init__(self)
		self.board_control = board_control
		self.image = pg.image.load("data/img_2.png").convert_alpha()
		self.image = pg.transform.scale(self.image, BALL_SIZE)
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.center = CENTER_COORDS
		self.place = BallPlace.Center

	def left(self):
		if self.place == BallPlace.LeftGate:
			self.board_control.score.score_left()
			self.place = BallPlace.Center
		else:
			self.place = self.ball_list[self.ball_list.index(self.place) - 1]
		self.rect.center = self.ball_pos[self.place]

	def right(self):
		if self.place == BallPlace.RightGate:
			self.board_control.score.score_right()
			self.place = BallPlace.Center
		else:
			self.place = self.ball_list[self.ball_list.index(self.place) + 1]
		self.rect.center = self.ball_pos[self.place]

	def restart(self):
		self.place = BallPlace.Center
		self.rect.center = self.ball_pos[self.place]
