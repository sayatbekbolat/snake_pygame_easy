import pygame
import time
import random

WHITE = (149, 165, 166)
BLUE = (0,0,255)
RED = (231, 76, 60)
BLACK = (0,0,0)
BACKGROUND = (26, 188, 156)
GAME_FINISH = (231, 76, 60)
WET_ASPHALT = (52, 73, 94)
pygame.init()

dis_width, dis_height = (800,600)
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake!')

font_style = pygame.font.SysFont('bahnschrift', 50)
score_font = pygame.font.SysFont('comicsansms', 50, bold=False, italic=True)

snake_block = 20
snake_speed = 15    

clock = pygame.time.Clock()

def your_score(score):
    valeu = score_font.render('Your score: ' + str(score), True, WHITE)
    dis.blit(valeu, [20,20])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, RED, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/8, dis_height/3])

def gameloop():
    
    game_over = False
    game_close = False

    x1, y1 = (dis_width/2,dis_height/2)
    x1_change, y1_change = (0,0)

    snake_list = []
    snake_len = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close:
            dis.fill(GAME_FINISH)
            message("You Lost! Press C-Play Again or Q-Quit", WET_ASPHALT)
            your_score(snake_len-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
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

        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(WET_ASPHALT)

        pygame.draw.rect(dis, RED, (foodx, foody, snake_block, snake_block))

        snake_head = list()
        snake_head.append(x1)
        snake_head.append(y1)
        
        snake_list.append(snake_head)

        if len(snake_list)>snake_len:
            del snake_list[0]
        
        our_snake(snake_block, snake_list)

        your_score(snake_len-1)
        pygame.display.update()    

        if x1==foodx and y1==foody:

            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            snake_len += 1
            print('Yammy')
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameloop()