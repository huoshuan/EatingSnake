import sys
import pygame
import random

"""构建蛇的基本类型"""
class Snake:
    def __init__(self, screen):
        self.position = [0,0]
        self.next = None
        self.screen = screen

    def print_snake(self):
        pygame.draw.rect(self.screen,(255,255,255), (self.position[0] * 12 + 20, self.position[1] * 12 + 20, 10, 10))

    def pass_transform(self):
        if(self.next != None):
            self.next.position[0] = self.position[0]
            self.next.position[1] = self.position[1]

##递归蛇身体的移动
def snake_body_move(snake_head:Snake, chessboard:[[]]):
    if(snake_head.next.next != None):
        snake_body_move(snake_head.next, chessboard)
        snake_head.pass_transform()
    else:
        chessboard[snake_head.next.position[0]][snake_head.next.position[1]] = 0
        snake_head.pass_transform()

##上下左右
def snake_move(screen, snake_head:Snake, move_direction:int, chessboard:[[]], score:int):
    if(move_direction == 0):
        if (chessboard[snake_head.position[0]][snake_head.position[1] - 1] == 2):
            score += 1
            chessboard[snake_head.position[0]][snake_head.position[1] - 1] = 0
            creat_egg(chessboard)
            head = Snake(screen)
            head.position = [snake_head.position[0], snake_head.position[1] - 1]
            head.next = snake_head
            snake_head = head

        snake_body_move(snake_head, chessboard)

        if (chessboard[snake_head.position[0]][snake_head.position[1] - 1] == 1):
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        snake_head.position[1] -= 1
        chessboard[snake_head.position[0]][snake_head.position[1]] = 1
        
    elif (move_direction == 1):
        if (chessboard[snake_head.position[0]][snake_head.position[1] + 1] == 2):
            score += 1
            chessboard[snake_head.position[0]][snake_head.position[1] + 1] = 0
            creat_egg(chessboard)
            head = Snake(screen)
            head.position = [snake_head.position[0], snake_head.position[1] + 1]
            head.next = snake_head
            snake_head = head

        snake_body_move(snake_head, chessboard)

        if (chessboard[snake_head.position[0]][snake_head.position[1] + 1] == 1):
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        snake_head.position[1] += 1
        chessboard[snake_head.position[0]][snake_head.position[1]] = 1

    elif (move_direction == 2):
        if (chessboard[snake_head.position[0] - 1][snake_head.position[1]] == 2):
            score += 1
            chessboard[snake_head.position[0] - 1][snake_head.position[1]] = 0
            creat_egg(chessboard)
            head = Snake(screen)
            head.position = [snake_head.position[0] - 1, snake_head.position[1]]
            head.next = snake_head
            snake_head = head

        snake_body_move(snake_head, chessboard)

        if (chessboard[snake_head.position[0] - 1][snake_head.position[1]] == 1):
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        snake_head.position[0] -= 1
        chessboard[snake_head.position[0]][snake_head.position[1]] = 1

    elif (move_direction == 3):
        if (chessboard[snake_head.position[0] + 1][snake_head.position[1]] == 2):
            score += 1
            chessboard[snake_head.position[0] + 1][snake_head.position[1]] = 0
            creat_egg(chessboard)
            head = Snake(screen)
            head.position = [snake_head.position[0] + 1, snake_head.position[1]]
            head.next = snake_head
            snake_head = head

        snake_body_move(snake_head, chessboard)

        if (chessboard[snake_head.position[0] + 1][snake_head.position[1]] == 1):
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        snake_head.position[0] += 1
        chessboard[snake_head.position[0]][snake_head.position[1]] = 1

    return snake_head, score

def snake_print(snake_head:Snake):
    pointer = snake_head
    while (pointer != None):
        pointer.print_snake()
        pointer = pointer.next

def creat_egg(chessboard:[[]]):
    random_x = random.randint(1,28)
    random_y = random.randint(1,28)
    chessboard[random_x][random_y] = 2
    return random_x, random_y

def print_egg(screen, chessboard:[[]]):
    for i in range(30):
        for j in range(30):
            if(chessboard[i][j] == 2):
                pygame.draw.rect(screen, (255, 255, 255), (i * 12 + 20, j * 12 + 20, 10, 10))

def creat_chessboard():
    chseeboard = []
    for i in range(30):
        line = []
        for j in range(30):
            line.append(0)
        chseeboard.append(line)

    for i in range(30):
        chseeboard[0][i] = 1
        chseeboard[29][i] = 1
        chseeboard[i][0] = 1
        chseeboard[i][29] = 1
    return chseeboard

def print_chessboard(screen):
    for i in range(30):
        pygame.draw.rect(screen, (255, 255, 255), (0 * 12 + 20, i * 12 + 20, 10, 10))
        pygame.draw.rect(screen, (255, 255, 255), (29 * 12 + 20, i * 12 + 20, 10, 10))
        pygame.draw.rect(screen, (255, 255, 255), (i * 12 + 20, 0 * 12 + 20, 10, 10))
        pygame.draw.rect(screen, (255, 255, 255), (i * 12 + 20, 29 * 12 + 20, 10, 10))

