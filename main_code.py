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
    window = pygame.display.set_mode(size, pygame.DOUBLEBUF)
    pygame.mouse.set_visible(False)
    pygame.display.set_icon(pygame.image.load('icon.png'))

    # ЧИКА
    chica_x = size[0] // 2 - 30
    chica_y = 510
    chica_w = 45
    chica_h = 80
    chica_rect = pygame.Rect(chica_x, chica_y, chica_w, chica_h)
    chica_speed = 2.5
    chica_icon = pygame.image.load('Спрайты/health_bar_chica.png')
    chica_icon = pygame.transform.scale(chica_icon, [50, 60])

    # Грегори
    gregory_x = 270
    gregory_y = 130
    gregory_w = 40
    gregory_h = 70
    gregory_rect = pygame.Rect(gregory_x, gregory_y, gregory_w, gregory_h)
    gregory_speed = 4
    direction = random.choice(['left', 'right'])

    # Кэсседи
    cass_x = 520
    cass_y = 300
    cass_w = 40
    cass_h = 70
    cass_rect = pygame.Rect(cass_x, cass_y, cass_w, cass_h)
    cass_jump = False
    cass_jump_time = None

    # Флешка
    mask = pygame.Surface((window_w, window_h))
    mask.fill((255, 255, 255))
    mask.set_alpha(180)
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
    hungry = 10
    hungry_font = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 25)

    # Музыка
    game_music = pygame.mixer.Sound('Музыка/IGotNoTime.mp3')
    game_music.set_volume(0.5)
    game_music.play()
    eat_sound = pygame.mixer.Sound('Музыка/eat_sound.mp3')
    eat_sound.set_volume(0.5)
    trash_hit = pygame.mixer.Sound('Музыка/trash_hit.mp3')
    trash_hit.set_volume(0.5)

    # Фон
    game_bg = pygame.image.load('Спрайты/game_bg.png')
    game_bg = pygame.transform.scale(game_bg, [size[0], size[1]])

    def pg_event_get():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_music.stop()
                bg_music = pygame.mixer.music.play(-1)
                import menu
                menu.menu_run()
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_music.stop()
                    bg_music = pygame.mixer.music.play(-1)
                    import menu
                    menu.menu_run()
                    run = False

    def chica_move():
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if chica_rect[0] <= size[0] - chica_w:
                chica_rect.move_ip(chica_speed, 0)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if chica_rect[0] >= 0:
                chica_rect.move_ip(-chica_speed, 0)

    def draw_some_rects(color, char_rect):
        pygame.draw.rect(window, color, char_rect, 2)

    run = True
    while run:
        pg_event_get()
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        # Случайное перемещение Грегори
        if 800 <= current_time - start_time_direction <= 1000:
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
            falling_object = random.choices(['pizza', 'trash'], weights=[20, 80], k=1)[0]

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
                    hungry += 6.5
                    if random.randint(1, 1) == 1:  # Шанс появления кэсс
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
            if current_text_index >= len(time_texts):  # ЕСЛИ НАСТУПАЕТ 6 УТРА
                current_text_index = 0

        # Заливка фона
        window.blit(game_bg, [0, 0])

        draw_some_rects('pink', cass_rect)  # Отрисовка Кэсседи

        draw_some_rects('blue', gregory_rect)  # Отрисовка Грегори

        # Балкон с Грегори
        pygame.draw.line(window, 'red', [0, 200], [520, 200], 2)

        # Пол
        pygame.draw.line(window, 'blue', [0, 590], [520, 590], 2)

        # Отрисовка падающих объектов
        for obj in trash:
            window.blit(trash_png, [obj.x, obj.y])
        for obj in pizza:
            window.blit(pizza_png, [obj.x, obj.y])

        draw_some_rects('gold', chica_rect)  # Отрисовка Чики

        # Флешка
        if cass_jump:  # Движение кэсседи
            if pygame.time.get_ticks() - cass_jump_time < 1000:
                cass_rect.move_ip(-1, 0)
            else:
                window.blit(mask, (0, 0))
                cass_rect.move_ip(1, 0)
                if pygame.time.get_ticks() - cass_jump_time > 4000:
                    cass_jump = False


        # Отрисовка надписей
        time_text = hungry_font.render(time_texts[current_text_index], False, 'yellow')
        window.blit(time_text, [75, 640])

        hungry_text = hungry_font.render(f'Насыщение: {hungry} %', False, 'yellow')
        window.blit(hungry_text, [70, 720])

        window.blit(clocks, [5, 620])
        window.blit(chica_icon, [10, 690])

        clock.tick(60)
        pygame.display.flip()
