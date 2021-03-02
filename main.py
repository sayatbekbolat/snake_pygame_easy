import pygame
import time

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)

pygame.init()

dis_width, dis_height = (800,600)
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake!')
font_style = pygame.font.SysFont(None, 50)

x1, y1 = (dis_width/2,dis_height/2)
x1_change, y1_change = (0,0)

snake_block = 10
snake_speed = 30

game_over = False
clock = pygame.time.Clock()

score = 0

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block

        if x1>dis_width or x1<0 or y1>dis_height or y1<0:
            game_over = True
    x1 += x1_change
    y1 += y1_change
    dis.fill(WHITE)
    pygame.draw.rect(dis, BLACK, (x1,y1,snake_block,snake_block))
    pygame.display.update()    
    clock.tick(snake_speed)

message('You lost - GAME OVER', RED)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()