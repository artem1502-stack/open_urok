from config import *


class Score(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.left = 0
		self.right = 0
		self.font = pg.font.SysFont("arial", 100)
		self.text = f"{self.left} : {self.right}"
		self.image = self.font.render(self.text, True, TEXT_COLOR)
		self.rect = self.image.get_rect()
		self.rect.center = TEXT_POS

	def score_right(self):
		self.right += 1
		self.update_text()

	def score_left(self):
		self.left += 1
		self.update_text()

	def restart(self):
		self.left = 0
		self.right = 0
		self.update_text()

	def update_text(self):
		self.text = f"{self.left} : {self.right}"
		self.image = self.font.render(self.text, True, TEXT_COLOR)
		self.rect = self.image.get_rect()
		self.rect.center = TEXT_POS
