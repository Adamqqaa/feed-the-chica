import pygame
from pygame.display import set_caption


def win_window():
	pygame.init()
	size = [520, 760]
	window = pygame.display.set_mode(size)
	pygame.display.set_icon(pygame.image.load('icon.png'))
	set_caption('You Win!')

	win_sound = pygame.mixer.Sound('Музыка/6_AM.mp3')
	win_sound.set_volume(0.7)

	put_down = pygame.mixer.Sound('Музыка/put_down.mp3')
	put_down.set_volume(0.4)

	choose = pygame.mixer.Sound('Музыка/choosing.mp3')
	choose.set_volume(0.6)

	fontItem = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 60)

	ChooseItem = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 45)
	ChooseItemSelect = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 50)

	fontItem.render('6 AM', False, 'yellow')

	pygame.font.Font('fonts/Minecraft Rus NEW.otf', 20)

	items = ['Начать заново', '', 'Меню', '', 'Выход']
	itemsSelect = ['Начать заново', '', 'Меню', '', 'Выход']

	select = 0
	selectAdd = 0

	girlands = pygame.image.load('Спрайты/Гирлянды.png')
	girlands = pygame.transform.scale(girlands, [size[0], size[1]])

	timer = 0
	win_sound.play()

	clock = pygame.time.Clock()

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				win_sound.stop()
				import menu
				menu.menu_run()
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					win_sound.stop()
					import menu
					menu.menu_run()
					run = False
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					selectAdd -= 1
					put_down.play()
				elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
					selectAdd += 1
					put_down.play()
				elif event.key in [pygame.K_RETURN, pygame.K_SPACE]:
					match items[select]:
						case 'Выход':
							win_sound.stop()
							choose.play()
							run = False
						case 'Начать заново':
							choose.play()
							win_sound.stop()
							import training
							training.training_run()
						case 'Меню':
							win_sound.stop()
							choose.play()
							import menu
							menu.menu_run()
							run = False

				select = (select + selectAdd) % len(items)
				while items[select] == '':
					select = (select + selectAdd) % len(items)
				selectAdd = 0
		timer += 1
		window.fill([0, 0, 0])

		if timer % 60 < 30:
			six_AM_text = fontItem.render('6 AM', False, [216, 166, 19])
		else:
			six_AM_text = fontItem.render('6 AM', False, 'black')

		window.blit(six_AM_text, [size[0] // 2 - 65, size[1] // 3])
		window.blit(girlands, [0, 0])

		for i in range(len(items)):
			if i == select:
				text = ChooseItemSelect.render(itemsSelect[i], 0, [216, 166, 19])
			else:
				text = ChooseItem.render(items[i], 0, [237, 220, 152])

			rect = text.get_rect(center=(size[0] // 2 + 10, 500 + 40 * i))
			window.blit(text, rect)

		clock.tick(60)
		pygame.display.flip()
