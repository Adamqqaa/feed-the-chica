import pygame
import random

# Константы
WIDTH = 800
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Инициализируем Pygame и создаем окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flash Effect")
clock = pygame.time.Clock()

class Flash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.alpha = 255

    def update(self):
        self.alpha -= 1
        if self.alpha < 0:
            self.alpha = 0
        self.image.set_alpha(self.alpha)

all_sprites = pygame.sprite.Group()
flash = Flash()
all_sprites.add(flash)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()