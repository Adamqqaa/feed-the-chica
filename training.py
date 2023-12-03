import pygame
from pygame.display import set_caption


def training_run(fontItemSelect=None):
	pygame.init()
	size = [520, 760]
	window = pygame.display.set_mode(size)
	pygame.display.set_icon(pygame.image.load('icon.png'))
	set_caption('Feed The Chica: Training')

	fontItem = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 45)
	fontItemSelect = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 15)

	training_text1 = pygame.image.load('Спрайты/Обучение1.png')

	choose = pygame.mixer.Sound('Музыка/choosing.mp3')
	choose.set_volume(0.6)

	put_down = pygame.mixer.Sound('Музыка/put_down.mp3')
	put_down.set_volume(0.4)

	run = True
	while run:
		keys = pygame.key.get_focused()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				bg_music = pygame.mixer.music.play(-1)
				import menu
				menu.menu_run()
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					bg_music = pygame.mixer.music.play(-1)
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
