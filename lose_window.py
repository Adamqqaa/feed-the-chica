import pygame
from pygame.display import set_caption


def lose_window():
	pygame.init()
	size = [520, 760]
	window = pygame.display.set_mode(size)
	pygame.display.set_icon(pygame.image.load('icon.png'))
	set_caption('You Lose. . .')
	clock = pygame.time.Clock()

	fontItem = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 60)
	u_lose = fontItem.render('You lose. . .', False, 'white')

	scary_music = pygame.mixer.Sound('Музыка/end_game.mp3')
	scary_music.play(-1)

	scary_chica = pygame.image.load('Спрайты/spooky_scary_chica.png')
	scary_chica = pygame.transform.scale(scary_chica, [size[0], size[0]])

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
		window.fill([0, 0, 0])
		window.blit(u_lose, [size[0] // 2 - 180, size[1] // 5])
		window.blit(scary_chica, [20, 240])
		clock.tick(60)
		pygame.display.flip()
	pygame.quit()
	quit()
