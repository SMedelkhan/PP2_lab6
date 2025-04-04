import pygame
from pygame.locals import *
from random import randint

pygame.init()

# Основные параметры
FPS = 120
clock = pygame.time.Clock()

LENGTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((LENGTH, HEIGHT))
screen_color = (255, 255, 255)
pygame.display.set_caption("Raser")

# Загрузка изображений
p_image = pygame.image.load("lab8/img/Player.png")
e_image = pygame.image.load("lab8/img/Enemy.png")
c_image = pygame.image.load("lab8/img/BuffCoin.png")
bg_image = pygame.image.load("lab8/img/AnimatedStreet.png")

# Font
font = pygame.font.Font(None , 36)


# Игрок
p_x, p_y = 200, 500
p_l, p_h = 44, 96
p_vel = 3 

# Враг
e_l, e_h = 48, 93
e_x = randint(0, LENGTH - e_l)
e_y = -e_h
e_vel = 6

# fone
bg_y1 = -HEIGHT
bg_y2 = 0
bg_vel = p_vel

# Монета (квадрат)
c_l, c_h = 86, 86  # Размеры монеты
c_x = randint(0, LENGTH - c_l)
c_y = -c_h
c_vel = 3
score = 0

def spawn_enemy():
    """Спавнит врага сверху в случайной позиции."""
    global e_x, e_y  
    e_x = randint(0, LENGTH - e_l)
    e_y = -e_h

def spawn_coin():
    """Спавнит монету сверху в случайной позиции."""
    global c_x, c_y  
    c_x = randint(0, LENGTH - c_l)
    c_y = -c_h

# Состояние клавиш
move_left = move_right = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_d:
                move_right = True
            if event.key == K_a:
                move_left = True
        elif event.type == KEYUP:
            if event.key == K_d:
                move_right = False
            if event.key == K_a:
                move_left = False

    # Движение игрока
    if move_right and p_x + p_vel + p_l < LENGTH:
        p_x += p_vel
    if move_left and p_x - p_vel > 0:
        p_x -= p_vel

    # Обновление хитбоксов
    p_rect = pygame.Rect(p_x, p_y, p_l, p_h)
    e_rect = pygame.Rect(e_x, e_y, e_l, e_h)
    c_rect = pygame.Rect(c_x, c_y, c_l, c_h)

    # движение фона
    bg_y1 += bg_vel
    bg_y2 += bg_vel

    if bg_y1 >= HEIGHT:
        bg_y1 = -HEIGHT
    if bg_y2 >= HEIGHT:
        bg_y2 = -HEIGHT

    # Движение врага
    e_y += e_vel  
    if e_y > HEIGHT:  
        spawn_enemy()  

    # Проверка столкновения игрока с врагом
    if p_rect.colliderect(e_rect):
        running = False  

    # Движение монеты
    c_y += c_vel  
    if c_y > HEIGHT:  
        spawn_coin()  

    # Проверка столкновения игрока с монетой (квадратный хитбокс)
    if p_rect.colliderect(c_rect):
        score += 1
        spawn_coin()

    # Обновление экрана
    screen.blit(bg_image , (0 , bg_y1))
    screen.blit(bg_image , (0 , bg_y2))
    screen.blit(p_image, (p_x, p_y))
    screen.blit(e_image, (e_x, e_y))
    screen.blit(c_image, (c_x, c_y))
    score_text = font.render(f"Your score: {score}" , True , (0 , 0 , 0))
    screen.blit(score_text , ((210 , 20)))
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
