import pygame
from pygame.display import set_caption


def developer_run():
	pygame.init()
	size = [520, 760]
	window = pygame.display.set_mode(size)
	pygame.display.set_icon(pygame.image.load('icon.png'))
	set_caption('Feed The Chica: Developer')

	black_blur = pygame.image.load('Спрайты/black_blur.png')
	black_blur = pygame.transform.scale(black_blur, [520, 760])

	menu_bg = pygame.image.load('Спрайты/pizza_bgpng.png')
	menu_bg = pygame.transform.scale(menu_bg, size)

	dev_text = pygame.image.load('Спрайты/Разработчк текст.png')

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False

		window.blit(menu_bg, [0, 0])
		window.blit(black_blur, [0, 0])
		window.blit(dev_text, [0, 10])
		pygame.display.flip()
