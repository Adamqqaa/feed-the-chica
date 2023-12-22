import pygame
from pygame.display import set_caption


def settings_run():
	pygame.init()
	size = [520, 760]
	window = pygame.display.set_mode(size)
	pygame.display.set_icon(pygame.image.load('icon.png'))
	set_caption('Feed The Chica: Settings')

	fontItem = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 45)
	fontItemSelect = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 50)

	chica_settings = pygame.image.load('Спрайты/chica_settings.png')
	chica_settings = pygame.transform.scale(chica_settings, [460, 460])

	black_blur = pygame.image.load('Спрайты/black_blur.png')
	black_blur = pygame.transform.scale(black_blur, [520, 760])

	menu_bg = pygame.image.load('Спрайты/pizza_bgpng.png')
	menu_bg = pygame.transform.scale(menu_bg, size)

	gm = ['Легко', 'Нормально', 'Тяжело']
	game_mode_choose = 1
	items = ['Сложность:', '', f'{gm[game_mode_choose]}']
	itemsSelect = ['Сложность:', '', f'{gm[game_mode_choose]}']

	select = 0
	selectAdd = 0

	put_down = pygame.mixer.Sound('Музыка/put_down.mp3')
	put_down.set_volume(0.4)

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					selectAdd -= 1
					put_down.play()
				elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
					selectAdd += 1
					put_down.play()

				if items[select] == 'Сложность:':
					if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
						game_mode_choose += 1
					elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
						game_mode_choose -= 1

			select = (select + selectAdd) % len(items)
			while items[select] == '':
				select = (select + selectAdd) % len(items)

			selectAdd = 0
		window.blit(menu_bg, [0, 0])
		window.blit(black_blur, [0, 0])
		window.blit(chica_settings, [40, 330])
		for i in range(len(items)):
			if i == select:
				text = fontItemSelect.render(itemsSelect[i], 0, [216, 166, 19])
			else:
				text = fontItem.render(items[i], 0, [217, 166, 119])
			rect = text.get_rect(center=(size[0] // 2, 70 + 40 * i))
			window.blit(text, rect)
		pygame.display.flip()
