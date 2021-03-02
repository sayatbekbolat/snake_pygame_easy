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
    mesg = pygame.font.render(msg, True, color)
    dis.blit = (mesg, [dis_width/2, dis_height/2])
    
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
        
    x1 += x1_change
    y1 += y1_change
    dis.fill(WHITE)
    pygame.draw.rect(dis, BLACK, (x1,y1,10,10))
    pygame.display.update()    
    clock.tick(30)
pygame.quit()
quit()