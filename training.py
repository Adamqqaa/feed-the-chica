import pygame
from pygame.display import set_caption


def training_run():
	pygame.init()
	size = [520, 760]
	window = pygame.display.set_mode(size)
	pygame.display.set_icon(pygame.image.load('icon.png'))
	set_caption('Feed The Chica: Training')

	training_text1 = pygame.image.load('Спрайты/Обучение1.png')

	choose = pygame.mixer.Sound('Музыка/choosing.mp3')
	choose.set_volume(0.6)

	put_down = pygame.mixer.Sound('Музыка/put_down.mp3')
	put_down.set_volume(0.4)

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.mixer.music.play(-1)
				import menu
				menu.menu_run()
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.mixer.music.play(-1)
					import menu
					menu.menu_run()
					run = False
				if event.key == pygame.K_s:
					choose.play()
					import main_code
					main_code.game_run()
		window.blit(training_text1, [0, 0])
		pygame.display.flip()
	pygame.quit()
	quit()
