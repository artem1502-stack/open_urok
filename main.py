from config import *
from board_control import BoardControl

pg.init()

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
all_sprites = pg.sprite.Group()
bc = BoardControl(window, all_sprites)

clock = pg.time.Clock()


def main_loop():
	quit_game = False

	while not quit_game:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit_game = True
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT:
					bc.left()
				elif event.key == pg.K_RIGHT:
					bc.right()
				elif event.key == pg.K_r:
					bc.restart()

		window.fill(BLACK)
		all_sprites.draw(window)
		all_sprites.update()
		pg.display.update()
		clock.tick(FPS)

	pg.quit()


if __name__ == "__main__":
	main_loop()
