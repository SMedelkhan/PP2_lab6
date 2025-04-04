import pygame
from random import randrange
import sys
 
pygame.init()

LENGTH= 600
HEIGHT = 400
screen = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
 
#Game Font
font = pygame.font.Font(None,30)
 
# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
 
# Snake Settings
s_pos = [100, 50]
s_body = [[100, 50], [90, 50], [80, 50]]
s_dir = "RIGHT"
speed = 15
 
# Food settings
f_pos = [randrange(1, (LENGTH // 10)) * 10, randrange(1, (HEIGHT // 10)) * 10]
f_spawn = False
eaten = False
game_score = 0


rect1 = pygame.Rect(90, 140, 80, 80)
rect2 = pygame.Rect(260, 140, 80, 80)
rect3 = pygame.Rect(430, 140, 80, 80)
level = 0




food_list = [[randrange(1, (LENGTH // 10)) * 10,
              randrange(1, (HEIGHT // 10)) * 10] for i in range(4)]

def spawn_food():
    while True:
        f_new = [randrange(1, (LENGTH // 10)) * 10,
                    randrange(1, (HEIGHT // 10)) * 10]
        if f_new not in s_body:
            return f_new
        
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and s_dir != "DOWN":
                s_dir = "UP"
            if event.key == pygame.K_s and s_dir != "UP":
                s_dir = "DOWN"
            if event.key == pygame.K_a and s_dir != "RIGHT":
                s_dir = "LEFT"
            if event.key == pygame.K_d and s_dir != "LEFT":
                s_dir = "RIGHT"    
 
 
 
    
    if s_dir == "UP":
        s_pos[1] -= 10
    elif s_dir == "DOWN":
        s_pos[1] += 10
    elif s_dir == "LEFT":
        s_pos[0] -= 10
    elif s_dir == "RIGHT":
        s_pos[0] += 10
 
 
    
    s_body.insert(0, list(s_pos))  
   

    if s_pos == f_pos:
        f_spawn = True
        game_score += 1
    else:
        s_body.pop()
 

         

    if f_spawn:
        f_pos = [randrange(1, (LENGTH // 10)) * 10, randrange(1, (HEIGHT // 10)) * 10]
        f_spawn = False
    
    

    

        
    #Collisions
    
    if s_pos[0] < 0 or s_pos[0] >= LENGTH or s_pos[1] < 0 or s_pos[1] >= HEIGHT:
        running = False
 
    for block in s_body[1:]:
        if s_pos == block:
            running = False
   
   
    # Update
    screen.fill(GREEN)
    for p in s_body:
        pygame.draw.rect(screen, BLACK, pygame.Rect(p[0], p[1], 10, 10))
    
    pygame.draw.rect(screen, RED, pygame.Rect(f_pos[0], f_pos[1], 10, 10))
 
    game_score_text = font.render(f"Your score: {game_score}",True,WHITE)
    screen.blit(game_score_text,(20,20))
    pygame.display.update()
 
    pygame.display.flip()
    clock.tick(speed)
   
 
 
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (LENGTH / 2, HEIGHT / 2)
screen.blit(game_over_text,game_over_rectangle)

pygame.display.update()
pygame.time.wait(1000)

