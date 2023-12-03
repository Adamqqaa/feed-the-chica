import pygame
from pygame.display import set_caption


def menu_run():
    pygame.init()
    size = [520, 760]
    window = pygame.display.set_mode(size)
    pygame.display.set_icon(pygame.image.load('icon.png'))
    set_caption('Feed The Chica: Menu')

    fontItem = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 45)
    fontItemSelect = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 50)

    chica_menu = pygame.image.load('Спрайты/chica_menu.png')
    chica_menu = pygame.transform.scale(chica_menu, [450, 420])

    black_blur = pygame.image.load('Спрайты/black_blur.png')
    black_blur = pygame.transform.scale(black_blur, [520, 760])

    menu_bg = pygame.image.load('Спрайты/pizza_bgpng.png')
    menu_bg = pygame.transform.scale(menu_bg, size)

    put_down = pygame.mixer.Sound('Музыка/put_down.mp3')
    put_down.set_volume(0.4)

    choose = pygame.mixer.Sound('Музыка/choosing.mp3')
    choose.set_volume(0.6)

    bg_music = pygame.mixer.music.load('Музыка/menu_bg_sound.mp3')
    bg_music = pygame.mixer.music.play(-1)

    items = ['Играть', '', 'Настройки', '', 'Разработчик', '', 'Выход']
    itemsSelect = ['Играть', '', 'Настройки', '', 'Разработчик', '', 'Выход']

    select = 0
    selectAdd = 0

    run = True
    while run:

        keys = pygame.key.get_focused()
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
                elif event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    if items[select] == 'Выход':
                        choose.play()
                        run = False
                    elif items[select] == 'Играть':
                        choose.play()
                        bg_music = pygame.mixer.music.stop()
                        import training
                        training.training_run()
                    elif items[select] == 'Настройки':
                        choose.play()
                        import settings
                        settings.settings_run()
                    elif items[select] == 'Разработчик':
                        choose.play()
                        import developer
                        developer.developer_run()
                select = (select + selectAdd) % len(items)
                while items[select] == '':
                    select = (select + selectAdd) % len(items)

                selectAdd = 0
        window.blit(menu_bg, [0, 0])
        window.blit(black_blur, [0, 0])
        window.blit(chica_menu, [40, 350])
        for i in range(len(items)):
            if i == select:
                text = fontItemSelect.render(itemsSelect[i], 0, [216, 166, 19])
            else:
                text = fontItem.render(items[i], 0, [217, 166, 119])

            rect = text.get_rect(center=(size[0] // 2, 70 + 40 * i))
            window.blit(text, rect)
        pygame.display.flip()
    pygame.quit()
    quit()
menu_run()