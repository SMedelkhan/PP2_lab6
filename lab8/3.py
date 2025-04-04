import pygame
import math

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None , 36)
remove_text = font.render("REMOVE", True, (255 , 255 , 255))
remove_rect = pygame.Rect(800 , 5 , 150 , 50)

# colors
WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (140,140,140)
DARK_GRAY = (100,100,100)

# display
screen_l = 1000
screen_h = 700
screen = pygame.display.set_mode((screen_l , screen_h))
pygame.display.set_caption("Paint")

running = True
drawing = False
brush_selected = True  # Флаг выбора кисти
brush_radius = 5
circle_selected = False
rect_selected = False

img_brush = pygame.transform.scale(pygame.image.load("lab8/img/brush.png"), (50, 50))
rect_brush = pygame.Rect(425, 5, 50, 50)

img_eraser = pygame.transform.scale(pygame.image.load("lab8/img/eraser.png"), (50, 50))
rect_eraser = pygame.Rect(500, 5, 50, 50)

img_circle = pygame.transform.scale(pygame.image.load("lab8/img/circle.png"), (50, 50))
rect_circle = pygame.Rect(600 , 5 , 50 , 50)
c_top_l = None
c_bottom_r = None

img_rect = pygame.transform.scale(pygame.image.load("lab8/img/rect.png"), (50, 50))
rect_rect = pygame.Rect(700, 5, 50, 50)
r_top_l = None
r_bottom_r = None

img_color = pygame.transform.scale(pygame.image.load("lab8/img/color.png"), (50, 50))
red_rect = pygame.Rect(80 , 5 , 50 , 50)
blue_rect = pygame.Rect(135 , 5 , 50 , 50)
green_rect = pygame.Rect(190 , 5 , 50 , 50)
black_rect = pygame.Rect(245 , 5 , 50 , 50)
white_rect = pygame.Rect(300 , 5 , 50 , 50)
darkgray_rect = pygame.Rect(355 , 5 , 50 , 50)



icon = pygame.Rect(0 ,0 , screen_l , 100)

current_color = BLACK
last_pos = None  # Для сглаживания рисования

screen.fill(WHITE)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if red_rect.collidepoint(event.pos):
                current_color = RED
            elif blue_rect.collidepoint(event.pos):
                current_color = BLUE
            elif green_rect.collidepoint(event.pos):
                current_color = GREEN
            elif black_rect.collidepoint(event.pos):
                current_color = BLACK
            elif darkgray_rect.collidepoint(event.pos):
                current_color = DARK_GRAY
            elif white_rect.collidepoint(event.pos):
                current_color = WHITE
            elif rect_eraser.collidepoint(event.pos):
                current_color = WHITE
                brush_selected = True
                circle_selected = False
                rect_selected = False
            elif remove_rect.collidepoint(event.pos):
                screen.fill(WHITE)

            if rect_brush.collidepoint(event.pos):
                brush_selected = True
                circle_selected = False
                rect_selected = False
                brush_radius = 5
            elif rect_circle.collidepoint(event.pos):
                brush_selected = False
                circle_selected = True
                rect_selected = False
            elif rect_rect.collidepoint(event.pos):
                brush_selected = False
                circle_selected = False
                rect_selected = True
            elif brush_selected:
                drawing = True
                last_pos = event.pos
            elif circle_selected:
                c_top_l = event.pos
                drawing = True
            elif rect_selected:
                r_top_l = event.pos
                drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if brush_selected:
                drawing = False
                last_pos = None
            elif circle_selected and drawing:
                c_bottom_r = event.pos
                drawing = False
                dx = c_bottom_r[0] - c_top_l[0]
                dy = c_bottom_r[1] - c_top_l[1]
                radius = int(math.hypot(dx, dy))
                pygame.draw.circle(screen, current_color, c_top_l, radius)
            elif rect_selected and drawing:
                r_bottom_r = event.pos
                drawing = False
                x = min(r_top_l[0], r_bottom_r[0])
                y = min(r_top_l[1], r_bottom_r[1])
                width = abs(r_bottom_r[0] - r_top_l[0])
                height = abs(r_bottom_r[1] - r_top_l[1])
                pygame.draw.rect(screen, current_color, (x, y, width, height))

        if event.type == pygame.MOUSEMOTION and drawing and brush_selected:
            if last_pos:
                pygame.draw.line(screen, current_color, last_pos, event.pos, brush_radius)
            last_pos = event.pos

    pygame.draw.rect(screen , GRAY , icon)

    screen.blit(img_color , (5 , 5))
    pygame.draw.rect(screen , RED , red_rect)
    pygame.draw.rect(screen , BLUE , blue_rect)
    pygame.draw.rect(screen , GREEN , green_rect)
    pygame.draw.rect(screen , BLACK , black_rect)
    pygame.draw.rect(screen , WHITE , white_rect)
    pygame.draw.rect(screen , DARK_GRAY , darkgray_rect)

    screen.blit(img_brush , (425, 5))
    screen.blit(img_eraser , (500, 5))
    screen.blit(img_circle , (600, 5))
    screen.blit(img_rect , (700, 5))

    pygame.draw.rect(screen , DARK_GRAY , remove_rect)
    screen.blit(remove_text , (820 , 15 , 150 , 50))

    pygame.display.update()
    clock.tick(60)