def init_game(screen, game_mode:int, game_difficulty:int):
    if(game_mode == 1):
        head = Snake(screen)
        head.position = [3, 2]
        head.next = Snake(screen)
        head.next.position = [2, 2]
        head.next.next = None

    else:
        head_1 = Snake(screen)
        head_1.position = [3, 2]
        head_1.next = Snake(screen)
        head_1.next.position = [2, 2]
        head_1.next.next = None

        head_2 = Snake(screen)
        head_2.position = [3, 27]
        head_2.next = Snake(screen)
        head_2.next.position = [2, 27]
        head_2.next.next = None

    if(game_difficulty == 1):
        game_speed = 1000
    elif(game_difficulty == 2):
        game_speed = 500
    else:
        game_speed = 100

    chessboard = creat_chessboard()
    creat_egg(chessboard)

    if(game_mode == 1):
        return head, game_speed, chessboard
    else:
        return head_1, head_2, game_speed, chessboard

def print_startmenu(screen):
    f = pygame.font.Font("C:\Windows\Fonts\simfang.ttf", 20)
    #f = pygame.font.Font(None, 20)
    text = f.render("贪吃蛇", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (200, 120)
    screen.blit(text, textRect)

    text = f.render("请选择难度：按e简单；按m中等；按h困难", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (200, 180)
    screen.blit(text, textRect)

    text = f.render("请选择人数：按1单人游戏；按2双人游戏", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (200, 240)
    screen.blit(text, textRect)

    text = f.render("选择好后，按enter开始游戏", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (200, 330)
    screen.blit(text, textRect)

def print_score(screen, score):
    f = pygame.font.Font("C:\Windows\Fonts\simfang.ttf", 20)
    score_text = f.render(score,True,(255, 255, 255),(0, 0, 0))
    textRect = score_text.get_rect()
    textRect.center = (200, 550)
    screen.blit(score_text, textRect)

def print_score(screen, score1:int, score2:int, isSingle:bool):
    f = pygame.font.Font("C:\Windows\Fonts\simfang.ttf", 80)

    if(isSingle):
        score_text = f.render(str(score1), True, (255, 255, 255), (0, 0, 0))
        textRect = score_text.get_rect()
        textRect.center = (200, 500)
        screen.blit(score_text, textRect)

    else:
        score_text = f.render(str(score1), True, (255, 255, 255), (0, 0, 0))
        textRect = score_text.get_rect()
        textRect.center = (100, 500)
        screen.blit(score_text, textRect)

        score_text = f.render(str(score2), True, (255, 255, 255), (0, 0, 0))
        textRect = score_text.get_rect()
        textRect.center = (300, 500)
        screen.blit(score_text, textRect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400,600))
    pygame.display.set_caption('贪吃蛇')

    clock = pygame.time.Clock()

    timer = 0
    in_game = False
    game_mode = 0
    game_difficulty = 0
    snake_speed = 500
    head = None
    head_1 = None
    head_2 = None
    chessboard = None
    direction_num_1 = 3
    direction_num_2 = 3

    score = 0
    score1 = 0
    score2 = 0
    '''snake_speed = 500
    direction_num = 3
    
    chessboard = creat_chessboard()
    creat_egg(chessboard)

    head = Snake(screen)
    head.position = [3,2]
    head.next = Snake(screen)
    head.next.position = [2,2]
    head.next.next = None'''

    

    while True:
        if(in_game == False):
            print_startmenu(screen)
        else:
            screen.fill((0,0,0))
            print_chessboard(screen)
            print_egg(screen, chessboard)

            if(timer>=game_speed):
              if game_mode == 1: 
                head, score = snake_move(screen, head, direction_num_1, chessboard, score)
              elif game_mode == 2:
                head_1, score1 = snake_move(screen, head_1, direction_num_1, chessboard, score1)
                head_2, score2 = snake_move(screen, head_2, direction_num_2, chessboard, score2)
                
              timer = 0
            delta_time = clock.tick(60)

            timer += delta_time
            
            if game_mode == 1:
              snake_print(head)
              print_score(screen, score, 0, True)
            elif game_mode == 2:
              snake_print(head_1)
              snake_print(head_2)
              print_score(screen, score1, score2, False)
            		
              

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and in_game == False:
                    game_difficulty = 1
                if event.key == pygame.K_m and in_game == False:
                    game_difficulty = 2
                if event.key == pygame.K_h and in_game == False:
                    game_difficulty = 3
                if event.key == pygame.K_1 and in_game == False:
                    game_mode = 1
                if event.key == pygame.K_2 and in_game == False:
                    game_mode = 2
                if event.key == pygame.K_RETURN and in_game == False and game_mode != 0 and game_difficulty != 0:
                    in_game = True
                    if game_mode == 1:
                      head, game_speed, chessboard = init_game(screen, game_mode, game_difficulty)
                    elif game_mode == 2:
                      head_1, head_2, game_speed, chessboard = init_game(screen, game_mode, game_difficulty)
                if event.key == pygame.K_UP:
                    direction_num_1 = 0
                if event.key == pygame.K_DOWN:
                    direction_num_1 = 1
                if event.key == pygame.K_LEFT:
                    direction_num_1 = 2
                if event.key == pygame.K_RIGHT:
                    direction_num_1 = 3
                if event.key == pygame.K_w:
                    direction_num_2 = 0
                if event.key == pygame.K_s:
                    direction_num_2 = 1
                if event.key == pygame.K_a:
                    direction_num_2 = 2
                if event.key == pygame.K_d:
                    direction_num_2 = 3


        pygame.display.flip()


main()