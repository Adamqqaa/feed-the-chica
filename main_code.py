import random

import pygame
from pygame.display import set_caption


def game_run():
	pygame.init()
	pygame.mixer.init()

	set_caption('Feed The Chica')
	window_w = 520
	window_h = 760
	size = [window_w, window_h]
	window = pygame.display.set_mode(size)
	pygame.display.set_icon(pygame.image.load('icon.png'))

	# ЧИКА
	animCount = 0
	chica_x = size[0] // 2 - 30
	chica_y = 510
	chica_w = 41
	chica_h = 78
	chica_rect = pygame.Rect(chica_x, chica_y, chica_w, chica_h)
	chica_speed = 3
	chica_icon = pygame.image.load('Спрайты/health_bar_chica.png')
	chica_icon = pygame.transform.scale(chica_icon, [50, 60])

	chica_idle = pygame.image.load(r"Спрайты\Персонажи\Чика\Chica_idle.png")

	chica_left = [pygame.image.load('Спрайты/Персонажи/Чика/Left_1.png'),
	              pygame.image.load('Спрайты/Персонажи/Чика/Left_2.png')]

	chica_right = [pygame.image.load('Спрайты/Персонажи/Чика/Right_1.png'),
	               pygame.image.load('Спрайты/Персонажи/Чика/Right_2.png')]

	# Грегори
	GregoryAnimCount = 0
	gregory_left = [pygame.image.load('Спрайты/Персонажи/Грегори/Gregory_Left1.png'),
	                pygame.image.load('Спрайты/Персонажи/Грегори/Gregory_Left2.png')]

	gregory_right = [pygame.image.load('Спрайты/Персонажи/Грегори/Gregory_Right1.png'),
	                 pygame.image.load('Спрайты/Персонажи/Грегори/Gregory_Right2.png')]

	gregory_x = 270
	gregory_y = 130
	gregory_w = 40
	gregory_h = 70
	gregory_rect = pygame.Rect(gregory_x, gregory_y, gregory_w, gregory_h)
	gregory_speed = 4
	direction = random.choice(['left', 'right'])

	# Флешка
	mask = pygame.Surface((window_w, window_h))
	mask.fill((255, 255, 255))
	alpha_lvl = 450
	mask.set_alpha(alpha_lvl)

	# Кэсседи
	cass1 = pygame.image.load('Спрайты/Персонажи/Кэссиди/cassidy_1.png')
	cass2 = pygame.image.load('Спрайты/Персонажи/Кэссиди/cassidy_2.png')
	cass_x = 520
	cass_y = 300
	cass_w = 40
	cass_h = 70
	cass_rect = pygame.Rect(cass_x, cass_y, cass_w, cass_h)
	cass_jump = False
	cass_jump_time = None

	# ЧАСЫ И ТАЙМЕРЫ
	clock = pygame.time.Clock()
	start_time_spawn = pygame.time.get_ticks()
	start_time_direction = pygame.time.get_ticks()

	# Таймер
	start_time = pygame.time.get_ticks()

	# Пицца и мусор
	pizza_png = pygame.image.load('Спрайты/pizza.png')
	pizza_png = pygame.transform.scale(pizza_png, [35, 35])

	trash_png = pygame.image.load('Спрайты/trash.png')
	trash_png = pygame.transform.scale(trash_png, [50, 50])

	trash_speed = 5
	trash_speed_font = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 25)

	trash = []
	pizza = []

	clocks = pygame.image.load('Спрайты/clocks.png')
	clocks = pygame.transform.scale(clocks, [63, 63])

	#  Надписи
	time_texts = ['12 PM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM']
	current_text_index = 0

	black_blur = pygame.image.load('Спрайты/black_blur2.png')
	pygame.transform.scale(black_blur, [520, 760])

	# Голод
	hungry = 15
	hungry_font = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 25)

	# Музыка
	game_music = pygame.mixer.Sound('Музыка/IGotNoTime.mp3')
	game_music.set_volume(0.5)
	game_music.play()

	eat_sound = pygame.mixer.Sound('Музыка/eat_sound.mp3')
	eat_sound.set_volume(0.5)

	trash_hit = pygame.mixer.Sound('Музыка/trash_hit.mp3')
	trash_hit.set_volume(0.5)

	cass_scare = pygame.mixer.Sound('Музыка/windowscare.mp3')
	cass_scare.set_volume(0.5)

	# Фон
	balcony = pygame.image.load("Спрайты/balcony.png")
	balcony = pygame.transform.scale(balcony, [520, 150])

	more_trash = pygame.image.load("Спрайты/more_trash.png")
	more_trash = pygame.transform.scale(more_trash, [520, 150])

	floor = pygame.image.load("Спрайты/floor.png")
	floor = pygame.transform.scale(floor, [520, 150])

	trash_on_floor = pygame.image.load("Спрайты/trash_on_floor.png")
	trash_on_floor = pygame.transform.scale(trash_on_floor, [520, 150])

	game_bg = pygame.image.load('Спрайты/game_bg.png')
	game_bg = pygame.transform.scale(game_bg, [size[0], size[1]])

	def chica_move():
		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			if chica_rect[0] <= size[0] - chica_w:
				chica_rect.move_ip(chica_speed, 0)
		if keys[pygame.K_a] or keys[pygame.K_LEFT]:
			if chica_rect[0] >= 0:
				chica_rect.move_ip(-chica_speed, 0)

	def draw_some_rects(color, char_rect):
		pygame.draw.rect(window, color, char_rect, 2)

	def pg_event_get():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				cass_scare.stop()
				game_music.stop()
				import menu
				menu.menu_run()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					cass_scare.stop()
					game_music.stop()
					import menu
					menu.menu_run()

	end_game = False
	run = True
	while run:
		pg_event_get()
		keys = pygame.key.get_pressed()
		current_time = pygame.time.get_ticks()

		# Случайное перемещение Грегори
		if current_time - start_time_direction >= 800 <= 2000:
			# Сбрасываем время
			start_time_direction = current_time
			# Генерируем случайное направление движения
			direction = random.choice(['left', 'right'])

		if direction == 'left':
			gregory_rect.move_ip(-gregory_speed, 0)
		else:
			gregory_rect.move_ip(gregory_speed, 0)

		# Проверяем, не вышел ли Грегори за границы экрана
		if gregory_rect.left <= 0:
			gregory_rect.left = 0
			direction = random.choice(['left', 'right'])

		elif gregory_rect.right >= window_w:
			gregory_rect.right = window_w
			direction = random.choice(['left', 'right'])

		chica_move()

		# Случайный спавн объектов
		if 900 <= current_time - start_time_spawn <= 2000:
			# Сброс времени
			start_time_spawn = pygame.time.get_ticks()
			# Случайно выбираем, будет ли падать пицца или мусор
			falling_object = random.choices(['pizza', 'trash'], weights=[25, 75], k=1)[0]

			if falling_object == 'pizza':
				# Добавляем новую падающую пиццу
				pizza.append(pygame.Rect(gregory_rect.x, 140, 35, 35))
			else:
				# Добавляем новый падающий мусор
				trash.append(pygame.Rect(gregory_rect.x, 140, 50, 45))

		# Перемещение и столкновение падающих объектов
		for obj in trash:
			obj.move_ip(0, trash_speed)
			if obj.colliderect(chica_rect):
				trash_hit.play()
				hungry -= 10
				trash.remove(obj)
			elif obj.bottom > window.get_height():
				trash.remove(obj)
		for obj in pizza:
			obj.move_ip(0, 4)
			if obj.colliderect(chica_rect):
				eat_sound.play()
				pizza.remove(obj)
				if hungry < 100:
					hungry += 5
					if random.randint(1, 6) == 1:  # Шанс появления кэсс
						if not cass_jump:
							cass_jump = True
							cass_jump_time = pygame.time.get_ticks()
			elif obj.bottom > window.get_height():
				pizza.remove(obj)

		if hungry >= 80 < 90:  # Усложнение игры после увеличения насыщения
			trash_speed = 7
			if hungry >= 90:
				trash_speed = 8
				if hungry >= 100:
					hungry = 100
					trash_speed = 8.5
		else:
			trash_speed = 6

		for obj in trash:  # Отрисовка хитбокса мусора
			pygame.draw.rect(window, [0, 0, 0], obj, 1)
		for obj in pizza:  # Отрисовка хитбокса пиццы
			pygame.draw.rect(window, [0, 0, 0], obj, 1)

		# Обновление надписей
		time_elapsed = (pygame.time.get_ticks() - start_time) / 100  # Обновление таймера
		if time_elapsed >= 276:  # Если прошло 27.6 секунд
			current_text_index += 1  # Прибавить час
			start_time = pygame.time.get_ticks()
			if current_text_index >= len(time_texts) - 1:  # ЕСЛИ НАСТУПАЕТ 6 УТРА
				end_game = True
		if end_game and hungry >= 80:  # Если игра закончилась и насыщенность больше 80
			cass_scare.stop()
			game_music.stop()
			import win_window
			win_window.win_window()
			run = False
		if end_game and hungry < 80:  # Если игра закончилась и насыщенность меньше 80
			cass_scare.stop()
			game_music.stop()
			run = False
			import lose_window
			lose_window.lose_window()
		if hungry <= 0:  # Если голод меньше 0%
			cass_scare.stop()
			game_music.stop()
			run = False
			import lose_window
			lose_window.lose_window()

		draw_some_rects('gold', chica_rect)  # Отрисовка хитбокса Чики
		draw_some_rects('blue', gregory_rect)  # Отрисовка хитбокса Грегори
		draw_some_rects('pink', cass_rect)  # Отрисовка хитбокса Кэсседи

		# Заливка фона
		window.blit(game_bg, [0, 0])

		window.blit(more_trash, [0, 78])

		if GregoryAnimCount + 1 >= 30:
			GregoryAnimCount = 0

		if direction == 'left':
			window.blit(gregory_left[GregoryAnimCount // 15], [gregory_rect.x, gregory_rect.y])
			GregoryAnimCount += 2
		else:
			window.blit(gregory_right[GregoryAnimCount // 15], [gregory_rect.x, gregory_rect.y])
			GregoryAnimCount += 2

		# Балкон с Грегори
		window.blit(balcony, [0, 78])

		window.blit(trash_on_floor, [0, 460])

		if animCount + 1 >= 30:
			animCount = 0

		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			window.blit(chica_right[animCount // 15], [chica_rect.x - 10, chica_rect.y - 30])
			animCount += 2
		elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
			window.blit(chica_left[animCount // 15], [chica_rect.x - 10, chica_rect.y - 30])
			animCount += 2
		else:
			window.blit(chica_idle, [chica_rect.x - 10, chica_rect.y - 30])

		# Пол
		window.blit(floor, [0, 460])

		# Отрисовка текстур падающих объектов
		for obj in trash:
			window.blit(trash_png, [obj.x, obj.y])
		for obj in pizza:
			window.blit(pizza_png, [obj.x, obj.y])

		# Флешка
		if cass_jump:  # Движение кэсседи
			if pygame.time.get_ticks() - cass_jump_time < 1200:
				window.blit(cass1, [cass_rect.x, cass_rect.y])
				cass_rect.move_ip(-1, 0)
				cass_scare.play()
			else:
				alpha_lvl -= 5
				mask.set_alpha(alpha_lvl)
				window.blit(cass2, [cass_rect.x, cass_rect.y])
				window.blit(mask, [0, 0])
				cass_rect.move_ip(1, 0)
				if cass_rect.x >= size[0]:
					cass_jump = False
					alpha_lvl = 450

		# Отрисовка надписей
		time_text = hungry_font.render(time_texts[current_text_index], False, 'yellow')
		window.blit(time_text, [75, 640])

		trash_speed_text = trash_speed_font.render(f'Скорость мусора: {trash_speed}', False, 'yellow')
		window.blit(trash_speed_text, [10, 10])

		hungry_text = hungry_font.render(f'Насыщение: {hungry} %', False, 'yellow')
		window.blit(hungry_text, [70, 720])

		window.blit(clocks, [5, 620])
		window.blit(chica_icon, [10, 690])

		clock.tick(60)
		pygame.display.flip()
